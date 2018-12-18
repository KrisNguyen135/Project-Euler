import numpy as np
#import matplotlib.pyplot as plt

def riffle_shuffle(deck, n):
    print('Riffle-shuffling on:')
    print(deck)

    left = deck[: n // 2]
    right = deck[n // 2 :]
    inter = np.ravel(np.column_stack((left, right)))

    print('Left-half:')
    print(left)
    print('Right-half:')
    print(right)
    print('Resulting interleaved deck:')
    print(inter)

    print('Distance between 1 and 2:')
    print(np.where(inter == 2)[0])

    print('-' * 50)

    return inter

def s(n):
    def get_next_second_element(temp, n):
        if temp % 2 == 0:
            return (temp + n) // 2

        return (1 + temp) // 2

    count = 0
    second_element = 2
    while True:
        second_element = get_next_second_element(second_element, n)
        count += 1
        if second_element == 2:
            break

    return count

if __name__ == '__main__':
    #n = 86 # n is an even integer

    '''deck = np.arange(1, n + 1)
    for i in range(8):
        deck = riffle_shuffle(deck, n)'''

    #print(s(n))

    xs = []
    ys = []
    for i in range(2, 131, 2):
        xs.append(i)
        ys.append(s(i))
        print(f'{xs[-1]}: {ys[-1]}')

    #plt.plot(xs, ys)
    #plt.show()

    xs = np.array(xs)
    ys = np.array(ys)

    print(xs[ys == 60])
