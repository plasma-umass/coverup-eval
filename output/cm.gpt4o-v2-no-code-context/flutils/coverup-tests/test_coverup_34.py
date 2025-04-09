# file: flutils/decorators.py:71-79
# asked: {"lines": [71, 73, 74, 75, 76, 77, 79], "branches": []}
# gained: {"lines": [71], "branches": []}

import pytest
import asyncio
from flutils.decorators import cached_property

class TestCachedProperty:
    
    @pytest.fixture
    def mock_func(self):
        async def mock_coroutine():
            return "result"
        return mock_coroutine

    @pytest.fixture
    def mock_obj(self, mock_func):
        class MockObj:
            def __init__(self):
                self.__dict__ = {}
        return MockObj()

    @pytest.mark.asyncio
    async def test_wrap_in_coroutine(self, mock_func, mock_obj):
        cached_prop = cached_property(mock_func)
        wrapped_coroutine = cached_prop._wrap_in_coroutine(mock_obj)
        
        assert asyncio.iscoroutine(wrapped_coroutine)
        
        future = await wrapped_coroutine
        
        assert future.result() == "result"
        assert mock_func.__name__ in mock_obj.__dict__
        assert isinstance(mock_obj.__dict__[mock_func.__name__], asyncio.Future)
