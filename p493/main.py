import numpy as np

results = []

for a1 in range(21):
    for a2 in range(21-a1):
        for a3 in range(21-a1-a2):
            for a4 in range(21-a1-a2-a3):
                for a5 in range(21-a1-a2-a3-a4):
                    for a6 in range(21-a1-a2-a3-a4-a5):
                        results.append([a1, a2, a3, a4, a5, a6, 20-a1-a2-a3-a4-a5-a6])

results = np.array(results)
#print(len(results)
print(results)
temp = sum( sum(subItem > 0 for subItem in item) for item in results)
print(temp)
