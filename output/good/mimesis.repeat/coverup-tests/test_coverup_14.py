# file mimesis/random.py:65-95
# lines [65, 66, 74, 75, 77, 78, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 93, 94, 95]
# branches ['77->78', '77->81', '87->88', '87->95', '88->89', '88->90', '90->91', '90->93']

import pytest
from mimesis.random import Random

@pytest.fixture
def random_instance():
    return Random()

def test_custom_code_with_different_placeholders(random_instance):
    result = random_instance.custom_code(mask='@#A', char='@', digit='#')
    assert len(result) == 3
    assert result[1].isdigit()
    assert result[0].isupper()
    assert result[2] == 'A'

def test_custom_code_with_same_placeholders(random_instance):
    with pytest.raises(ValueError):
        random_instance.custom_code(mask='@@@', char='@', digit='@')

def test_custom_code_with_custom_mask(random_instance):
    mask = 'ABC###XYZ@@@123'
    result = random_instance.custom_code(mask=mask, char='@', digit='#')
    assert len(result) == len(mask)
    for i, char in enumerate(mask):
        if char == '@':
            assert result[i].isupper()
        elif char == '#':
            assert result[i].isdigit()
        else:
            assert result[i] == char
