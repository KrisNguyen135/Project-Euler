import networkx as nx

fileName = 'p083_matrix.txt'
maxtrix = [list(map(int, line.split(','))) for line in open(fileName).readlines()]
rowNum, columnNum = len(maxtrix), len(maxtrix[0])

G = nx.DiGraph()
for row in range(rowNum):
    for column in range(columnNum):
        neighbors = [(row + x, column + y) for x, y in [(-1, 0), (0, -1), (1, 0), (0, 1)]
            if 0 <= row + x < rowNum and 0 <= column + y < columnNum]
        for ix, jy in neighbors:
            G.add_edge((row, column), (ix, jy), weight=maxtrix[ix][jy])

path_length = nx.dijkstra_path_length(G, source=(0, 0), target=(rowNum - 1,columnNum - 1))
print(maxtrix[0][0] + path_length)
