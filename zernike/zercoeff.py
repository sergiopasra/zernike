#

# http://mathworld.wolfram.com/ZernikePolynomial.html


from __future__ import division

from scipy.misc import comb
from numpy.polynomial import Polynomial as P

def zernike_coeff(n, m):

    m = abs(m)

    if m > n:
        raise ValueError('n and m -> n>=m')

    refi = n - m

    if refi % 2 == 1:
        return [0.0]

    top = refi // 2

    coeffs = [0] * (n + 1)

    for k in range(top + 1):
        pw = n - 2 * k
        coeff = (-1)**k * comb(n - k, k) * comb(n - 2*k, top - k)
        coeffs[pw] = coeff

    return coeffs


def zernike_pol(n, m):

    coeff = zernike_coeff(n, m)
    return P(coeff)

