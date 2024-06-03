# file mimesis/random.py:65-95
# lines [65, 66, 74, 75, 77, 78, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 93, 94, 95]
# branches ['77->78', '77->81', '87->88', '87->95', '88->89', '88->90', '90->91', '90->93']

import pytest
from mimesis.random import Random

def test_custom_code():
    rnd = Random()

    # Test with default parameters
    result = rnd.custom_code()
    assert len(result) == 4
    assert result[0].isalpha()
    assert result[1:].isdigit()

    # Test with custom mask
    result = rnd.custom_code(mask='##@@')
    assert len(result) == 4
    assert result[:2].isdigit()
    assert result[2:].isalpha()

    # Test with same char and digit placeholders
    with pytest.raises(ValueError):
        rnd.custom_code(char='#', digit='#')

    # Test with different mask, char, and digit
    result = rnd.custom_code(mask='@@@###', char='@', digit='#')
    assert len(result) == 6
    assert result[:3].isalpha()
    assert result[3:].isdigit()

    # Test with non-default placeholders
    result = rnd.custom_code(mask='**$$$', char='*', digit='$')
    assert len(result) == 5
    assert result[:2].isalpha()
    assert result[2:].isdigit()
