from bank import value

def test_greeting_is_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELL0") == 20

def test_greeting_starts_with_h():
    assert value("hell1") == 20
    assert value("HI") == 20
    assert value("h ") == 20
    assert value("ello") == 100

def test_greeting_neither_hello_nor_starts_with_h():
    assert value("123") == 100
    assert value("") == 100
    assert value("_.?") == 100
    assert value("\n") == 100
    assert value("h\n") == 20