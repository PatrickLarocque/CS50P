from working import convert
import pytest

def test_valid_inputs():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"
    assert convert("12:00 PM to 12:00 PM") == "12:00 to 12:00"
    assert convert("12:00 AM to 12:00 AM") == "00:00 to 00:00"
    
def test_hours_out_of_range():
    with pytest.raises(ValueError):
        convert("13 AM to 5 PM")
    with pytest.raises(ValueError):
        convert("9 AM to 13 PM")
    with pytest.raises(ValueError):
        convert("-1 AM to 5 PM")
    with pytest.raises(ValueError):
        convert("9 AM to -1 PM")
    with pytest.raises(ValueError):
        convert("0 AM to 5 PM")
    with pytest.raises(ValueError):
        convert("9 AM to 0 PM")
        
def test_invalid_twelve_hour_syntax():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("9AM to 5 PM")
    with pytest.raises(ValueError):
        convert("9 AM to 5PM")
    with pytest.raises(ValueError):
        convert("9 AMto 5PM")
    with pytest.raises(ValueError):
        convert("9 AM to5PM")
    with pytest.raises(ValueError):
        convert(" 9 AM to 5PM ")
    with pytest.raises(ValueError):
        convert("9 AM 5 PM")

