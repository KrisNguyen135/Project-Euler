from random import randrange

samples = 1000000

board = [0] * 40
chance = [7, 22, 36]
comm_chest = [2, 17, 33]

current_pos = 0
chance_pos = 0
cc_pos = 0
doubles = 0

def CHANCE():
    global current_pos
    global chance_pos

    my_list = [0, 10, 11, 24, 39, 5]
    chance_pos = (chance_pos + 1) % 16

    if chance_pos < 6:
        current_pos = my_list[chance_pos]
    if chance_pos == 6 or chance_pos == 7:
        if current_pos == 7: current_pos = 15
        if current_pos == 22: current_pos = 25
        if current_pos == 36: current_pos = 5
    if chance_pos == 8:
        if current_pos == 22: current_pos = 28
        else: current_pos = 12
    if chance_pos == 9: current_pos -= 3

def CC():
    global current_pos
    global cc_pos

    my_list = [0, 10]
    cc_pos = (cc_pos + 1) % 16

    if cc_pos < 2: current_pos = my_list[cc_pos]

for i in range(samples):
    dice1 = randrange(4) + 1
    dice2 = randrange(4) + 1

    # check for doubles
    if dice1 == dice2: doubles += 1
    else: doubles = 0

    # go to jail if achieve 3rd double
    if doubles > 2:
        current_pos = 10
        doubles = 0
    else:
        # move to that square
        current_pos = (current_pos + dice1 + dice2) % 40

        # handle chance and community chest
        if current_pos in chance: CHANCE()
        if current_pos in comm_chest: CC()
        # handle G2J
        if current_pos == 30: current_pos = 10

    board[current_pos] += 1

#print(board)
current_max = max(board)
result = str(board.index(current_max))
for i in range(2):
    current_max = max([item for item in board if item < current_max])
    result += str(board.index(current_max))
print(result)
