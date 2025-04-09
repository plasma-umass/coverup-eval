# file: flutils/decorators.py:61-69
# asked: {"lines": [61, 62, 63, 65, 66, 68, 69], "branches": [[62, 63], [62, 65], [65, 66], [65, 68]]}
# gained: {"lines": [61, 62, 63, 65, 66, 68, 69], "branches": [[62, 63], [62, 65], [65, 66], [65, 68]]}

import pytest
import asyncio
from flutils.decorators import cached_property

class TestCachedProperty:
    def test_cached_property_with_none_obj(self):
        class TestClass:
            @cached_property
            def method(self):
                return 42

        prop = TestClass.method
        result = prop.__get__(None, TestClass)
        assert result is prop

    def test_cached_property_with_coroutine_function(self, monkeypatch):
        class TestClass:
            @cached_property
            async def async_method(self):
                return 42

        async def mock_wrap_in_coroutine(self, obj):
            return 42

        monkeypatch.setattr(cached_property, '_wrap_in_coroutine', mock_wrap_in_coroutine)

        obj = TestClass()
        result = obj.async_method
        assert asyncio.run(result) == 42

    def test_cached_property_with_regular_function(self):
        class TestClass:
            @cached_property
            def regular_method(self):
                return 42

        obj = TestClass()
        result = obj.regular_method
        assert result == 42
        assert obj.__dict__['regular_method'] == 42
