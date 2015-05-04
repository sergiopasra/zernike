#

# http://mathworld.wolfram.com/ZernikePolynomial.html


from __future__ import division

import math
import numpy
from scipy.special import jacobi, eval_jacobi

class ZernikePol(object):
    def __init__(self, n, m):
        k = n - m

        if k % 2 == 1:
            self.is_zero = True
        else:
            self.is_zero = False

        n_jacobi = k // 2
        self.sign = (-1)**n_jacobi
        self.m = m
        self.n = n


        # jacobi form
        self.jacobi_pol = jacobi(n=n_jacobi, alpha=m, beta=0)

    def __call__(self, rho):
        if self.is_zero:
            return 0.0
        
        comp = 1 - 2 * rho * rho
        return self.sign * rho**self.m * self.jacobi_pol(comp)

def eval_zernike_R(n, m, rho):
    # n>=m
    # m>=0

    k = n - m

    if k % 2 == 1:
        return 0.0

    n_jacobi = k // 2

    comp = 1 - 2 * rho * rho
    # jacobi form
    print n_jacobi
    return (-1)**n_jacobi * rho**m * eval_jacobi(n_jacobi, m, 0, comp)

def eval_zernike(n, m, rho, phi):

    if m < 0:
        return eval_zernike_R(n, -m, rho) * numpy.sin(-m * phi)
    else:
        return eval_zernike_R(n, m, rho) * numpy.cos(m * phi)

