# file flutils/decorators.py:71-79
# lines [71, 73, 74, 75, 76, 77, 79]
# branches []

import pytest
import asyncio
from flutils.decorators import cached_property

class TestCachedProperty:
    @pytest.mark.asyncio
    async def test_wrap_in_coroutine(self, mocker):
        class TestClass:
            @cached_property
            async def async_method(self):
                await asyncio.sleep(0.1)
                return 'result'

        test_instance = TestClass()
        cached_prop = cached_property(test_instance.async_method)
        
        # Mock the function to ensure it gets called
        mock_func = mocker.patch.object(test_instance, 'async_method', wraps=test_instance.async_method)
        
        # Call the _wrap_in_coroutine method
        result = await cached_prop._wrap_in_coroutine(test_instance)
        
        # Ensure the function was called
        mock_func.assert_called_once()
        
        # Ensure the result is a future and has the expected value
        assert isinstance(result, asyncio.Future)
        assert await result == 'result'
        
        # Ensure the future is stored in the instance's __dict__
        assert test_instance.__dict__['async_method'] == result
