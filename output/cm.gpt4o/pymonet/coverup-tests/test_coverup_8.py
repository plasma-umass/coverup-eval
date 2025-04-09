# file pymonet/maybe.py:14-17
# lines [14, 15, 16, 17]
# branches ['16->exit', '16->17']

import pytest
from pymonet.maybe import Maybe

def test_maybe_initialization():
    # Test case where is_nothing is False
    maybe_value = Maybe(10, False)
    assert not maybe_value.is_nothing
    assert maybe_value.value == 10

    # Test case where is_nothing is True
    maybe_nothing = Maybe(None, True)
    assert maybe_nothing.is_nothing
    assert not hasattr(maybe_nothing, 'value')
