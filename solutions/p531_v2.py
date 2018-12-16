import sys

class ExtendedGCD():
    def solve(a, b):
        x, y = 0, 1
        last_x, last_y = 1, 0
        while b != 0:
            q, r = divmod(a, b)
            a, b = b, r
            x, last_x = last_x - q * x, x
            y, last_y = last_y - q * y, y
        return last_x, last_y

# Solve x = a_i (mod n_i) where n_i are coprime.
class ChineseRemainderTheorem():
    def solve(equations):
        a, m = equations[0]
        for i in range(1, len(equations)):
            b, n = equations[i]
            q = m * n
            x, y = ExtendedGCD.solve(m, n)
            root = (a + (b - a) * x * m) % q
            a, m = root, q
        return a

# Solve ax = 1 (mod m).
class ModInverse():
    def solve(a, m):
        x, y = ExtendedGCD.solve(a, m)
        return x % m

class Factorization():
    def __init__(self, n):
        self.values = self.__init_values(n)
        self.phi_values = self.__init_phi_values(n)

    def __init_values(self, n):
        values = [{} for _ in range(n)]
        visited = [False for _ in range(n)]
        for i in range(2, n):
            print('Factorizing values:', i)
            if visited[i]:
                continue
            for j in range(i, n, i):
                visited[j] = True
                values[j][i] = 1
            d = i**2
            while d <= n:
                for j in range(d, n, d):
                    values[j][i] += 1
                d *= i
        return values

    def __init_phi_values(self, n):
        values = [{} for _ in range(n)]
        for i in range(2, n):
            print('Factorizing phi:', i)
            d = 1
            i_factorization = self.get(i)
            for prime in i_factorization:
                e = i_factorization[prime]
                if e > 1:
                    values[i][prime] = e - 1
                d *= (prime - 1)

            d_factorization = self.get(d)
            for prime in d_factorization:
                e = d_factorization[prime]
                if prime not in values[i]:
                    values[i][prime] = 0
                values[i][prime] += e
        return values

    def get(self, n):
        return self.values[n]

    def get_phi(self, n):
        return self.phi_values[n]

    def flatten(self, factorization):
        result = 1
        for prime in factorization:
            e = factorization[prime]
            result *= prime**e
        return result

class Problem():
    def __init__(self):
        self.factorization = Factorization(1005000)

    def solve(self):
        result = 0
        for n in range(1000000, 1005000):
            for m in range(n + 1, 1005000):
                print('Solving:', n, m)
                x = self.f(n, m)
                result += x
        print(result)

    def f(self, n, m):
        return self.g(self.__get_phi(n), n, self.__get_phi(m), m)

    def g(self, a, n, b, m):
        equations = self.__normalize_equations(a, n, b, m)
        if equations:
            return ChineseRemainderTheorem.solve(equations)
        else:
            return 0

    def __normalize_equations(self, a, n, b, m):
        n_factorization = self.__factorize(n)
        m_factorization = self.__factorize(m)

        equations = {}
        for prime in n_factorization:
            e = n_factorization[prime]
            d = prime**e
            value = a % d
            equations[prime] = (value, d)
        for prime in m_factorization:
            e = m_factorization[prime]
            d = prime**e
            value = b % d
            if prime in equations:
                prev_value, prev_d = equations[prime]
                if prev_d == d:
                    if prev_value != value:
                        return None
                elif prev_d > d:
                    if prev_value % d != value:
                        return None
                else:
                    if prev_value != value % prev_d:
                        return None
                    else:
                        equations[prime] = (value, d)
            else:
                equations[prime] = (value, d)
        return [equations[prime] for prime in equations]

    def __factorize(self, n):
        return self.factorization.get(n)

    def __get_phi(self, n):
        return self.factorization.flatten(self.factorization.get_phi(n))

def main():
    problem = Problem()
    problem.solve()

main()
