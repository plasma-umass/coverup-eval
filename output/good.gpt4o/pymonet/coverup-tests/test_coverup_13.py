# file pymonet/maybe.py:101-112
# lines [101, 110, 111, 112]
# branches ['110->111', '110->112']

import pytest
from pymonet.maybe import Maybe

class TestMaybe:
    def test_get_or_else_with_value(self):
        maybe = Maybe(42, False)
        assert maybe.get_or_else(0) == 42

    def test_get_or_else_with_default(self):
        maybe = Maybe(None, True)
        assert maybe.get_or_else(0) == 0
