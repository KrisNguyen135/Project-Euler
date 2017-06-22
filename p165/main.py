from math import gcd

# class for a cartesian point with (x, y) as coordinates
class Point():
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

    def find_line(self, point):
        if point.x == self.x: return Line(1, 0, -self.x, self, point)

        a = point.y - self.y
        b = self.x - point.x
        c = point.x * self.y - self.x * point.y
        divisor = gcd(gcd(a, b), c)
        return Line(a // divisor, b // divisor, c // divisor, self, point)

# class for a cartesian line with ax+by+c=0 as equation
class Line():
    def __init__(self, a, b, c, end_point1, end_point2):
        self.a, self.b, self.c, self.end_point1, self.end_point2 = a, b, c, end_point1, end_point2

    def __str__(self):
        return '{0} * x + {1} * y + {2} = 0'.format(self.a, self.b, self.c)
        + '. End points: ' + str(self.end_point1) + ', ' + str(strself.end_point2)

    def find_true_intersection(self, line):
        denominator = self.a * line.b - self.b * line.a
        if denominator == 0: return False

        intersection = Point(
            #round((self.b * line.c - self.c * line.b) / denominator, 10),
            (self.b * line.c - self.c * line.b) / denominator,
            #round((self.c * line.a - self.a * line.c) / denominator, 10)
            (self.c * line.a - self.a * line.c) / denominator
        )

        cross_product1 = (intersection.x - self.end_point1.x) * (intersection.x - self.end_point2.x)
        cross_product2 = (intersection.y - line.end_point1.x) * (intersection.y - line.end_point2.x)
        if cross_product1 < 0 and cross_product2 < 0: return intersection
        return False

def generate_numbers(limit):
    s = [0] * (limit + 1)
    t = [0] * (limit + 1)
    s[0] = 290797
    t[0] = 297
    for i in range(limit):
        s[i + 1] = (s[i] * s[i]) % 50515093
        t[i + 1] = s[i + 1] % 500
    return t[1:]

def solve(limit):
    numbers = generate_numbers(limit)
    lines = []
    for pair_index in range(limit // 4):
        point1 = Point(numbers[4 * pair_index], numbers[4 * pair_index + 1])
        point2 = Point(numbers[4 * pair_index + 2], numbers[4 * pair_index + 3])
        lines.append(point1.find_line(point2))
    print('Number of lines:', len(lines))

    intersection_set = set()
    for i in range(len(lines) - 1):
        if i % 100 == 0: print(i, len(lines))
        for j in range(i + 1, len(lines)):
            line1 = lines[i]
            line2 = lines[j]
            intersection = line1.find_true_intersection(line2)
            if intersection: intersection_set.add(intersection)

    return len(intersection_set)

limit = 20000
print(solve(limit))
