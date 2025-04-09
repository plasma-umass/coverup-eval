# file: pysnooper/utils.py:23-32
# asked: {"lines": [23, 24, 25, 26, 28, 29, 30, 31, 32], "branches": [[30, 31], [30, 32]]}
# gained: {"lines": [23, 24, 25, 28, 29, 30, 31], "branches": [[30, 31]]}

import pytest
from pysnooper.utils import WritableStream
from unittest.mock import MagicMock

def test_writable_stream_subclasshook():
    class TestStream:
        def write(self, s):
            pass

    class TestStreamInvalid:
        write = None

    assert WritableStream.__subclasshook__(TestStream) is True
    assert WritableStream.__subclasshook__(TestStreamInvalid) is NotImplemented
    assert WritableStream.__subclasshook__(object) is NotImplemented

def test_writable_stream_write():
    with pytest.raises(TypeError):
        instance = WritableStream()
        instance.write("test")
