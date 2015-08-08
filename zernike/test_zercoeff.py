#
from zercoeff import zernike_coeff



def test_zernike_coeff():
    assert zernike_coeff(0, 0) == [1.0]
    assert zernike_coeff(1, 1) == [0.0, 1.0]
    assert zernike_coeff(2, 0) == [-1.0, 0, 2.0]
    assert zernike_coeff(2, 2) == [0, 0, 1.0]

