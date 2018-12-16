from math import sqrt
from random import randrange
from copy import deepcopy

def compute_time(ys):
    result = sum(sqrt((ys[i + 1] - ys[i] + 10 * sqrt(2)) ** 2 + (ys[i + 1] - ys[i]) ** 2) / (9 - i) for i in range(len(ys) - 1))
    result += (sqrt((ys[0] - 25 * sqrt(2) + 50) ** 2 + ys[0] ** 2) + sqrt((ys[-1] + 25 * sqrt(2) - 50) ** 2 + ys[-1] ** 2)) / 10

    return result

def left_to_right_adjust(ys):
    def individual_run(index, ys):
        temp_best_time = compute_time(ys)
        increment_step = 1

        up_ys = deepcopy(ys); up_ys[index] += 1
        up_time = compute_time(up_ys)
        down_ys = deepcopy(ys); down_ys[index] -= 1
        down_time = compute_time(down_ys)

        if up_time < down_time: change_direction = 1
        else: change_direction = -1

        ys[index] += change_direction * increment_step
        temp_time = compute_time(ys)

        while temp_time != temp_best_time:
            while temp_time < temp_best_time:
                temp_best_time = temp_time
                ys[index] += change_direction * increment_step
                temp_time = compute_time(ys)

            ys[index] -= change_direction * increment_step
            increment_step /= 10
            ys[index] += change_direction * increment_step
            temp_time = compute_time(ys)

        return ys

    def complete_run(ys):
        temp_best_time = compute_time(ys)

        for index in range(len(ys)): ys = individual_run(index, ys)
        temp_time = compute_time(ys)

        while temp_time < temp_best_time:
            temp_best_time = temp_time
            for index in range(len(ys)): ys = individual_run(index, ys)
            temp_time = compute_time(ys)
            print(ys)
            print(temp_time)

        return ys

    return complete_run(ys)

def custom_gradient_descent(ys, learning_rate=0.01):
    def get_gradient(ys, i):
        if i == 0:
            denominator1 = sqrt((ys[0] - 25 * sqrt(2) + 50) ** 2 + ys[0] ** 2)
            denominator2 = sqrt((ys[1] - ys[0] + 10 * sqrt(2)) ** 2 + (ys[1] - ys[0]) ** 2)

            return (4 * ys[0] + 100 - 50 * sqrt(2)) / (10 * denominator1) + (4 * ys[0] - 4 * ys[1] - 20 * sqrt(2)) / (9 * denominator2)

        if i == 5:
            denominator1 = sqrt((ys[5] - ys[4] + 10 * sqrt(2)) ** 2 + (ys[5] - ys[4]) ** 2)
            denominator2 = sqrt((ys[5] + 25 * sqrt(2) - 50) ** 2 + ys[5] ** 2)

            return (4 * ys[5] - 4 * ys[4] + 20 * sqrt(2)) / (5 * denominator1) + (4 * ys[5] + 50 * sqrt(2) - 100) / (10 * denominator2)

        denominator1 = sqrt((ys[i] - ys[i - 1] + 10 * sqrt(2)) ** 2 + (ys[i] - ys[i - 1]) ** 2)
        denominator2 = sqrt((ys[i + 1] - ys[i] + 10 * sqrt(2)) ** 2 + (ys[i + 1] - ys[i]) ** 2)

        return (4 * ys[i] - 4 * ys[i - 1] + 20 * sqrt(2)) / ((9 - i + 1) * denominator1) + (4 * ys[i] - 4 * ys[i + 1] - 20 * sqrt(2)) / ((9 - i) * denominator2)

    old_time = compute_time(ys)
    print('Updated ys:', ys)
    print('Updated time:', old_time)

    gradient_list = [get_gradient(ys, i) for i in range(len(ys))]
    print('Gradient list:', gradient_list)
    new_ys = [ys[i] - learning_rate * gradient_list[i] for i in range(len(ys))]
    print('Updated ys:', new_ys)
    new_time = compute_time(new_ys)
    print('Updated time:', new_time)

    while new_time <= old_time:
        old_time = new_time
        gradient_list = [get_gradient(new_ys, i) for i in range(len(ys))]
        new_ys = [new_ys[i] - learning_rate * gradient_list[i] for i in range(len(ys))]
        print('Updated ys:', new_ys)
        new_time = compute_time(new_ys)
        print('Updated time:', new_time)


def main():
    #ys = [0, 0, 0, 0, 0, 0]

    ys = [
        25 / sqrt(2),
        15 / sqrt(2),
        5 / sqrt(2),
        - 5 / sqrt(2),
        - 15 / sqrt(2),
        - 25 / sqrt(2)
    ]
    

    #print(compute_time([1.1, 0, 0, 0, 0, 0]))
    #ys = left_to_right_adjust(ys)

    custom_gradient_descent(ys)

    return

if __name__ == "__main__":
    main()
