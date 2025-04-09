# file: pymonet/maybe.py:153-164
# asked: {"lines": [153, 160, 162, 163, 164], "branches": [[162, 163], [162, 164]]}
# gained: {"lines": [153, 160, 162, 163, 164], "branches": [[162, 163], [162, 164]]}

import pytest
from pymonet.maybe import Maybe
from pymonet.monad_try import Try

class TestMaybe:
    def test_to_try_with_value(self):
        maybe = Maybe(42, is_nothing=False)
        result = maybe.to_try()
        assert isinstance(result, Try)
        assert result.is_success
        assert result.value == 42

    def test_to_try_without_value(self):
        maybe = Maybe(None, is_nothing=True)
        result = maybe.to_try()
        assert isinstance(result, Try)
        assert not result.is_success
        assert result.value is None
