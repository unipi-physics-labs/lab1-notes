import sys

for n in (1, 2**32, 2**64):
    print(n, sys.getsizeof(n))
