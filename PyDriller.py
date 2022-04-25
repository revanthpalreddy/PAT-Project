from pydriller import Repository

f = open("data/Analysis.csv", "a")
d = {}
f.write("filepath, author_names, date_added, num_of_contributors, how_often_modified\n")

for commit in Repository(path_to_repo='https://github.com/numpy/numpy').traverse_commits():
    # f.write("-----------------------------------\n")
    # changecount = 0
    # f.write(commit.hash)
    # f.write(commit.msg)

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

for key in d:
    d[key][1] = d[key][1][0]
    f.write('{}, {}, {}, {}, {}\n'.format(key, d[key][0], d[key][1], d[key][2], d[key][3]))