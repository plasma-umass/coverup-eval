# file pymonet/maybe.py:153-164
# lines [153, 160, 162, 163, 164]
# branches ['162->163', '162->164']

import pytest
from pymonet.maybe import Maybe
from pymonet.monad_try import Try

@pytest.fixture
def nothing_maybe():
    return Maybe.nothing()

@pytest.fixture
def just_maybe():
    return Maybe.just(42)

def test_maybe_to_try_with_nothing(nothing_maybe):
    result = nothing_maybe.to_try()
    assert isinstance(result, Try)
    assert result.is_success is False
    assert result.value is None

def test_maybe_to_try_with_just(just_maybe):
    result = just_maybe.to_try()
    assert isinstance(result, Try)
    assert result.is_success is True
    assert result.value == 42
