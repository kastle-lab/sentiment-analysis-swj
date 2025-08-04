import random

members = ['anmol', 'chris','michael','alexis', 'jon wasky'] 
reviewRanges = ['1 - 20',' 21 - 40', '41 - 60', '61 - 80', '81 - 100']
assignments = {}

random.shuffle(members)

for i in range(min(len(members), len(reviewRanges))):
    idx = random.randrange(len(reviewRanges))
    reviewRange = reviewRanges.pop(idx)
    member = members[i]
    assignments[member] = reviewRange

for key, value in assignments.items():
    print(f"{key} : {value}")