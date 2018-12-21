from random import randint
import multiprocessing
import time

cut_result = {
    8: [4, 2, 1],
    4: [2, 1],
    2: [1],
    1: []
}

def simulate():
    result = -1
    paper_list = [8, 4, 2, 1]
    while paper_list:
        if len(paper_list) == 1:
            result += 1
            paper_list = cut_result[paper_list[0]]
        else:
            paper_index = randint(0, len(paper_list) - 1)
            paper_list += cut_result[paper_list[paper_index]]
            paper_list.pop(paper_index)
    return result

def run_tests(n_tests):
    start = time.time()

    running_apprx = 0
    for i in range(n_tests):
        #print(i)
        running_apprx += simulate()

    print(f'Took {time.time() - start : .2f} seconds')
    print('Final result:', running_apprx / n_tests)

if __name__ == '__main__':
    n_processes = 4
    processes = []
    for i in range(n_processes):
        p = multiprocessing.Process(target=run_tests, args=(10 ** 7,))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    print('Finished')
