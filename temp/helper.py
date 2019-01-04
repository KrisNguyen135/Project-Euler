from math import sqrt


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


def multithreading_processing():
    var = None

    def thread_worker():
        global var

        while True:
            x = task_queue.get()
            if x is None:
                break

            # processing task
            # interacting with `var`

            task_queue.task_done()

    # setting up necessary variables

    # setting up multithreading things
    task_queue = queue.Queue()
    threads = []
    n_threads = 4
    for i in range(n_threads):
        t = threading.Thread(target=thread_worker)
        t.start()
        threads.append(t)

    # adding tasks in the task queue

    # blocking until all tasks are done
    task_queue.join()

    # poison-pill and stopping all threads
    for i in range(n_threads):
        task_queue.put(None)
    for t in threads:
        t.join()

    # processing `var` to get the final result