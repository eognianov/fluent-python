import bisect
import random
from typing import Callable, List

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FMT = '{0:2d} @ {1:2d} {2}{0:<2d}'


def demo(bisect_fn: Callable):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)
        offset = position * ' |'
        print(ROW_FMT.format(needle, position, offset))


print('haystack ->', ''.join('%2d' % n for n in HAYSTACK))
demo(bisect.bisect)


def grade(score: int):
    breakpoints: List[int] = [60, 70, 80, 90]
    grades: str = 'FDCBA'
    index = bisect.bisect(breakpoints, score)
    return grades[index]


print([grade(score) for score in [33, 99, 77, 70, 89, 90, 100]])

# bisect insprt

SIZE = 7
random.seed(1729)
my_sorted_list = []
for i in range(SIZE):
    item = random.randrange(SIZE*2)
    bisect.insort(my_sorted_list, item)
    print(f"{item}->{my_sorted_list}")