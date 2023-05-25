from twttr import shorten

# Test that all vowels are removed. Test capitalization, numbers and punctuation characters work as intended.
def test_shorten():
    assert shorten("Twttier") == "Twttr"
    assert shorten("CS50") == "CS50"
    assert shorten("AaEeIiOoUu") == ""
    assert shorten("!@#$%^&*()?><:[].,';") == "!@#$%^&*()?><:[].,';"