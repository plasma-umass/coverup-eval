# file mimesis/random.py:65-95
# lines [65, 66, 74, 75, 77, 78, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 93, 94, 95]
# branches ['77->78', '77->81', '87->88', '87->95', '88->89', '88->90', '90->91', '90->93']

import pytest
from mimesis.random import Random

@pytest.fixture
def random_instance():
    return Random()

def test_custom_code_different_placeholders(random_instance):
    mask = '@##$%'
    char = '@'
    digit = '#'
    result = random_instance.custom_code(mask=mask, char=char, digit=digit)
    assert len(result) == len(mask)
    assert result[0].isalpha() and result[0].isupper()
    assert result[1].isdigit()
    assert result[2].isdigit()
    assert result[3] == '$'
    assert result[4] == '%'

def test_custom_code_same_placeholders_error(random_instance):
    with pytest.raises(ValueError):
        random_instance.custom_code(char='@', digit='@')
