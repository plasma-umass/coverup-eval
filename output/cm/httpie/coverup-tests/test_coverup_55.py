# file httpie/output/streams.py:21-24
# lines [21, 22, 24]
# branches []

import pytest
from httpie.output.streams import BinarySuppressedError, BINARY_SUPPRESSED_NOTICE

def test_binary_suppressed_error():
    with pytest.raises(BinarySuppressedError) as exc_info:
        raise BinarySuppressedError()
    assert exc_info.value.message == BINARY_SUPPRESSED_NOTICE
