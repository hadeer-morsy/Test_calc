import pytest
from calculator import Calculator


def test_calculator_creation():
    assert Calculator() is not None


@pytest.mark.parametrize('a, b, result', [
    (1, 1, 2),
    (1, 2, 3),
    (100, 100, 200),
    (2000, 10, 2010),
    (222, 111, 333),
    (200, -200, 0),
])
def test_addition_parametrized(a, b, result):
    assert Calculator().add(a, b) == result


@pytest.mark.parametrize('a, b, result', [
    (2, 1, 1),
    (5, 2, 3),
    (300, 100, 200),
    (2020, 10, 2010),
    (444, 111, 333),
    (-200, -200, 0),
])
def test_subtraction_parametrized(a, b, result):
    assert Calculator().sub(a, b) == result


@pytest.mark.parametrize('a, b, result', [
    (1, 1, 1),
    (1, 2, 2),
    (100, 100, 10000),
    (200, 10, 2000),
    (22, 111, 2442),
    (200, 0, 0),
])
def test_multiplication_parametrized(a, b, result):
    assert Calculator().mult(a, b) == result


@pytest.mark.parametrize('a, b, result', [
    (2, 1, 2.0),  # Division should return a float
    (4, 2, 2.0),
    (100, 100, 1.0),
    (200, 10, 20.0),
    (2442, 111, 22.0),
    (0, 100, 0.0),
])
def test_division_parametrized(a, b, result):
    assert Calculator().div(a, b) == result
