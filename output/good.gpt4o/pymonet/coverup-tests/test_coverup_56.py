# file pymonet/maybe.py:19-22
# lines [19, 20, 21, 22]
# branches []

import pytest
from pymonet.maybe import Maybe

class TestMaybe:
    def test_maybe_eq(self):
        maybe1 = Maybe(None, True)
        maybe2 = Maybe(None, True)
        assert maybe1 == maybe2

        maybe3 = Maybe(10, False)
        maybe4 = Maybe(10, False)
        assert maybe3 == maybe4

        maybe5 = Maybe(20, False)
        assert maybe3 != maybe5

        assert maybe1 != maybe3
        assert maybe1 != "not a Maybe instance"
