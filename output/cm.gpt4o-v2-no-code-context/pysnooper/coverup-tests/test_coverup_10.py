# file: pysnooper/utils.py:23-32
# asked: {"lines": [23, 24, 25, 26, 28, 29, 30, 31, 32], "branches": [[30, 31], [30, 32]]}
# gained: {"lines": [23, 24, 25, 28, 29], "branches": []}

import pytest
from abc import ABC, abstractmethod

# Assuming _check_methods is defined somewhere in pysnooper/utils.py
from pysnooper.utils import _check_methods

class WritableStream(ABC):
    @abstractmethod
    def write(self, s):
        pass

    @classmethod
    def __subclasshook__(cls, C):
        if cls is WritableStream:
            return _check_methods(C, 'write')
        return NotImplemented

def test_writable_stream_subclasshook_with_writable():
    class TestWritable:
        def write(self, s):
            pass

    assert issubclass(TestWritable, WritableStream)

def test_writable_stream_subclasshook_without_writable():
    class TestNotWritable:
        pass

    assert not issubclass(TestNotWritable, WritableStream)

def test_writable_stream_subclasshook_not_writable_stream():
    class TestClass:
        pass

    class NotWritableStream(WritableStream):
        pass

    assert NotWritableStream.__subclasshook__(TestClass) == NotImplemented
