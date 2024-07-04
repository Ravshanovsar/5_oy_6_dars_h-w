def gen_fibonacci(stop):
    a1 = 1
    a2 = 0
    s = 0
    while s <= stop:
        yield a2
        s = a1 + a2
        a1 = a2
        a2 = s

gen = gen_fibonacci(20)
lof = iter(gen)
for i in lof:
    print(i)