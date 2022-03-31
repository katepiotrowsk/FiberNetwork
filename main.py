from heapq import heappop, heappush, heapify
from math import hypot

def dist(a, b):
   """Get the distance between two networks"""
   return hypot(a[0]-b[0], a[1]-b[1])

houses = []
try:
    while True:
        line = input()
        x, y = map(float, line.split(','))
        houses.append((x, y))
except EOFError:
    pass

n = len(houses)
res = 0.0
# entries of h are of the form (dist, i, j)
unseen = set(range(n))
h = [(dist(houses[0], houses[j]), 0, j) for j in range(1, n)]
heapify(h)
unseen.remove(0)
while unseen:
    d, i, j = heappop(h)
    if i not in unseen and j not in unseen:
        continue
    res += d
    if j in unseen:
        i, j = j, i
    unseen.remove(i)
    for k in range(n):
        if k in unseen:
            heappush(h, (dist(houses[i], houses[k]), i, k))

print(f"{res:.2f}")
