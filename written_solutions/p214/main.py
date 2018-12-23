#from math import sqrt
import threading, queue
import pandas as pd

def generate_primes_under(limit, output='primes.txt'):
    sieve = [True for i in range(limit)]

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

def generate_factorizations(input='primes.txt', output='factorizations.txt'):
    with open(input, 'r') as f:
        input_lines = f.readlines()

    primes = list(map(lambda x: int(x[: -1]), input_lines))

    limit = primes[-1] + 1
    sieve = ['' for i in range(limit)]

    for prime in primes:
        for i in range(prime, limit, prime):
            sieve[i] += str(prime) + ','

    with open(output, 'w') as f:
        f.write('1\n')
        for i in range(2, limit):
            f.write(sieve[i][: -1] + '\n')

def generate_totients(factorization_input='factorizations.txt',
    prime_input='primes.txt', output='totients.txt'):

    def thread_worker():
        while True:
            x = task_queue.get()
            if x is None:
                break

            if sieve[x] is None:
                #print(f'Processing {x} in {threading.current_thread()}:{input_lines[x][: -1]}...')

                string_factors = factorization_input_lines[x][: -1].split(',')
                totient = x
                for string_factor in string_factors:
                    factor = int(string_factor)
                    totient *= (factor - 1)
                    totient //= factor

                sieve[x] = totient
                task_queue.put(totient)

            task_queue.task_done()


    print('Reading in input file...')
    with open(factorization_input, 'r') as f:
        factorization_input_lines = f.readlines()

    factorization_input_lines = [''] + factorization_input_lines
    limit = len(factorization_input_lines)

    print('Creating sieve...')
    sieve = [None for i in range(limit)]
    sieve[1] = 1

    # setting up the task queue and running threads
    task_queue = queue.Queue()
    threads = []
    n_threads = 4
    for i in range(n_threads):
        thread = threading.Thread(target=thread_worker)
        thread.start()
        threads.append(thread)

    # starting the thread execution by adding to the task queue
    print('Starting threads...')
    with open(prime_input, 'r') as f:
        prime_input_lines = f.readlines()

    primes = list(map(lambda x: int(x[: -1]), prime_input_lines))
    for prime in primes:
        task_queue.put(prime)

    # waiting until all tasks are done
    task_queue.join()

    for i in range(n_threads):
        task_queue.put(None)
    for thread in threads:
        thread.join()

    print('Writing to files...')
    with open(output, 'w') as f:
        for i in range(limit):
            if sieve[i] is not None:
                f.write(str(i) + ',' + str(sieve[i]) + '\n')

def solve(totient_input='totients.txt', prime_input='primes.txt',
    target_length=25):

    global running_sum

    def thread_worker():
        global running_sum

        def check_length(x, target_length):
            i = x
            running_length = 1
            while i != 1 and running_length <= target_length:
                i = df.loc[i]['totient']
                running_length += 1

            return i == 1 and running_length == target_length


        while True:
            prime = task_queue.get()
            if prime is None:
                break

            print(f'Processing {prime}...')
            if check_length(prime, target_length):
                running_sum += prime

            task_queue.task_done()


    print('Reading in totient input...')
    df = pd.read_csv(totient_input, header=None, names=['x', 'totient'])
    df = df.set_index('x')

    print('Reading in prime input...')
    with open(prime_input, 'r') as f:
        prime_input_lines = f.readlines()
    primes = list(map(lambda x: int(x[: -1]), prime_input_lines))


    task_queue = queue.Queue()
    threads = []
    n_threads = 4
    for i in range(n_threads):
        thread = threading.Thread(target=thread_worker)
        thread.start()
        threads.append(thread)

    print('Starting threads...')
    for prime in primes:
        task_queue.put(prime)

    task_queue.join()

    for i in range(n_threads):
        task_queue.put(None)
    for thread in threads:
        thread.join()
        

if __name__ == '__main__':
    running_sum = 0

    #generate_primes_under(40000000)

    #generate_factorizations(input='test_primes.txt',
    #    output='test_factorizations.txt')
    #generate_factorizations()

    #generate_totients(factorization_input='test_factorizations.txt',
    #    prime_input='test_primes.txt', output='test_totients.txt')
    #generate_totients()

    #solve(totient_input='test_totients.txt', prime_input='test_primes.txt',
    #    target_length=4)
    solve()

    print('Final result:', running_sum)

    print('Finished.')
