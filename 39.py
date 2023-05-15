"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""
import math

p = [0]*1000

for a in range(1,999):
    for b in range(1, 1000 - a):
        for c in range(1, 1000 - b - a):
            if (a * a + b * b) == (c * c):
                p[a + b + c] += 1

max = p[0]
for i in p:
    if i > max:
        max = i

print(p.index(max), max)