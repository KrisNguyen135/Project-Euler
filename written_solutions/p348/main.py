from math import sqrt
import threading, queue

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
