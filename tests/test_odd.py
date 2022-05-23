from typing_extensions import assert_type
from fifth_challenge.data.odd import odd

def test_odd():
    number = 4
    assert odd(number) == False
    result = odd(number)
    assert isinstance(result, bool)
