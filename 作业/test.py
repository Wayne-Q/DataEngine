def frange(start, end, step):
    x = start
    while x<end:
        yield x
        x += step


for i in frange(10, 20, 0.5):
    print(i)


# list = [1, 2, 3]
# a = iter(list)
#
# print(next(a))
# print(next(a))
