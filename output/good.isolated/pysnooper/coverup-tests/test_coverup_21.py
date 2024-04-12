# file pysnooper/utils.py:23-32
# lines [26, 32]
# branches ['30->32']

import pytest
from abc import ABC, abstractmethod
from pysnooper.utils import WritableStream

class MockStream(WritableStream):
    def write(self, s):
        pass

def test_writable_stream_subclasshook():
    assert issubclass(MockStream, WritableStream)
    assert not issubclass(ABC, WritableStream)
