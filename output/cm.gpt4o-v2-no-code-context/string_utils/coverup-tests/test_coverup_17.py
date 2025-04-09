# file: string_utils/manipulation.py:500-526
# asked: {"lines": [500, 523, 524, 526], "branches": [[523, 524], [523, 526]]}
# gained: {"lines": [500, 523, 524, 526], "branches": [[523, 524], [523, 526]]}

import pytest
from string_utils.manipulation import booleanize, InvalidInputError

def test_booleanize_true_values():
    assert booleanize('true') is True
    assert booleanize('TRUE') is True
    assert booleanize('1') is True
    assert booleanize('yes') is True
    assert booleanize('YES') is True
    assert booleanize('y') is True
    assert booleanize('Y') is True

def test_booleanize_false_values():
    assert booleanize('false') is False
    assert booleanize('FALSE') is False
    assert booleanize('0') is False
    assert booleanize('no') is False
    assert booleanize('NO') is False
    assert booleanize('n') is False
    assert booleanize('N') is False
    assert booleanize('nope') is False
    assert booleanize('') is False

def test_booleanize_invalid_input(mocker):
    mocker.patch('string_utils.manipulation.is_string', return_value=False)
    with pytest.raises(InvalidInputError):
        booleanize('invalid')
