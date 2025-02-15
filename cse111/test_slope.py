import pytest
import random

def get_slope(m, x, b):
    if b == None:
        b=0
    return m*x + b 
    
def test_get_slope():
    assert get_slope(2, 2, 2) == 6
    assert get_slope(3, 3, 3) == 12
    assert get_slope(4, 4, 4) == 20
    assert get_slope(5, 5, 5) == 30
    assert get_slope(6, 6, 6) == 42
    assert get_slope(7, 7, 7) == 56

def test_get_slope_random():
    for i in range (100):
        m = random.randint(1, 100)
        x = random.randint(1, 100)
        b = random.randint(1, 100)
        assert get_slope(m, x, b) == m*x + b

def test_get_slope_random_negative():
    for i in range (100):
        m = random.randint(-100, -1)
        x = random.randint(-100, -1)
        b = random.randint(-100, -1)
        assert get_slope(m, x, b) == m*x + b

def test_get_slope_random_zero():
    for i in range (100):
        m = random.randint(-100, 100)
        x = 0
        b = random.randint(-100, 100)
        assert get_slope(m, x, b) == m*x + b

def test_get_slope_random_none():
    for i in range (100):
        m = 0
        x = random.randint(-100, 100)
        b = random.randint(-100, 100)
        assert get_slope(m, x, b) == m*x + b