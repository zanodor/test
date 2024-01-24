#!/usr/bin/env python3
import sys
import re
import subprocess
from pathlib import Path

"""
limitation:
process all filenames with dash -> space   *-*.md
https://forum.obsidian.md/t/github-wiki-kinda-works-to-host-the-wiki/2980
"""

branch = subprocess.check_output("git rev-parse --abbrev-ref HEAD", shell=True)

if branch != b"main\n":
    sys.exit(0)

header, *filenames = subprocess.check_output(
    "git log -1 --stat --oneline --name-only", shell=True
).splitlines()

subprocess.run("git checkout main && git merge --strategy-option theirs master", shell=True)

files = [Path(f.decode()) for f in filenames if f.endswith(b".md")]

for file in files:
    text = file.read_text()
    ntext = re.sub(r"!(\[\[.+\]\])", r"\1", text)  # ![[imagename]] --> [[imagename]]
    ntext = re.sub(r"\[\[(.+?)\|(.+?)\]\]", r"[[\2|\1]]", ntext)  # [[fn|linkTitle]] -> [[linkTitle|fn]]
    if ntext != text:
        file.write_text(ntext)

subprocess.run("git add -A && git commit -m 'Message'", shell=True)

subprocess.run("git checkout master", shell=True)
