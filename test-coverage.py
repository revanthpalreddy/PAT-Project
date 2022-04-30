#!/usr/bin/env python3

import os
os.system('pip install gitpython')
from git import Repo
from git import rmtree

Repo.clone_from('https://github.com/numpy/numpy.git', 'numpy-public-git')
os.system('pip install -r numpy-public-git/doc_requirements.txt -r numpy-public-git/linter_requirements.txt -r numpy-public-git/release_requirements.txt -r numpy-public-git/test_requirements.txt');
os.system('coverage run --branch numpy-public-git/runtests.py');
os.system('coverage json --pretty-print -o json-coverage/coverage.json ');
os.system('coverage html -d html-coverage');
rmtree('numpy-public-git')
