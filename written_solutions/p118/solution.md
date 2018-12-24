# Project Euler Problem 118:<br><i>Pandigital prime sets</i>

Link to original problem prompt: [https://projecteuler.net/problem=118](https://projecteuler.net/problem=118)

## Approach

The main strategy is to generate all prime numbers that have unique digits. The we would loop through those primes and try to combine them together to make a set specified in the problem prompt.

### Generating prime numbers with unique digits

I'm sure many people's first approach would be to generate all prime numbers below 100,000,000 using a sieve or something similar. From that set of prime numbers we could loop through it and omit any element that has repeating digits.

Using Python, it wasn't a good method, speed-wise, to make a sieve for 100,000,000 integers and generate the primes from there (a rare "ah-ha" moment for programmer who don't like Python I'm sure). So I tried generating all numbers with unique digits below 100,000,000 first and then check to see if each other them is a prime number or not. This method proved to be faster with Python's `permutations` method. Specifically, say if you pass 'abc' to the method, it will return all permutations of the string of a given length. For example, if the length is 2, the return result will be an iterable containing `('a', 'b')`, `('a', 'c')`, `('b', 'a')`, `('b', 'c')`, `('c', 'a')`, `('c', 'b')`.

However, as indicated above, the method actually returns the permutations as tuples, while we actually want the concatenated strings. So, I rewrote the `permutations` method from the official Python documentation to yield concatenated strings:

```
def custom_permutations(iterable, r):
    pool = iterable
    n = len(pool)

    indices = list(range(n))
    cycles = list(range(n, n - r, -1))
    yield ''.join(pool[i] for i in indices[: r])

    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i :] = indices[i + 1 :] + indices[i : i + 1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield ''.join(pool[i] for i in indices[: r])
                break
        else:
            return
```

We can now can this function with `r` (the length of the permutated strings) ranging from 1 to 9 to generate all numbers with unique digits. Then we can feed each of them to a prime-checking function to obtain the final list of prime numbers with unique digits.

### Reducing to sorted strings and counts

To solve the problem, we now have to match the generated primes to create sets as specified in the problem prompts. Another strategy I found to improve the speed of the program is from the insight that in the sets, for example, `{98765431, 2}` and `{98765413, 2}` that satisfy the conditions of the problem, 98765431 and 98765413 are simply permutations of each other. So we can omit all permutations of those prime numbers and only keep one of them, with the count of the original numbers.

In the end while we count the number of sets that satisfy the conditions of the problem, we will multiple each with the appropriate count:

```
running_result = 0

# looping through all sets satisfying the conditions
for solution in complete_solutions:
    temp_product = 1
    # multiplying with the counts, stored in `df`
    for sorted_prime in solution:
        temp_product *= df.loc[sorted_prime]['count']

    running_result += temp_product
```

### Looping through to generate valid sets

First, we will have two list to keep track of when we loop through the reduced set of primes with unique digits: a list of currently-forming sets, and a list of complete sets. We will check each element in the reduced set of primes with each currently-forming set to see if it can be added in there (if its digits are not included in the set yet), and if a currently-forming set achieves a total of 9 digits, it will be transferred to the list of complete sets:

```
running_solutions = [([], '')] # list of (list of sorted primes, concatenated string)
complete_solutions = [] # list of (list of sorted primes that are complete)

# looping through the reduced set of primes
for sorted_prime in sorted_primes:
    # checking against each currently-forming set
    for solution in running_solutions:
        concat_string = solution[1] + str(sorted_prime)

        if len(concat_string) == len(set(concat_string)):
            new_solution = (solution[0] + [sorted_prime],
                concat_string)

            # adding to the list of complete sets
            if len(concat_string) == 9:
                complete_solutions.append(new_solution[0])
            else:
                running_solutions.append(new_solution)

```

## Conclusion

I had a lot of fun with this problem. The strategy of forming the valid sets was quite interesting to work out. This problem also had me look at the source code for the `itertools.permutations` method of Python.
