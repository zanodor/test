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

branch = subprocess.check_output("git rev-parse --abbrev-ref HEAD",
                                 shell=True)

if branch == b"master\n":
    sys.exit(0)

header, *filenames = subprocess.check_output("git log -1 --stat --oneline --name-only",
                                              shell=True).splitlines()

files = Path("/home/zan/Obsidian/test/").rglob("*-*.md")

for file in files:
    text = file.read_text(encoding="utf-8")  # Adjust encoding if needed

    # Replace the regex patterns as needed
    ntext = re.sub(r"!(\[\[.+\]\])", r"\1", text)  # ![[imagename]] --> [[imagename]]
    ntext = re.sub(r"\[\[(.+?)\|(.+?)\]\]", r"[[\2|\1]]", ntext)  # [[fn|linkTitle]] -> [[linkTitle|fn]]

    # Check if changes are needed
    if ntext != text:
        # Write the modified content back to the file
        file.write_text(ntext, encoding="utf-8")  # Adjust encoding if needed
        print(f"Changes applied to: {file}")

subprocess.run("git add -A && git commit -m 'Message'",
                shell=True)

subprocess.run("git checkout main",
                shell=True)#

subprocess.run("git checkout master&&git merge --strategy-option theirs main",
                shell=True)

subprocess.run("git checkout main -- .",
                shell=True)
