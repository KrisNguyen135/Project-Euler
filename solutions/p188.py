if __name__ == '__main__':
    target = 1855
    temp_result = 1777

    for i in range(2, target + 1):
        print('Looping:', i)
        temp_result = pow(1777, temp_result % 1250000, 100000000)

    print('Final result:', temp_result)

    print('Finished.')
