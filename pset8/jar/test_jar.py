from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    
def test_init_with_arugment():
    jar = Jar(6)
    assert jar.capacity == 6
    
def test_deposit_more_than_capacity():
    jar = Jar(1)
    with pytest.raises(ValueError):
        jar.deposit(2)

def test_valid_deposit():
    jar = Jar(1)
    jar.deposit(1)
    assert jar.size == 1
    
def test_withdraw_more_than_available():
    jar = Jar(1)
    with pytest.raises(ValueError):
        jar.withdraw(1)
        
def test_valid_withdraw():
    jar = Jar(1)
    jar.deposit(1)
    jar.withdraw(1)
    assert jar.size == 0
    
