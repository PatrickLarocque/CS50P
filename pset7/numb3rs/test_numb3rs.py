from numb3rs import validate

def test_valid_inputs():
    assert validate("0.0.0.0") == True
    assert validate("1.1.1.1") == True
    assert validate("255.255.255.255") == True

def test_values_greater_than_255():
    assert validate("256.1.1.1") == False
    assert validate("1.256.1.1") == False
    assert validate("1.1.256.1") == False
    assert validate("1.1.1.256") == False
    
def test_values_less_than_0():
    assert validate("-1.1.1.1") == False
    assert validate("1.-1.1.1") == False
    assert validate("1.1.-1.1") == False
    assert validate("1.1.1.-1") == False
        
def test_non_numeric_values():
    assert validate("cat.1.1.1") == False
    assert validate("1.cat.1.1") == False
    assert validate("1.1.cat.1") == False
    assert validate("1.1.1.cat") == False
    
def test_missing_segments():
    assert validate(".1.1.1") == False
    assert validate("1..1.1") == False
    assert validate("1.1..1") == False
    assert validate("1.1.1.") == False
    
def test_extra_segments():
    assert validate("255.255.255.255.255") == False
    assert validate("1.1.1.1.1") == False