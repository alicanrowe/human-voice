#!/usr/bin/env python3
"""Flag patterns that make text read as machine-written.

usage: python3 voice_check.py [file ...]   (reads stdin when no file is given)
Exit 1 when anything is flagged, so it can gate a publish step.
"""
import re, sys

STOCK = [
    "delve", "tapestry", "testament to", "journey", "elevate", "seamless", "curated", "unleash", "vibrant",
    "realm", "crafted with care", "labor of love", "labour of love", "more than just", "whether you're",
    "in today's world", "let's dive in", "dive into", "game-changer", "game changer", "nestled", "boasts",
    "meticulously", "embark", "a symphony of", "evokes", "speaks to", "timeless", "elevated",
]
CHECKS = [
    ("em/en dash", re.compile(r"[—–]|\s--\s")),
    ("'not X, but Y' swap", re.compile(r"\b(?:not|isn't|wasn't|aren't)\b[^.!?\n]{1,60}?(?:,|;)\s*(?:but|it's|it is|they're)\b", re.I)),
    ("'X for Y' swap", re.compile(r"\b(?:trad(?:e|es|ed|ing)|swap(?:s|ped|ping)?|exchang(?:e|es|ed|ing))\b[^.!?\n]{1,40}?\bfor\b", re.I)),
    ("list of three", re.compile(r"\b[\w'-]+(?: [\w'-]+){0,2}, [\w'-]+(?: [\w'-]+){0,2},? (?:and|or) [\w'-]+", re.I)),
    ("rhetorical question opener", re.compile(r"(?:^|\n)\s*(?:Ever|Have you ever|What if|Imagine)\b[^?\n]*\?", re.I)),
    ("stock word", re.compile(r"\b(?:" + "|".join(re.escape(w) for w in STOCK) + r")\b", re.I)),
]


def check(text):
    hits = []
    for lineno, line in enumerate(text.splitlines(), 1):
        for name, rx in CHECKS:
            for m in rx.finditer(line):
                hits.append((lineno, name, m.group(0).strip()))
    return hits


def main():
    srcs = [(p, open(p, encoding="utf-8").read()) for p in sys.argv[1:]] or [("stdin", sys.stdin.read())]
    total = 0
    for name, text in srcs:
        for lineno, kind, frag in check(text):
            print(f"{name}:{lineno}: {kind}: {frag!r}")
            total += 1
    print(f"{total} flag(s)" if total else "clean")
    sys.exit(1 if total else 0)


if __name__ == "__main__":
    main()
