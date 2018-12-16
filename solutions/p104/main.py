from math import log10

tailcut = 10 ** 9

def isPandigital(num):
    string = str(num)
    return len(string) == 9 and all([str(i) in string for i in range(1, 10)])

fn1 = 1
fn2 = 1

i = 2
while True:
    i += 1
    fn = (fn1 + fn2) % tailcut
    fn2, fn1 = fn1, fn

    if isPandigital(fn):
        t = i * 0.20898764024997873 - 0.3494850021680094
        if isPandigital(int(10 ** (t - int(t) + 8))): break
print(i)
