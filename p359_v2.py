from math import sqrt

def get_closest_tri(x):
    unprocessed_tri = (sqrt(8 * x + 1) - 1) / 2
    floor_tri = int(unprocessed_tri)

    if unprocessed_tri - floor_tri < 0.5:
        tri = floor_tri
    else:
        tri = floor_tri + 1

    return tri * (tri + 1) // 2

def process_head(f):
    return (f ** 2) // 2

def process_first_floor(r):
    return r * (r + 1) // 2

def process(f, r):
    if f == 1:
        return process_first_floor(r)

    if r == 1:
        return process_head(f)

    head_number = (f ** 2) // 2

    if f % 2 == 1:
        head_index = f
    else:
        head_index = f + 1
    head_tri = head_index * (head_index - 1) // 2

    room_index = head_index + r - 1
    room_tri = room_index * (room_index - 1) // 2

    if r % 2 == 1:
        return room_tri + head_number - head_tri
    else:
        return room_tri - head_number + head_tri

def solve():
    limit2 = 28
    limit3 = 13

    running_sum = 0

    '''# handling (1, 71328803586048)
    running_sum += process_first_floor(71328803586048)

    # handling (71328803586048, 1)
    running_sum += process_head(71328803586048)'''

    for power2 in range(limit2):
        for power3 in range(limit3):
            print(power2, power3)

            divisor1 = (2 ** power2) * (3 ** power3)
            divisor2 = 71328803586048 // divisor1

            running_sum += process(divisor1, divisor2)

    print(running_sum % (10 ** 8))

def main():
    '''f = 99
    r = 100
    print(process_head(f))
    print(process_non_head(f, r))'''

    solve()

main()
