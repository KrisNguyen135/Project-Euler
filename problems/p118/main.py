from math import sqrt
from copy import copy

def is_pan(string):
    for digit in string:
        if digit == '0': return False
        if string.count(digit) > 1: return False
    return True

def get_pan_primes(limit):
    sieve = [True] * limit
    new_limit = int(sqrt(limit)) + 1
    for i in range(2, new_limit):
        if sieve[i]:
            for j in range(i * 2, limit, i):
                sieve[j] = False
    return [i for i in range(2, limit) if sieve[i] and is_pan(str(i))]

limit = 98765432
#limit = 200
pan_primes = get_pan_primes(limit)
print('Finish getting primes.')

potential_sets = {}
result_sets = []

for prime in pan_primes:
    sets_to_add = {}
    points_to_remove = []
    for current_point in potential_sets:
        helper_point = current_point + str(prime)
        if len(helper_point) > 9: points_to_remove.append(current_point)
        elif is_pan(helper_point):
            helper_set = copy(potential_sets[current_point])
            helper_set.append(prime)
            if len(helper_point) == 9: result_sets.append(helper_set)
            else: sets_to_add[helper_point] = helper_set
    for current_point in points_to_remove:
        potential_sets.pop(current_point)
    for current_point in sets_to_add:
        potential_sets[current_point] = sets_to_add[current_point]
    potential_sets[str(prime)] = [prime]

#print(result_sets)
print('Done')
print(len(result_sets))
