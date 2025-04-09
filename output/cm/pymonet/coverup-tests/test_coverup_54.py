# file pymonet/maybe.py:73-85
# lines [73, 83, 84, 85]
# branches ['83->84', '83->85']

import pytest
from pymonet.maybe import Maybe

def test_maybe_ap_with_nothing(mocker):
    # Mock the Maybe.nothing method to ensure it is called and to verify it does not affect other tests
    mocker.patch('pymonet.maybe.Maybe.nothing', return_value=Maybe(None, True))

    nothing_maybe = Maybe(None, True)
    applicative = Maybe(lambda x: x + 1, False)

    result = nothing_maybe.ap(applicative)

    # Assert that Maybe.nothing was called and the result is a Maybe with None
    Maybe.nothing.assert_called_once()
    assert isinstance(result, Maybe)
    assert result.is_nothing

def test_maybe_ap_with_value():
    just_maybe = Maybe(lambda x: x * 2, False)
    applicative = Maybe(3, False)

    result = just_maybe.ap(applicative)

    # Assert that the function inside just_maybe is applied to the value of applicative
    assert isinstance(result, Maybe)
    assert not result.is_nothing
    assert result.value == 6
