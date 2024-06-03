# file flutils/decorators.py:61-69
# lines [61, 62, 63, 65, 66, 68, 69]
# branches ['62->63', '62->65', '65->66', '65->68']

import pytest
import asyncio
from flutils.decorators import cached_property

class TestCachedProperty:
    def test_cached_property_sync(self):
        class TestClass:
            @cached_property
            def sync_method(self):
                return 42

        obj = TestClass()
        assert obj.sync_method == 42
        assert obj.__dict__['sync_method'] == 42

    @pytest.mark.asyncio
    async def test_cached_property_async(self):
        class TestClass:
            @cached_property
            async def async_method(self):
                return 42

        obj = TestClass()
        result = await obj.async_method
        assert result == 42
        assert obj.__dict__['async_method'] == 42

    def test_cached_property_none(self):
        class TestClass:
            @cached_property
            def sync_method(self):
                return 42

        obj = None
        prop = TestClass.sync_method
        assert prop.__get__(obj, TestClass) is prop
