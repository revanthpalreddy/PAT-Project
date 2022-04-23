#!/usr/bin/env python3

import os
os.system('pip install -r numpy/doc_requirements.txt -r numpy/linter_requirements.txt -r numpy/release_requirements.txt -r numpy/test_requirements.txt');
os.system('coverage run numpy/runtests.py');
os.system('coverage json --pretty-print -o json-coverage/coverage.json ');
os.system('coverage html -d html-coverage');
