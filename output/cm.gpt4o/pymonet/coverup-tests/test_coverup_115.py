# file pymonet/box.py:37-46
# lines [46]
# branches []

import pytest
from pymonet.box import Box

class TestBox:
    def test_bind_executes_mapper(self):
        class TestBox(Box):
            def __init__(self, value):
                self.value = value

        def mapper(x):
            return x * 2

        box = TestBox(10)
        result = box.bind(mapper)
        
        assert result == 20

    def test_bind_with_mock(self, mocker):
        class TestBox(Box):
            def __init__(self, value):
                self.value = value

        mapper = mocker.Mock(return_value=30)
        box = TestBox(15)
        result = box.bind(mapper)
        
        mapper.assert_called_once_with(15)
        assert result == 30
