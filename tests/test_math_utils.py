from utils.math_utils import suma, resta


def test_suma():
    assert suma(2, 3) == 5
    assert suma(-1, 1) == 0


def test_resta():
    assert resta(5, 3) == 2
    assert resta(0, 5) == -5
