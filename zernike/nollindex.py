import math


def noll_to_nm(j):

    j1 = j-1
    x = 0.5 * (math.sqrt(8 * j1 + 1) - 1)
    n = int(x)
    n1 = n * (n +1) // 2
    steps = j1 - n1
    r4 = n % 4

    sj2 = j % 2
    sign = -2*sj2 + 1

    if r4 in [2, 3]:
        off = -sj2
    if r4 in [0, 1]:
        off = (sj2 + 1) % 2

    m = sign * steps + off
    return n,m


def nm_to_noll(n, m):
    n1 = (n * (n +1) // 2) + 1
    r4 = n % 4

    if r4 in [0, 1]:
        idm = m

    if r4 in [2, 3]:
        idm = -m

    k = -1 if idm > 0 else 0
    j = n1 + abs(m) + k
    return j

