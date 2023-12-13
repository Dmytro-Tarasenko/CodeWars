# Consider a sequence u where u is defined as follows:
#
# The number u(0) = 1 is the first one in u.
# For each x in u, then y = 2 * x + 1 and z = 3 * x + 1 must be in u too.
# There are no other numbers in u.
# Ex: u = [1, 3, 4, 7, 9, 10, 13, 15, 19, 21, 22, 27, ...]
#
# 1 gives 3 and 4, then 3 gives 7 and 10, 4 gives 9 and 13, then 7 gives 15 and 22 and so on...
#
# Task:
# Given parameter n the function dbl_linear (or dblLinear...) returns the element u(n) of the
# ordered (with <) sequence u (so, there are no duplicates).
#
# Example:
# dbl_linear(10) should return 22
#
# Note:
# Focus attention on efficiency

from collections import deque


def dbl_linear_deque(n):
    u, q2, q3 = 1, deque([]), deque([])
    for _ in range(n):
        q2.append(2 * u + 1)
        q3.append(3 * u + 1)
        u = min(q2[0], q3[0])
        if u == q2[0]: q2.popleft()
        if u == q3[0]: q3.popleft()
    return u

def dbl_linear_best_imho(n):
    u = [1]
    i = 0
    j = 0
    while len(u) <= n:
        x = 2 * u[i] + 1
        y = 3 * u[j] + 1
        if x <= y:
            i += 1
        if x >= y:
            j += 1
        u.append(min(x,y))
    return u[n]
