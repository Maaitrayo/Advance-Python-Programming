import sys

def mygenerator(n):
    for x in range(n):
        yield x**3

values = mygenerator(10000)
# size of the object doesnot change
print(sys.getsizeof(values))
# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))

# for x in values:
#     print(x)

def infinite_seqence():
    result = 1
    while True:
        yield result
        result *= 5

values = infinite_seqence()

print(next(values))
print(next(values))