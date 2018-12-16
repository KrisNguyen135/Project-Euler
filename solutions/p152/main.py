limit = 80

potential_sums = {}
result_sums = []

for i in reversed(range(2, limit + 1)):
    print(i)

    elements_to_add = {}
    elements_to_pop = []
    for element in potential_sums:
        new_sum = 1 / (i ** 2) + potential_sums[element]
        if new_sum > 0.5: elements_to_pop.append(element)
        else:
            new_element = element + (i,)
            if new_sum == 0.5: result_sums.append(new_element)
            else: elements_to_add[new_element] = new_sum

    for element in elements_to_pop: potential_sums.pop(element)
    for element in elements_to_add: potential_sums[element] = elements_to_add[element]

    potential_sums[(i,)] = 1 / (i ** 2)

print(result_sums)
print(len(result_sums))
