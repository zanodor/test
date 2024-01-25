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

# Get the current branch
branch = subprocess.check_output("git rev-parse --abbrev-ref HEAD", shell=True).strip().decode()

# Exit if the branch is already master
if branch == "master":
    sys.exit(0)

# Log information for the last commit
header, *filenames = subprocess.check_output("git log -1 --stat --oneline --name-only", shell=True).splitlines()

# Define the root directory for Markdown files
root_directory = Path("/home/zan/Obsidian/test/")

# Regex patterns for replacements
pattern_image = re.compile(r"!(\[\[.+\]\])")
pattern_wikilink = re.compile(r"\[\[(.+?)\|(.+?)\]\]")

# Iterate through Markdown files
for file in root_directory.rglob("*-*.md"):
    text = file.read_text(encoding="utf-8")

    # Replace the regex patterns
    ntext = pattern_image.sub(r"\1", text)  # ![[imagename]] --> [[imagename]]
    ntext = pattern_wikilink.sub(r"[[\2|\1]]", ntext)  # [[fn|linkTitle]] -> [[linkTitle|fn]]

    # Check if changes are needed
    if ntext != text:
        # Write the modified content back to the file
        file.write_text(ntext, encoding="utf-8")
        print(f"Changes applied to: {file}")

# Add and commit changes to the current branch
subprocess.run(["git", "add", "-A"])
subprocess.run(["git", "commit", "-m", "Message"])

# Switch to the master branch and merge changes
subprocess.run(["git", "checkout", "master"])
subprocess.run(["git", "merge", "--strategy-option", "theirs", "main"])

# Switch back to the main branch and update local files
subprocess.run(["git", "checkout", "main", "--", "."])
