# file pymonet/maybe.py:14-17
# lines [14, 15, 16, 17]
# branches ['16->exit', '16->17']

import pytest
from pymonet.maybe import Maybe

def test_maybe_init():
    # Test the case where is_nothing is False and a value is set
    maybe_with_value = Maybe(10, False)
    assert maybe_with_value.is_nothing is False
    assert hasattr(maybe_with_value, 'value')
    assert maybe_with_value.value == 10

    # Test the case where is_nothing is True and no value is set
    maybe_no_value = Maybe(None, True)
    assert maybe_no_value.is_nothing is True
    assert not hasattr(maybe_no_value, 'value')
