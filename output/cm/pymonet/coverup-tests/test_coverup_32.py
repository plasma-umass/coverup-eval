# file pymonet/maybe.py:114-125
# lines [114, 121, 123, 124, 125]
# branches ['123->124', '123->125']

import pytest
from pymonet.maybe import Maybe
from pymonet.either import Left, Right

@pytest.fixture
def nothing_maybe():
    return Maybe.nothing()

@pytest.fixture
def just_maybe():
    return Maybe.just('test_value')

def test_maybe_to_either_with_nothing(nothing_maybe):
    result = nothing_maybe.to_either()
    assert isinstance(result, Left)
    assert result.value is None

def test_maybe_to_either_with_value(just_maybe):
    result = just_maybe.to_either()
    assert isinstance(result, Right)
    assert result.value == 'test_value'
