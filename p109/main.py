S = [i for i in range(1, 21)] + [25]
D = [i for i in range(1, 21)] + [25]
T = [i for i in range(1, 21)]

possible_points = [item for item in S] # single points
possible_points += [item * 2 for item in D] # double points
possible_points += [item * 3 for item in T] # triple points

result = 21 # number of possible checkouts in 1 turn

for item in D:
    temp_score = item * 2
    for index1 in range(len(possible_points)):
        if temp_score + possible_points[index1] < 100:
            result += 1 # increment if checkout in 2 turns satisfies
            for index2 in range(index1, len(possible_points)):
                if temp_score + possible_points[index1] + possible_points[index2] < 100: result += 1 # increment if checkout in 3 turns satisfies

print(result)
