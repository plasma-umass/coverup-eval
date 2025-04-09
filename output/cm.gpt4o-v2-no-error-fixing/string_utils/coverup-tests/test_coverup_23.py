# file: string_utils/manipulation.py:500-526
# asked: {"lines": [500, 523, 524, 526], "branches": [[523, 524], [523, 526]]}
# gained: {"lines": [500, 523, 524, 526], "branches": [[523, 524], [523, 526]]}

import pytest
from string_utils.manipulation import booleanize
from string_utils.errors import InvalidInputError

def test_booleanize_true_values():
    assert booleanize('true') is True
    assert booleanize('1') is True
    assert booleanize('yes') is True
    assert booleanize('y') is True
    assert booleanize('TRUE') is True
    assert booleanize('YES') is True

def test_booleanize_false_values():
    assert booleanize('false') is False
    assert booleanize('0') is False
    assert booleanize('no') is False
    assert booleanize('n') is False
    assert booleanize('nope') is False
    assert booleanize('random') is False

def test_booleanize_invalid_input():
    with pytest.raises(InvalidInputError):
        booleanize(123)
    with pytest.raises(InvalidInputError):
        booleanize(None)
    with pytest.raises(InvalidInputError):
        booleanize(['true'])
    with pytest.raises(InvalidInputError):
        booleanize({'key': 'value'})
