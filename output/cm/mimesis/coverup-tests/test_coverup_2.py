# file mimesis/random.py:65-95
# lines [65, 66, 74, 75, 77, 78, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 93, 94, 95]
# branches ['77->78', '77->81', '87->88', '87->95', '88->89', '88->90', '90->91', '90->93']

import pytest
from mimesis.random import Random

@pytest.fixture
def custom_random():
    return Random()

def test_custom_code_different_placeholders(custom_random):
    result = custom_random.custom_code(mask='@#A', char='@', digit='#')
    assert len(result) == 3
    assert result[0].isalpha() and result[0].isupper()
    assert result[1].isdigit()
    assert result[2] == 'A'

def test_custom_code_raises_error_on_same_placeholders(custom_random):
    with pytest.raises(ValueError):
        custom_random.custom_code(mask='@@', char='@', digit='@')
