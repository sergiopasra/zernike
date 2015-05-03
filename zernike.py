#

# http://mathworld.wolfram.com/ZernikePolynomial.html


from __future__ import division

import math
from scipy.special import jacobi, eval_jacobi
import numpy

def zernike_calc(n, m, rho, phi):

    if m < 0:
        return zernike_odd_calc(n, -m, rho, phi)
    else:
        return zernike_even_calc(n, m, rho, phi)

def zernike_odd_calc(n, m, rho, phi):
    return zernike_R_calc(n, m, rho) * math.sin(m * phi)

def zernike_even_calc(n, m, rho, phi):
    return zernike_R_calc(n, m, rho) * math.cos(m * phi)

def zernike_R_calc(m, n, rho):
    # n>=m>=0

    k = n - m

    if k % 2 == 1:
        return 0.0

    n_jacobi = k // 2

    comp = 1 - 2 * rho * rho
    # jacobi form
    jacobi_pol = jacobi(n=n_jacobi, alpha=m, beta=0)

    print '|jpol', jacobi_pol, '1'
    return (-1)**n_jacobi * rho**m * jacobi_pol(comp)

class ZernikePol(object):
    def __init__(self, m, n):
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

def eval_zernike_R(m, n, rho):
    # n>=m
    # m>=0

    k = n - m

    if k % 2 == 1:
        return 0.0

    n_jacobi = k // 2

    comp = 1 - 2 * rho * rho
    # jacobi form
    return (-1)**n_jacobi * rho**m * eval_jacobi(n_jacobi, m, 0, comp)

def eval_zernike(n, m, rho, phi):

    if m < 0:
        return eval_zernike_R(n, m, rho) * math.sin(m * phi)
    else:
        return eval_zernike_R(n, m, rho) * math.cos(m * phi)

