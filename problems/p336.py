def reverse_str(string):
    return string[: : -1]

def generate_maximix(length):
    init_str = 'ABCDEFGHIJK'[: length]

    current_list = [init_str[: -2] + reverse_str(init_str[-2:])]

    '''for target_char in reversed(init_str[: -2]):
        temp_result = []

        for string in current_list:'''

    for pos in reversed(range(length - 2)):
        print('Going through', init_str[pos])
        temp_result = []

        for string in current_list:
            reversed_str = string[: pos] + reverse_str(string[pos:])

            for reverse_pos in range(pos + 1, length - 1):
                temp_result.append(reversed_str[: reverse_pos] + reverse_str(reversed_str[reverse_pos:]))

        current_list = temp_result

    return current_list

def main():
    length = 11
    target = 2011

    arr_list = generate_maximix(length)
    print('Sorting the list...')
    arr_list.sort()
    #print(arr_list)
    print(arr_list[target - 1])


main()
