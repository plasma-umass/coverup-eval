# file: pysnooper/utils.py:23-32
# asked: {"lines": [23, 24, 25, 26, 28, 29, 30, 31, 32], "branches": [[30, 31], [30, 32]]}
# gained: {"lines": [23, 24, 25, 28, 29, 30, 31], "branches": [[30, 31]]}

import pytest
from pysnooper.utils import WritableStream
import abc

class TestWritableStream:
    
    def test_writable_stream_subclasshook_with_write_method(self):
        class TestStream:
            def write(self, s):
                pass
        
        assert WritableStream.__subclasshook__(TestStream) is True

    def test_writable_stream_subclasshook_without_write_method(self):
        class TestStream:
            pass
        
        assert WritableStream.__subclasshook__(TestStream) is NotImplemented

    def test_writable_stream_subclasshook_with_none_write_method(self):
        class TestStream:
            write = None
        
        assert WritableStream.__subclasshook__(TestStream) is NotImplemented

    def test_writable_stream_cannot_instantiate(self):
        with pytest.raises(TypeError):
            WritableStream()

    def test_writable_stream_subclass_can_instantiate(self):
        class TestStream(WritableStream):
            def write(self, s):
                pass
        
        instance = TestStream()
        assert isinstance(instance, WritableStream)
