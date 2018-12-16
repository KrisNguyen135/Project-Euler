from math import sqrt

def square_check(num):
    helper = sqrt(num)
    return helper == int(helper)

def find_first_pairs(limit):
    first_pairs = []
    for r in range(1, limit // 3 + 1):
        q_limit = min(2 * limit // 3 - r, (limit - r) // 2) + 1
        for q in range(r, q_limit):
            helper = r ** 2 + q ** 2 + r * q
            if square_check(helper): first_pairs.append((r, q))
    return first_pairs

def find_triples(first_pairs, limit):
    triples = []
    for r, q in first_pairs:
        for p in range(q, limit + 1 - r - q):
            helper = r ** 2 + p ** 2 + r * p
            if square_check(helper):
                helper = q ** 2 + p ** 2 + q * p
                if square_check(helper): triples.append((r, q, p))
    return triples

limit = 1000
first_pairs = find_first_pairs(limit)
triples = find_triples(first_pairs, limit)
sums = set(map(sum, triples))
print(sum(sums))
