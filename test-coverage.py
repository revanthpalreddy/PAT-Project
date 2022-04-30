#!/usr/bin/env python3

import os
os.system('pip install -r numpy-git/doc_requirements.txt -r numpy-git/linter_requirements.txt -r numpy-git/release_requirements.txt -r numpy-git/test_requirements.txt');
os.system('coverage run --branch numpy-git/runtests.py');
os.system('coverage json --pretty-print -o json-coverage/coverage.json ');
os.system('coverage html -d html-coverage');
