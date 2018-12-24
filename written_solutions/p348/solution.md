# Project Euler problem 348:<br><br><i>Sum of a square and a cube</i>

Link to the original problem: [https://projecteuler.net/problem=348](https://projecteuler.net/problem=348)

## Approach

I used a straightforward (and somewhat of a brute-force) approach: generate all palindromes in an ascending order and check to see each of them can be expressed in 4 different ways as a sum of a cube and a square.

### Generating increasing palindromes

Here is when Python generators come in extremely handy. A big difference between generators and other iterables in Python is that generators generate and return their elements lazily. This gives generating functions in Python a significant advantage in speed.

```
def generate_palindromes(n_digits):
    half_n_digits = n_digits // 2

    if n_digits % 2 == 0:
        for i in range(10 ** (half_n_digits - 1), 10 ** half_n_digits):
            string_i = str(i)
            yield int(string_i + string_i[:: -1])

    else:
        for i in range(10 ** (half_n_digits - 1), 10 ** half_n_digits):
            string_i = str(i)
            for j in range(10):
                yield int(string_i + str(j) + string_i[:: -1])
```

### Checking if a palindrome satisfies the given condition

We simply loop through all the possible candidates for the cube (since its root has a tighter constraint than the square root) and see if the difference between the palindrome and the cube is a square or not. We also stop the function and return `False` if the count exceeds 4.

```
def check_sum(palindrome):
    count = 0
    limit = int(palindrome ** (1 / 3)) + 1

    for i in range(2, limit):
        j_squared = palindrome - (i ** 3)
        if j_squared == (int(sqrt(j_squared)) ** 2):
            #print(f'Found a valid combination for {palindrome}: {i}^3 and {j_squared}.')
            count += 1
            if count > 4:
                print(f'{palindrome} has more than 4 valid combinations.')
                break

    return count == 4
```

### Application of concurrency

If you know me, you know I like applying concurrency while solving Project Euler problems. Here I have 4 separate threads running at the same time to check the generated palindromes to save some execution time. Note that for number-crunching, heavy-processing tasks such as this one, it is better to use multiprocessing as opposed to threading. I personally already had the boilerplate code for threading so I simply slapped that into this program and ran it. The program took less than a minute so I didn't mind too much.

```
def solve(n_targets):
    global running_count
    global running_sum

    def process_worker():
        global running_count
        global running_sum

        while True:
            n_digits = task_queue.get()
            if n_digits is None:
                break

            #print(f'Starting process {n_digits}-digit numbers in {threading.current_thread()}...')

            for palindrome in generate_palindromes(n_digits):
                if check_sum(palindrome):
                    print(f'Found valid palindrome: {palindrome}.')
                    running_count += 1
                    if running_count == n_targets:
                        print('Count reached target.')
                        #return
                    running_sum += palindrome

            task_queue.task_done()


    task_queue = queue.Queue()
    threads = []
    n_threads = 4
    for i in range(n_threads):
        t = threading.Thread(target=process_worker)
        t.start()
        threads.append(t)

    for i in range(2, 10):
        task_queue.put(i)

    task_queue.join()

    for i in range(n_threads):
        task_queue.put(None)
    for t in threads:
        t.join()

if __name__ == '__main__':
    #print(check_sum(4224))

    running_count = 0
    running_sum = 0

    solve(5)

    print('Final count:', running_count)
    print('Final sum:', running_sum)

```

## Conclusion

This is a fairly straightforward problem and I was able to get to the correct answer quite quickly via concurrency. I'd be interested to find out if there are better solutions to this problem.
