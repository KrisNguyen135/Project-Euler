from math import sqrt
import networkx as nx
import matplotlib.pyplot as plt

def display_graph(graph):
    nodes = graph.nodes()
    print('Number of nodes:', len(nodes))
    print(nodes)

    edges = graph.edges()
    print('Number of edges:', len(edges))
    print(edges)

    nx.draw_networkx(graph)
    plt.show()

def generate_primes_digit_sep(digit_num):
    limit = 10 ** digit_num
    sieve = [True for i in range(limit)]
    sieve[1] = False
    loop_limit = int(sqrt(limit)) + 1

    for i in range(2, loop_limit):
        if sieve[i]:
            for j in range(i * 2, limit, i):
                sieve[j] = False

    digit_sep = []
    for digit in range(1, digit_num + 1):
        digit_sep.append([num for num in range(10 ** (digit - 1), 10 ** digit) if sieve[num]])

    return digit_sep

def generate_potential_1way_connection(prime, con1=True, con2=True):
    con1_result = []
    con2_result = []
    str_prime = str(prime)

    if con1:
        for location in range(len(str_prime)):
            current_digit = int(str_prime[location])
            con1_result += [str_prime[:location] + str(upper_digit) + str_prime[location + 1:] for upper_digit in range(current_digit + 1, 10)]

    if con2:
        con2_result += [str(digit) + str_prime for digit in range(1, 10)]

    return list(map(int, con1_result)), list(map(int, con2_result))

def generate_network(digit_num, primes_digit_sep):
    graph = nx.Graph()
    graph.add_nodes_from(primes_digit_sep[0])

    for i in range(digit_num - 1):
        print("Generating network at %i digit..." %(i))

        current_primes = primes_digit_sep[i]
        next_primes = primes_digit_sep[i + 1]
        graph.add_nodes_from(next_primes)

        for prime in current_primes:
            con1_potential_connections, con2_potential_connections = generate_potential_1way_connection(prime)

            for item in con1_potential_connections:
                if item in current_primes:
                    graph.add_edge(prime, item)

            for item in con2_potential_connections:
                if item in next_primes:
                    graph.add_edge(prime, item)

    current_primes = primes_digit_sep[-1]
    for prime in current_primes:
        con1_potential_connections, _ = generate_potential_1way_connection(prime, con2=False)

        for item in con1_potential_connections:
            if item in current_primes:
                graph.add_edge(prime, item)

    return graph

def process(primes, ref_graph):
    graph = nx.Graph()

    graph.add_node(2)

    result = 0
    for i in range(1, len(primes)):
        current_nodes = graph.nodes()
        current_prime = primes[i]; print("Processing", current_prime)
        graph.add_node(current_prime)

        for current_neighbor in ref_graph.neighbors(current_prime):
            if current_neighbor > current_prime:
                break
            elif current_neighbor in current_nodes:
                graph.add_edge(current_prime, current_neighbor)

        if not nx.has_path(graph, 2, current_prime):
            result += current_prime

    #display_graph(graph)
    return result

def main():
    digit_num = 7
    primes_digit_sep = generate_primes_digit_sep(digit_num); print("Finished generating primes.")

    ref_graph = generate_network(digit_num, primes_digit_sep); print("Finished generating reference graph.")

    primes = []
    for item in primes_digit_sep:
        primes += item

    result = process(primes, ref_graph)

    print("Final result:", result)

main()
