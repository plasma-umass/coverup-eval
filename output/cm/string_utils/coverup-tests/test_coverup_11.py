# file string_utils/manipulation.py:500-526
# lines [500, 523, 524, 526]
# branches ['523->524', '523->526']

import pytest
from string_utils.manipulation import booleanize

def test_booleanize_true_values():
    assert booleanize('true')
    assert booleanize('1')
    assert booleanize('yes')
    assert booleanize('y')
    assert booleanize('TRUE')
    assert booleanize('YES')
    assert booleanize('Y')

def test_booleanize_false_values():
    assert not booleanize('false')
    assert not booleanize('0')
    assert not booleanize('no')
    assert not booleanize('n')

def test_booleanize_invalid_input(mocker):
    mocker.patch('string_utils.manipulation.is_string', return_value=False)
    with pytest.raises(Exception):
        booleanize('invalid_input')
