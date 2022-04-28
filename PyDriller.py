from pydriller import Repository
import re
import csv
import pandas as pd
from matplotlib import pyplot as plt

# f = open("data/PyDriller.csv", "w")
# f1 = open("data/PyDrillerCommitMessages.csv", "w")



d = {}
commitMessages = {}
authorNames = {}
# f.write("filepath, author_names, date_added, num_of_contributors, how_often_modified\n")
# f1.write("code, number_of_occurences\n")

for commit in Repository(path_to_repo='https://github.com/numpy/numpy').traverse_commits():
    # f.write("-----------------------------------\n")
    # changecount = 0
    # f.write(commit.hash)
    # f.write(commit.msg)

    if commit.author.name not in authorNames:
        authorNames[commit.author.name] = 1
    else:
        authorNames[commit.author.name] += 1

    if bool(re.match('bug', commit.msg, re.I)):
        if 'bug' not in commitMessages:
            commitMessages['bug'] = 1
        else:
            commitMessages['bug'] += 1

    if bool(re.match('enh', commit.msg, re.I)):
        if 'enh' not in commitMessages:
            commitMessages['enh'] = 1
        else:
            commitMessages['enh'] += 1

    if bool(re.match('dev', commit.msg, re.I)):
        if 'dev' not in commitMessages:
            commitMessages['dev'] = 1
        else:
            commitMessages['dev'] += 1

    if bool(re.match('doc', commit.msg, re.I)):
        if 'doc' not in commitMessages:
            commitMessages['doc'] = 1
        else:
            commitMessages['doc'] += 1

    if bool(re.match('maint', commit.msg, re.I)):
        if 'maint' not in commitMessages:
            commitMessages['maint'] = 1
        else:
            commitMessages['maint'] += 1

    if bool(re.match('build', commit.msg, re.I)):
        if 'build' not in commitMessages:
            commitMessages['build'] = 1
        else:
            commitMessages['build'] += 1




    for file in commit.modified_files:
        # changecount += 1
        # if file.new_path is not None:
        #     s = file.new_path.split('/')
        # else:
        #     continue
        # if len(s)>=3:
        #     if s[2]=='tests':
        #         f.write("%s, %s, %s\n" % (commit.author.name, file.new_path, commit.author_date))
        # elif s[0]=='tests':
        # # f.write(s)
        #     f.write("%s, %s, %s\n" % (commit.author.name, file.new_path, commit.author_date))
        # if file.filename.startswith('test'):
        #     f.write("%s, %s, %s\n" % (commit.author.name, file.new_path, commit.author_date))

        if file.filename.startswith('test'):
            if file.new_path not in d:
                d[file.new_path] = [[], [], [], []]

            if commit.author.name not in d[file.new_path][0]:
                d[file.new_path][0].append(commit.author.name)

            if commit.author_date not in d[file.new_path][1]:
                d[file.new_path][1].append(commit.author_date.date().isoformat())

            d[file.new_path][2] = (len(d[file.new_path][0]))
            d[file.new_path][3] = (len(d[file.new_path][1]))


with open('data/PyDriller.csv', 'w') as csv_file:
    # header1 = ['filepath', 'author_names', 'date_added', 'num_of_contributors', 'how_often_modified']
    writer1 = csv.writer(csv_file)
    writer1.writerow(['filepath', 'author_names', 'date_added', 'num_of_contributors', 'how_often_modified'])

    for key in d:
        d[key][1] = d[key][1][0]
        StrListNames = ','.join(str(e) for e in d[key][0])
        # f.write('{}, {}, {}, {}, {}\n'.format(key, StrListNames, d[key][1], d[key][2], d[key][3]))
        writer1.writerow([key, StrListNames, d[key][1], d[key][2], d[key][3]])

with open('data/PyDrillerCommitMessages.csv', 'w') as csv_file:
    writer2 = csv.writer(csv_file)
    writer2.writerow(['code', 'num_of_occurrences'])

    for key1 in commitMessages:
        writer2.writerow([key1, commitMessages[key1]])

with open('data/PyDrillerAuthors.csv', 'w') as csv_file:
    writer3 = csv.writer(csv_file)
    writer3.writerow(['names', 'count'])
    for key2 in authorNames:
        writer3.writerow([key2, authorNames[key2]])








