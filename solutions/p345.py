import numpy as np
from scipy.optimize import linear_sum_assignment


def main():
    my_file = open("p345.txt", "r")
    lines = my_file.read().split("\n")
    lines.pop()
    my_file.close()

    matrix = [list(map(int, line.split())) for line in lines]
    cost_matrix = np.array(matrix)

    upper_bound = cost_matrix.max()
    cost_matrix = upper_bound - cost_matrix

    row_ind, col_ind = linear_sum_assignment(cost_matrix)
    temp_sum = cost_matrix[row_ind, col_ind].sum()
    print(upper_bound * 15 - temp_sum)


if __name__ == "__main__":
    main()
