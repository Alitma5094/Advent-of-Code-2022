import re

with open("input/5.txt") as f:
    input = [x.strip() for x in f.readlines()]

pattern = r'\d+'
# numbers = re.findall(pattern, "move 3 from 9 to 6")

# 
#                         [Z] [W] [Z]
#         [D] [M]         [L] [P] [G]
#     [S] [N] [R]         [S] [F] [N]
#     [N] [J] [W]     [J] [F] [D] [F]
# [N] [H] [G] [J]     [H] [Q] [H] [P]
# [V] [J] [T] [F] [H] [Z] [R] [L] [M]
# [C] [M] [C] [D] [F] [T] [P] [S] [S]
# [S] [Z] [M] [T] [P] [C] [D] [C] [D]
#  1   2   3   4   5   6   7   8   9 

stacks = [
    ["S", "C", "V", "N"],
    ["Z", "M", "J", "H", "N", "S"],
    ["M", "C", "T", "G", "J", "N", "D"],
    ["T", "D", "F", "J", "W", "R", "M"],
    ["P", "F", "H"],
    ["C", "T", "Z", "H", "J"],
    ["D", "P", "R", "Q", "F", "S", "L", "Z"],
    ["C", "S", "L", "H", "D", "F", "P", "W"],
    ["D", "S", "M", "P", "F", "N", "G", "Z"],
]
data = []
for index in input:
    data.append(re.findall(pattern, index))

for line in data:
    count = int(line[0]) # 3
    start = int(line[1]) # 9
    destination = int(line[2]) # 6
    for i in range(count):
        stacks[destination - 1].append(stacks[start - 1].pop())


for sub_list in stacks:
  print(sub_list[-1])
