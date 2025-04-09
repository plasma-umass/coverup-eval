# file: flutils/decorators.py:61-69
# asked: {"lines": [61, 62, 63, 65, 66, 68, 69], "branches": [[62, 63], [62, 65], [65, 66], [65, 68]]}
# gained: {"lines": [61, 62, 63, 65, 68, 69], "branches": [[62, 63], [62, 65], [65, 68]]}

import pytest
import asyncio
from flutils.decorators import cached_property

class TestClass:
    def __init__(self, value):
        self.value = value

    @cached_property
    def sync_prop(self):
        return self.value + 1

    @cached_property
    async def async_prop(self):
        await asyncio.sleep(0.1)
        return self.value + 1

def test_cached_property_sync():
    obj = TestClass(1)
    assert obj.sync_prop == 2
    assert obj.__dict__['sync_prop'] == 2

@pytest.mark.asyncio
async def test_cached_property_async():
    obj = TestClass(1)
    result = await obj.async_prop
    assert result == 2
    assert isinstance(obj.__dict__['async_prop'], asyncio.Future)
    assert await obj.__dict__['async_prop'] == 2

def test_cached_property_none():
    prop = cached_property(lambda x: x)
    assert prop.__get__(None, TestClass) is prop
