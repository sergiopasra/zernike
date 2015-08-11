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


def test_noll():
    # Noll sequence from OEIS
    # A176988
    noll = [1, 3, 2, 5, 4, 6, 9, 7, 8, 10, 15, 13, 11, 12, 14, 21, 19, 17, 16, 18, 20, 27, 25, 23, 22, 24, 26, 28, 35, 33, 31, 29, 30, 32, 34, 36, 45, 43, 41, 39, 37, 38, 40, 42, 44, 55, 53, 51, 49, 47, 46, 48, 50, 52, 54, 65, 63, 61, 59, 57, 56, 58, 60, 62, 64, 66, 77, 75, 73, 71, 69, 67, 68, 70, 72, 74, 76, 78, 91, 89, 87, 85, 83, 81, 79, 80, 82, 84, 86, 88, 90, 105, 103, 101, 99, 97, 95, 93, 92, 94, 96, 98, 100, 102, 104, 119, 117, 115, 113, 111, 109, 107, 106, 108, 110, 112, 114, 116, 118, 120]
    inoll = iter(noll)
    for n in range(15):
        for m in range(-n, n+1, 2):
            j = nm_to_noll(n, m) 
            j_noll = next(inoll)
            assert j == j_noll

    inoll = iter(noll)
    for n in range(15):
        for m in range(-n, n+1, 2):
            j_noll = next(inoll)
            nn, mm = noll_to_nm(j_noll) 
            assert nn == n
            assert mm == m

test_noll()
