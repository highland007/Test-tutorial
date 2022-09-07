# Test file handling

import json

f = open("test_file.txt", "r")
fw = open("test_file", "w")
fj = open("test_file.json", "w")


# TEST f
# data = f.readline()
# print(data, end="")
# data = f.readline()
# print(data, end="")

# for line in f:
#     print(line, end='')

# print(list(f))
# print(f.readlines())

f.closed
f.close()
f.closed

# TEST fw
for i in range(0,100):
    fw.write(f"Test write {i} \n")

fw.close()


# TEST json
x = [1, 'simple', 'list', 3.14]
json.dump(x, fj)

fj.close()
