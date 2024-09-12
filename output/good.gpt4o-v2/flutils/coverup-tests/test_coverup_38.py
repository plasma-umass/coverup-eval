# file: flutils/decorators.py:61-69
# asked: {"lines": [61, 62, 63, 65, 66, 68, 69], "branches": [[62, 63], [62, 65], [65, 66], [65, 68]]}
# gained: {"lines": [61, 62, 63, 65, 66, 68, 69], "branches": [[62, 63], [62, 65], [65, 66], [65, 68]]}

import pytest
import asyncio
from flutils.decorators import cached_property

class TestClass:
    @cached_property
    def regular_method(self):
        return 42

    @cached_property
    async def coroutine_method(self):
        await asyncio.sleep(0.1)
        return 42

def test_cached_property_regular_method():
    obj = TestClass()
    assert obj.regular_method == 42
    assert obj.__dict__['regular_method'] == 42

@pytest.mark.asyncio
async def test_cached_property_coroutine_method():
    obj = TestClass()
    result = await obj.coroutine_method
    assert result == 42
    assert isinstance(obj.__dict__['coroutine_method'], asyncio.Future)
    assert await obj.__dict__['coroutine_method'] == 42

def test_cached_property_none_obj():
    def dummy_func():
        return 42
    prop = cached_property(dummy_func)
    result = prop.__get__(None, TestClass)
    assert result is prop
