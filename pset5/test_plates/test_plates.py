from plates import is_valid

def test_plate_len_less_than_2():
    assert is_valid("C") == False
    assert is_valid("c") == False
    assert is_valid("CS") == True

def test_plate_len_greater_than_6():
    assert is_valid("ABCDEFG") == False
    assert is_valid("abcdefg") == False
    assert is_valid("abcdef") == True

def test_first_two_characters_are_alphabetical():
    assert is_valid("1C") == False
    assert is_valid("C1") == False
    assert is_valid("50") == False
    assert is_valid("1") == False

def test_all_characters_are_alphanumeric():
    assert is_valid("CS!50") == False
    assert is_valid("CS\n50") == False
    assert is_valid(" CS50 ") == False
    assert is_valid("CS50.,") == False

def test_invalid_alphabetical_characters_after_numbers():
    assert is_valid("CS5C") == False

def test_first_number_is_not_zero():
    assert is_valid("CS05") == False
    assert is_valid("abc012") == False

def test_is_valid_plate():
    assert is_valid("CS50") == True
    assert is_valid("ABC123") == True
