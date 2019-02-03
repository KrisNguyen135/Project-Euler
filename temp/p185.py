# Standard libraries
from itertools import combinations
from copy import deepcopy


# length of the string in question
#LENGTH = 5
LENGTH = 16

# guess -> number of correct spots
'''GUESSES = {
    '90342': 2,
    '70794': 0,
    '39458': 2,
    '34109': 1,
    '51545': 2,
    '12531': 1
}'''

GUESSES = {
    '5616185650518293': 2,
    '3847439647293047': 1,
    '5855462940810587': 3,
    '9742855507068353': 3,
    '4296849643607543': 3,
    '3174248439465858': 1,
    '4513559094146117': 2,
    '7890971548908067': 3,
    '8157356344118483': 1,
    '2615250744386899': 2,
    '8690095851526254': 3,
    '6375711915077050': 1,
    '6913859173121360': 1,
    '6442889055042768': 2,
    '2321386104303845': 0,
    '2326509471271448': 2,
    '5251583379644322': 2,
    '1748270476758276': 3,
    '4895722652190306': 1,
    '3041631117224635': 3,
    '1841236454324589': 3,
    '2659862637316867': 2
}


def recur_solve(temp_sols, remain_guesses):
    """
    `temp_sols` is a list of tuples `(temporary solution string, invalids)`,
    where `invalids` is a list of sets of numbers that cannot be in the
    locations that correspond to their respective indices.
    `remain_guesses` is a list of tuples `(guess, number of correct spots)`.
    Pop the next item in `remain_guesses`, filter out incorrect solutions in
    `temp_sols`, generate the adjusted `temp_sols`, and call `recur_find`.
    """
    '''print('`recur_find()` called...')
    print('Current solutions:')
    print(temp_sols)
    print('Remaining guesses:')
    print(remain_guesses)'''
    print(len(remain_guesses))

    # return -1 if there are no solutions
    if len(temp_sols) == 0:
        return -1

    # return all solutions if there are any remaining guesses
    if len(remain_guesses) == 0:
        return temp_sols

    guess, n_corrects = remain_guesses[0]
    next_sols = []

    # generate all possible combinations of indices of the correct guesses
    for indices in combinations(range(LENGTH), n_corrects):
        # filter and adjust all temporary solutions
        for sol in temp_sols:
            sol_string, invalids = deepcopy(sol)
            correct = True

            for i in range(LENGTH):
                # case of the index of a correct guess
                if i in indices:
                    if sol_string[i] == 'x' and guess[i] not in invalids[i]:
                        sol_string = sol_string[:i] + guess[i] \
                                     + sol_string[i+1:]
                        invalids[i] = None
                    elif sol_string[i] == guess[i]:
                        pass
                    else:
                        correct = False
                        break
                # case of the index of an incorrect guess
                else:
                    if sol_string[i] == 'x':
                        invalids[i].add(guess[i])
                    elif sol_string[i] == guess[i]:
                        correct = False
                        break

            if correct:
                next_sols.append((sol_string, invalids))

    return recur_solve(next_sols, remain_guesses[1:])


def solve(start_sols, guesses):
    temp_sols = start_sols
    
    while len(guesses) > 0:
        guess, n_corrects = guesses[0]
        next_sols = []

        # generate all possible combinations of indices of the correct guesses
        for indices in combinations(range(LENGTH), n_corrects):
            # filter and adjust all temporary solutions
            for sol in temp_sols:
                sol_string, invalids = deepcopy(sol)
                correct = True

                for i in range(LENGTH):
                    # case of the index of a correct guess
                    if i in indices:
                        if sol_string[i] == 'x' and guess[i] not in invalids[i]:
                            sol_string = sol_string[:i] + guess[i] \
                                         + sol_string[i + 1:]
                            invalids[i] = None
                        elif sol_string[i] == guess[i]:
                            pass
                        else:
                            correct = False
                            break
                    # case of the index of an incorrect guess
                    else:
                        if sol_string[i] == 'x':
                            invalids[i].add(guess[i])
                        elif sol_string[i] == guess[i]:
                            correct = False
                            break

                if correct:
                    next_sols.append((sol_string, invalids))

        temp_sols = next_sols


if __name__ == '__main__':
    # generate the correct data structures for the list of guesses
    guesses = [(guess, n_corrects) for guess, n_corrects in GUESSES.items()]
    # sort guesses by the number of correct spots
    guesses.sort(key=lambda x: x[1])

    #recur_solve([('x' * LENGTH, [set() for _ in range(LENGTH)])], guesses)
    solve([('x' * LENGTH, [set() for _ in range(LENGTH)])], guesses)
