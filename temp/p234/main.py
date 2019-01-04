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


def generate_semidivisibles(prime_input='primes.txt'):
    global running_sum

    def n_divisibles(lower, upper, p):
        '''real_lower = lower // p * p
        real_upper = upper // p * p

        return (real_upper - real_lower) / p'''

        refactored_lower = lower // p
        refactored_upper = upper // p if upper % p else (upper - 1) // p

        print(f'{lower}-{upper}-{p}:{refactored_upper - refactored_lower}')
        return refactored_upper - refactored_lower

    def thread_worker():
        global running_sum

        while True:
            task = task_queue.get()
            if task is None:
                break

            p1, p2 = task
            p1_squared = p1 ** 2
            p2_squared = p2 ** 2

            n_p1_divisibles = n_divisibles(p1_squared, p2_squared, p1)
            n_p2_divisibles = n_divisibles(p1_squared, p2_squared, p2)
            n_p1_p2_divisibles = n_divisibles(p1_squared, p2_squared, p1 * p2)
            n_semindivisibles = n_p1_divisibles + n_p2_divisibles\
                                - 2 * n_p1_p2_divisibles

            print(f'{n_semindivisibles} semidivisibles between {p1} and {p2}')
            running_sum += n_semindivisibles

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

    # test execution
    upper_limit = 15
    #generate_primes_under(int(sqrt(upper_limit)) + 1, output='test_primes.txt')
    generate_semidivisibles(prime_input='test_primes.txt')

    # real execution
    '''upper_limit = 999966663333
    generate_primes_under(int(sqrt(upper_limit)) + 1)'''