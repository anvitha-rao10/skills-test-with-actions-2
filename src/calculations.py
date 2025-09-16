import pytest
import math
from src.calculations import area_of_circle, get_nth_fibonacci

# ----------------------------
# Tests for area_of_circle()
# ----------------------------
def test_area_of_circle_positive():
    assert math.isclose(area_of_circle(1), math.pi)
    assert math.isclose(area_of_circle(2), 4 * math.pi)
    assert math.isclose(area_of_circle(0), 0)

def test_area_of_circle_negative():
    with pytest.raises(ValueError):
        area_of_circle(-5)


# ----------------------------
# Tests for get_nth_fibonacci()
# ----------------------------
def test_fibonacci_base_cases():
    assert get_nth_fibonacci(0) == 0
    assert get_nth_fibonacci(1) == 1

def test_fibonacci_recursive_cases():
    assert get_nth_fibonacci(2) == 1
    assert get_nth_fibonacci(3) == 2
    assert get_nth_fibonacci(5) == 5
    assert get_nth_fibonacci(10) == 55

def test_fibonacci_negative():
    with pytest.raises(ValueError):
        get_nth_fibonacci(-1)
