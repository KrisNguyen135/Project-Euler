from math import inf

def read_data():
    def process_text(text):
        if text == '-':
            return inf
        return int(text)

    with open('p107_network.txt', 'r') as f:
    #with open('sample_network.txt', 'r') as f:
        lines = f.read().split('\n')[:-1]

    matrix = []
    for line in lines: matrix.append(list(map(process_text, line.split(','))))

    for i in range(len(matrix)): matrix[i][i] = 0

    return matrix

def primm(matrix):
    def find_next(matrix, finished_node_list, unfinished_node_list):
        temp_best1 = finished_node_list[0]
        temp_best2 = unfinished_node_list[0]

        for node1 in finished_node_list:
            for node2 in unfinished_node_list:
                temp_distance = matrix[node1][node2]
                if temp_distance < matrix[temp_best1][temp_best2]:
                    temp_best1 = node1
                    temp_best2 = node2

        return temp_best1, temp_best2

    finished_node_list = [0]
    unfinished_node_list = [i for i in range(1, len(matrix))]

    adj_matrix = [[0 for i in range(len(matrix))] for j in range(len(matrix))]

    while unfinished_node_list:
        node1, node2 = find_next(matrix, finished_node_list, unfinished_node_list)
        finished_node_list.append(node2)
        unfinished_node_list.remove(node2)
        adj_matrix[node1][node2] = 1
        adj_matrix[node2][node1] = 1

    print('Resulting adjacency matrix:')
    for row in adj_matrix:
        for item in row:
            print(item, end=' ')
        print()

    return adj_matrix

def main():
    matrix = read_data()
    adj_matrix = primm(matrix)

    total_weight_sum = 0
    adjusted_weight_sum = 0
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            if matrix[i][j] < inf:
                total_weight_sum += matrix[i][j]
            if adj_matrix[i][j]:
                adjusted_weight_sum += matrix[i][j]

    print('Total weight sum: %i.' % total_weight_sum)
    print('Adjusted weight sum: %i.' % adjusted_weight_sum)
    print('Saved weight: %i.' % (total_weight_sum - adjusted_weight_sum))

    return

if __name__ == '__main__':
    main()
