with open("input/1.txt") as f:
    input = [x.strip() for x in f.readlines()]

# max = 0
# subtotal = 0

# for item in input:
#     if item == '':
#         if subtotal > max:
#             max = subtotal
#         subtotal = 0
#     else:
#         subtotal += int(item)

# print(max)

max = []
subtotal = 0

for item in input:
    if item == '':
        max.append(subtotal)
        subtotal = 0
    else:
        subtotal += int(item)

max = sorted(max, reverse=True)
print(max[0] + max[1] + max[2])