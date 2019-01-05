from math import sqrt
from threading import Thread
from queue import Queue


def generate_primes_under(limit, output='primes.txt'):
    sieve = [True for _ in range(limit)]

    sub_limit = int(sqrt(limit)) + 1

    with open(output, 'w') as f:
        for i in range(2, sub_limit):
            if sieve[i]:
                f.write(str(i) + '\n')

                for j in range(2 * i, limit, i):
                    sieve[j] = False

        for i in range(sub_limit // 2 * 2, limit):
            if sieve[i]:
                f.write(str(i) + '\n')


def solve(limit, prime_input='primes.txt'):
    global running_sum

    def sum_divisibles(lower, upper, p):
        if lower >= limit:
            return 0

        refactored_lower = lower // p

        if upper > limit:
            upper = limit

        refactored_upper = upper // p if upper % p else (upper - 1) // p

        divisible_sum = p * (refactored_upper * (refactored_upper + 1)
                        - refactored_lower * (refactored_lower + 1)) // 2

        #print(f'{lower}-{upper}|{p}:{divisible_sum}')
        return divisible_sum


    def thread_worker():
        global running_sum

        while True:
            task = task_queue.get()
            if task is None:
                break

            p1, p2 = task
            p1_squared = p1 ** 2
            p2_squared = p2 ** 2

            p1_divisible_sum = sum_divisibles(p1_squared, p2_squared, p1)
            p2_divisible_sum = sum_divisibles(p1_squared, p2_squared, p2)
            p1_p2_divisible_sum = sum_divisibles(
                p1_squared, p2_squared, p1 * p2
            )
            semidivisible_sum = p1_divisible_sum + p2_divisible_sum\
                                - 2 * p1_p2_divisible_sum

            running_sum += semidivisible_sum

            task_queue.task_done()

    # reading in and cleaning saved prime numbers
    with open(prime_input, 'r') as f:
        lines = f.readlines()
    primes = list(map(lambda x: int(x[: -1]), lines))

    # setting up threading variables
    task_queue = Queue()
    threads = []
    n_threads = 4
    for i in range(n_threads):
        t = Thread(target=thread_worker)
        t.start()
        threads.append(t)

    # adding prime pairs to task queue
    for i in range(len(primes) - 1):
        task_queue.put((primes[i], primes[i + 1]))

    # blocking until all tasks are done
    task_queue.join()

    # poison-pill and stopping all threads
    for i in range(n_threads):
        task_queue.put(None)
    for t in threads:
        t.join()

    print('Final result:', running_sum)


if __name__ == '__main__':
    running_sum = 0

    # test 1
    '''upper_limit = 15
    prime_limit = 6
    generate_primes_under(prime_limit, output='test_primes.txt')
    solve(upper_limit, prime_input='test_primes.txt')'''

    # test 2
    '''upper_limit = 1001
    prime_limit = 38
    generate_primes_under(prime_limit, output='test_primes.txt')
    solve(upper_limit, prime_input='test_primes.txt')'''

    # real execution
    upper_limit = 999966663334
    prime_limit = 1000004
    generate_primes_under(prime_limit)
    solve(upper_limit)