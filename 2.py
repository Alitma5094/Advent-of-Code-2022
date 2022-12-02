with open("input/2.txt") as f:
    input = [x.strip() for x in f.readlines()]



data = []
for i in input:
    data.append(i.split())

totalScore = 0

# for round in data:
#     score = 0
#     if round[1] == "X":
#         score = 1
#     elif round[1] == "Y":
#         score = 2
#     else:
#         score = 3

#     if round[0] == "A":
#         if round[1] == "X":
#             score += 3
#         elif round[1] == "Y":
#             score += 6
#         else:
#             score += 0
    
#     elif round[0] == "B":
#         if round[1] == "X":
#             score += 0
#         elif round[1] == "Y":
#             score += 3
#         else:
#             score += 6
#     else:
#         if round[1] == "X":
#             score += 6
#         elif round[1] == "Y":
#             score += 0
#         else:
#             score += 3
#     totalScore += score

for round in data:
    score = 0

    if round[0] == "A":
        if round[1] == "X":
            # rock - lose (scissors)
            score += 0
            score += 3
        elif round[1] == "Y":
            # rock - draw (rock)
            score += 3
            score += 1
        else:
            # rock - win (paper)
            score += 6
            score += 2
    
    elif round[0] == "B":
        if round[1] == "X":
            # paper - lose (rock)
            score += 0
            score += 1
        elif round[1] == "Y":
            # paper - draw (paper)
            score += 3
            score += 2
        else:
            # paper - win (scissors)
            score += 6
            score += 3

    else:
        if round[1] == "X":
            # scissors - lose (paper)
            score += 0
            score += 2
        elif round[1] == "Y":
            # scissors - draw (scissors)
            score += 3
            score += 3
        else:
            # scissors - win (rock)
            score += 6
            score += 1

    totalScore += score


    
# A X rock
# B Y paper
# C Z scissors

print(totalScore)