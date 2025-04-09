# file: pymonet/maybe.py:153-164
# asked: {"lines": [153, 160, 162, 163, 164], "branches": [[162, 163], [162, 164]]}
# gained: {"lines": [153, 160, 162, 163, 164], "branches": [[162, 163], [162, 164]]}

import pytest
from pymonet.maybe import Maybe
from pymonet.monad_try import Try

def test_maybe_to_try_with_value():
    maybe = Maybe.just(10)
    result = maybe.to_try()
    assert isinstance(result, Try)
    assert result.is_success
    assert result.get() == 10

def test_maybe_to_try_with_nothing():
    maybe = Maybe.nothing()
    result = maybe.to_try()
    assert isinstance(result, Try)
    assert not result.is_success
    assert result.get() is None
