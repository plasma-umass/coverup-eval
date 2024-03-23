# file mimesis/exceptions.py:8-9
# lines [8, 9]
# branches []

import pytest
from mimesis.exceptions import UnsupportedAlgorithm

def test_unsupported_algorithm_exception():
    with pytest.raises(UnsupportedAlgorithm) as exc_info:
        raise UnsupportedAlgorithm("Custom message")

    assert str(exc_info.value) == "Custom message", "Exception message does not match"
