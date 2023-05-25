from fuel import convert, gauge
import pytest

def test_converting_non_integers():
    with pytest.raises(ValueError):
        convert("cat/dog")

def test_convert_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        convert("0/0")

def test_numerator_greater_than_denominator():
    with pytest.raises(ValueError):
        convert("3/2")

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"

def test_valid_input():
    assert convert("3/4") == 75 and gauge(75) == "75%"
    assert convert("0/4") == 0 and gauge(0) == "E"
    assert convert("4/4") == 100 and gauge(100) == "F"