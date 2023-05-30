from um import count

def test_words_containing_um():
    assert count("yum") == 0
    assert count("yummy") == 0
    assert count("clumsy") == 0
    assert count("sum, mum, drum, umber, lumpy, human, humid") == 0
    assert count("Umm") == 0
    
def test_um_followed_by_punctuation():
    assert count("Um?") == 1
    assert count("Um.") == 1
    assert count("um, um") == 2
    assert count("um! um; um...") == 3
    
    
def test_um_preceeded_by_other_characters():
    assert count("Hello! Um, world!") == 1
    assert count("This is, um, CS50") == 1