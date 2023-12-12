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

def u_n(n: int) -> list:
    res = []
    if n == 0:
        return [1]
    _2_n = [2 * i + 1 for i in u_n(n - 1)]
    _3_n = [3 * i + 1 for i in u_n(n - 1)]
    res.extend(sorted(list(set(_2_n) | set(_3_n))))

    return res


def dbl_linear(n):
    seq = [1]
    iter_ = 0

    while len(seq) <= n + 1:
        iter_ += 1
        seq.extend(u_n(iter_))

    return seq[n]

print(dbl_linear(2))
print(dbl_linear(3))
print(dbl_linear(10))
