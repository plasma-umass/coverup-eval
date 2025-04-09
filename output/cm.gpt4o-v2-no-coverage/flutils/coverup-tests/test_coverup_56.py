# file: flutils/decorators.py:61-69
# asked: {"lines": [62, 63, 65, 66, 68, 69], "branches": [[62, 63], [62, 65], [65, 66], [65, 68]]}
# gained: {"lines": [62, 63, 65, 68, 69], "branches": [[62, 63], [62, 65], [65, 68]]}

import pytest
import asyncio
from unittest.mock import Mock

from flutils.decorators import cached_property

class TestCachedProperty:
    def test_get_with_none_obj(self):
        def dummy_func():
            pass
        prop = cached_property(dummy_func)
        result = prop.__get__(None, None)
        assert result is prop

    def test_get_with_non_coroutine_function(self):
        class TestClass:
            @cached_property
            def prop(self):
                return 42

        obj = TestClass()
        result = obj.prop
        assert result == 42
        assert obj.__dict__['prop'] == 42

    @pytest.mark.asyncio
    async def test_get_with_coroutine_function(self, mocker):
        class TestClass:
            @cached_property
            async def prop(self):
                return 42

        obj = TestClass()
        mocker.patch.object(cached_property, '_wrap_in_coroutine', side_effect=cached_property._wrap_in_coroutine)
        result = await obj.prop
        assert result == 42
        assert 'prop' in obj.__dict__
        assert asyncio.isfuture(obj.__dict__['prop'])

    @pytest.mark.asyncio
    async def test_wrap_in_coroutine(self):
        class TestClass:
            @cached_property
            async def prop(self):
                return 42

        obj = TestClass()
        prop = obj.__class__.__dict__['prop']
        wrapper = prop._wrap_in_coroutine(obj)
        result = await wrapper
        assert result == 42
        assert 'prop' in obj.__dict__
        assert asyncio.isfuture(obj.__dict__['prop'])
