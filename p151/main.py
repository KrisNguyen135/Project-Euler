from random import randint

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

test_num = 10 ** 8
approximation = sum(simulate() for i in range(test_num)) / test_num
print(approximation)
