import math



def other_index(otheri):

    x = 0.5 * (math.sqrt(8 * otheri + 1) - 1)
    n = int(x)
    remain = n * (n +1) // 2
    steps = otheri - remain
    m = -n + 2 * steps
    return n, m

# Noll index 

# 0,0 1,1 1,-1, 2,0 2,-2, 2,2,  3,-1, 3,1, 3,-3, 3,3
#  1   2   3     4   5     6     7     8    9    10o
# impares a m < 0
# pares a m >= 0
# j mas peque a |m| mas peque


#def noll_to_nm(j):
#
#    j1 = j-1
#    x = 0.5 * (math.sqrt(8 * j1 + 1) - 1)
#    n = int(x)
#    rr = n * (n +1) // 2
#    s1 = j1 - rr
#
#    m = (-1)**j * ((n % 2) + 2 *  int((s1 + ((n+1) %2)) / 2.0))
#    return n,m


def nm_to_noll(n, m):
    n1 = (n * (n +1) // 2) + 1
    n2 = n1 + n
    rr = n1 % 2
    primer_par =  n1 + rr
    primer_impar = n1 + 1 - rr
    if n == 0:
        j = 1
    elif ((n + 1) % 2) == 0:
        if m > 0:
            j = n1 + rr + abs(m) - 1
        else:
            j = n1 + 1 - rr  + abs(m) - 1
    else:
        if rr < 1 - rr:
            if m >= 0:
                j = primer_par + abs(m)
            else:
                j = primer_impar + (abs(m)-2)
        else:
            if m > 0:
                j = primer_par + (abs(m) - 2)
            else:
                j = primer_impar + abs(m)
            
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


test_noll()
