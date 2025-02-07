# file: flutils/decorators.py:71-79
# asked: {"lines": [71, 73, 74, 75, 76, 77, 79], "branches": []}
# gained: {"lines": [71], "branches": []}

import pytest
import asyncio
from flutils.decorators import cached_property

class TestCachedProperty:
    
    @pytest.mark.asyncio
    async def test_wrap_in_coroutine(self):
        class TestClass:
            @cached_property
            async def async_method(self):
                await asyncio.sleep(0.1)
                return 42

        obj = TestClass()
        cached_prop = obj.__class__.async_method
        coroutine = cached_prop._wrap_in_coroutine(obj)
        
        result = await coroutine
        assert result == 42
        assert obj.__dict__['async_method'] == result
