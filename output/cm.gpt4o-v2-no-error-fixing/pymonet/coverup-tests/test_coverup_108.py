# file: pymonet/maybe.py:153-164
# asked: {"lines": [160, 162, 163, 164], "branches": [[162, 163], [162, 164]]}
# gained: {"lines": [160, 162, 163, 164], "branches": [[162, 163], [162, 164]]}

import pytest
from pymonet.maybe import Maybe
from pymonet.monad_try import Try

def test_maybe_to_try_with_value():
    maybe = Maybe("value", is_nothing=False)
    result = maybe.to_try()
    assert isinstance(result, Try)
    assert result.is_success
    assert result.value == "value"

def test_maybe_to_try_without_value():
    maybe = Maybe(None, is_nothing=True)
    result = maybe.to_try()
    assert isinstance(result, Try)
    assert not result.is_success
    assert result.value is None
