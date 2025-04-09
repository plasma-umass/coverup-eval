# file flutils/decorators.py:71-79
# lines [71, 73, 74, 75, 76, 77, 79]
# branches []

import asyncio
import pytest
from unittest.mock import MagicMock

# Assuming the cached_property class is part of the flutils.decorators module
from flutils.decorators import cached_property

class TestClass:
    @cached_property
    async def async_method(self):
        return 42

@pytest.mark.asyncio
async def test_cached_property_with_async_method():
    obj = TestClass()
    assert not hasattr(obj, 'async_method')

    # Access the property to ensure the coroutine is created and cached
    result = await obj.async_method
    assert result == 42
    assert 'async_method' in obj.__dict__
    assert isinstance(obj.__dict__['async_method'], asyncio.Future)

    # Access the property again to ensure the cached coroutine is used
    second_result = await obj.async_method
    assert second_result == 42
