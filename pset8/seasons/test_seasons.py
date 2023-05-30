from seasons import minutes_between
import pytest

def test_minutes_between():
    assert minutes_between("2022-05-30") == "Five hundred twenty-five thousand, six hundred minutes"
    
def test_invalid_dates():
    with pytest.raises(ValueError):
        minutes_between("cat")
    with pytest.raises(ValueError):
        minutes_between("05-30-2022")
    with pytest.raises(ValueError):
        minutes_between("30-05-2022")
    with pytest.raises(ValueError):
        minutes_between("May 30th, 2022")
    with pytest.raises(ValueError):
        minutes_between("May 30 2022")
    with pytest.raises(ValueError):
        minutes_between("05/30/2022")
    with pytest.raises(ValueError):
        minutes_between("30/05/2022")