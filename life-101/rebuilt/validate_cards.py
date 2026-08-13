#!/usr/bin/env python3
"""Validator for RemNote card files, per remnote-card-designer spec.
Usage: validate_cards.py FILE [FILE...]
"""
import sys, re, collections

TARGETS = {  # (low, high) percentage
    'concept': (20, 30), 'descriptor': (15, 25), 'basic': (40, 50),
    'cloze': (0, 5), 'set': (5, 10), 'sequence': (5, 10),
}
PRIORITY_TAGS = {'##core-concept','##big-picture','##connection','##practical',
                 '##confusing','##prerequisite','##high-frequency'}

def classify(line):
    s = line.rstrip()
    if not s.strip():
        return None
    body = s.strip()
    if re.search(r'\s1\.\s*>>>\s*$', body) or re.search(r'\s1\.\s*>>>\s+#', body):
        return 'sequence'
    if re.search(r'>>>\s*$', body) or re.search(r'>>>\s+#', body):
        return 'set'
    if '{{' in body and '::' not in body and '>>' not in body and ';;' not in body:
        return 'cloze'
    if '>>' in body and not body.count('>>>'):
        return 'basic'
    if ';;' in body:
        return 'descriptor'
    if '::' in body:
        return 'concept'
    return None

def answer_of(body):
    for d in ('>>>', '>>', ';;', '::'):
        if d in body:
            return body.split(d, 1)[1].strip()
    return ''

def validate(path):
    lines = open(path, encoding='utf-8').read().split('\n')
    counts = collections.Counter()
    issues = []
    prompts = collections.defaultdict(list)
    concept_stack = []  # (indent, has_concept)
    list_parent = None
    for n, l in enumerate(lines, 1):
        if not l.strip():
            continue
        indent = len(l) - len(l.lstrip())
        t = classify(l)
        body = l.strip()
        if list_parent is not None and indent <= list_parent:
            list_parent = None

        # markdown bullets banned EXCEPT as Set/Sequence items (per skill spec)
        if body.startswith(('- ', '* ', '+ ')) or re.match(r'^\d+\.\s', body):
            if not (list_parent and indent > list_parent):
                issues.append((n, 'CRITICAL', 'markdown bullet outside a Set/Sequence', body[:70]))
            continue
        if re.search(r'\*\*|__', body):
            issues.append((n, 'MAJOR', 'markdown bold in card text', body[:70]))
        # banned legacy delimiters
        for bad in ('↔', '→', '←', '―'):
            if bad in body:
                issues.append((n, 'CRITICAL', f'legacy arrow delimiter {bad}', body[:70]))
        # cloze balance
        if body.count('{{') != body.count('}}'):
            issues.append((n, 'CRITICAL', 'unbalanced cloze braces', body[:70]))

        if t is None:
            # plain structural line (topic/section) — track for descriptor nesting
            while concept_stack and concept_stack[-1][0] >= indent:
                concept_stack.pop()
            continue

        counts[t] += 1
        if t in ('set','sequence'): list_parent = indent
        ans = answer_of(body)
        words = len(ans.split())

        # length rules
        if t in ('basic', 'concept', 'descriptor'):
            if words > 30:
                issues.append((n, 'MAJOR', f'answer {words} words (>30 = decompose)', body[:70]))
            elif words > 20 and t == 'descriptor':
                issues.append((n, 'MINOR', f'descriptor {words} words (ideal 1-15)', body[:70]))

        # descriptor must nest under a concept
        while concept_stack and concept_stack[-1][0] >= indent:
            concept_stack.pop()
        if t == 'descriptor' and not concept_stack:
            issues.append((n, 'MAJOR', 'descriptor has no parent Concept ::', body[:70]))
        if t == 'concept':
            concept_stack.append((indent, body.split('::',1)[0].strip().lower()))

        # prompt extraction + duplicate/answer-in-prompt checks
        for d in ('>>>', '>>', ';;', '::'):
            if d in body:
                p = body.split(d, 1)[0].strip()
                break
        p_clean = re.sub(r'\s+', ' ', p).lower()
        if t == 'descriptor':
            parent = concept_stack[-1][1] if concept_stack else ''
            p_clean = f'{parent}>{p_clean}'
        if p_clean:
            prompts[p_clean].append(n)
        # answer-in-prompt
        for c in re.findall(r'\{\{(.+?)\}\}', ans):
            core = re.sub(r'[^0-9a-z%$.]', '', c.lower())
            if len(core) > 1 and core in re.sub(r'[^0-9a-z%$.]', '', p_clean):
                issues.append((n, 'MAJOR', f'cloze "{c}" leaked into prompt', body[:70]))
        # yes/no recognition
        if t == 'basic' and re.match(r'^(is|are|does|do|can|will|should|did)\b', p_clean) and \
           re.match(r'^(yes|no)\b', ans.lower()):
            issues.append((n, 'MAJOR', 'yes/no recognition card', body[:70]))

    for p, ns in prompts.items():
        if len(ns) > 1:
            issues.append((ns[1], 'MAJOR', f'duplicate prompt (also line {ns[0]})', p[:70]))

    total = sum(counts.values())
    return counts, total, issues

def report(paths):
    grand = collections.Counter(); gtot = 0; allissues = 0
    for path in paths:
        counts, total, issues = validate(path)
        grand.update(counts); gtot += total
        crit = sum(1 for i in issues if i[1] == 'CRITICAL')
        maj = sum(1 for i in issues if i[1] == 'MAJOR')
        mino = sum(1 for i in issues if i[1] == 'MINOR')
        allissues += crit + maj
        name = path.split('/')[-1]
        print(f'\n=== {name}  ({total} cards)  critical:{crit} major:{maj} minor:{mino}')
        if total:
            for t in ('concept','descriptor','basic','cloze','set','sequence'):
                pct = 100*counts[t]//total if total else 0
                lo, hi = TARGETS[t]
                flag = '' if lo <= pct <= hi else '  <-- off target'
                print(f'    {t:11} {counts[t]:5} {pct:3}%   target {lo}-{hi}%{flag}')
        for n, sev, msg, ctx in issues[:12]:
            print(f'    [{sev}] line {n}: {msg}')
            print(f'             {ctx}')
        if len(issues) > 12:
            print(f'    ... and {len(issues)-12} more')
    if len(paths) > 1 and gtot:
        print(f'\n=== TOTAL ({gtot} cards)')
        for t in ('concept','descriptor','basic','cloze','set','sequence'):
            pct = 100*grand[t]//gtot
            lo, hi = TARGETS[t]
            flag = '' if lo <= pct <= hi else '  <-- off target'
            print(f'    {t:11} {grand[t]:5} {pct:3}%   target {lo}-{hi}%{flag}')
    print(f'\nBlocking issues (critical+major): {allissues}')
    return allissues

if __name__ == '__main__':
    sys.exit(1 if report(sys.argv[1:]) else 0)
