# file: flutils/decorators.py:61-69
# asked: {"lines": [62, 63, 65, 66, 68, 69], "branches": [[62, 63], [62, 65], [65, 66], [65, 68]]}
# gained: {"lines": [62, 63, 65, 66, 68, 69], "branches": [[62, 63], [62, 65], [65, 66], [65, 68]]}

import pytest
import asyncio
from flutils.decorators import cached_property

class TestCachedProperty:
    @pytest.fixture
    def mock_func(self, mocker):
        return mocker.Mock()

    @pytest.fixture
    def mock_obj(self, mock_func):
        class MockClass:
            @cached_property
            def prop(self):
                return mock_func()
        return MockClass()

    def test_cached_property_sync(self, mock_obj, mock_func):
        mock_func.return_value = 42
        assert mock_obj.prop == 42
        assert mock_obj.prop == 42
        mock_func.assert_called_once()

    def test_cached_property_async(self, mocker, mock_func):
        async def async_func():
            return 42

        class MockClass:
            @cached_property
            async def prop(self):
                return await async_func()

        mock_obj = MockClass()
        loop = asyncio.get_event_loop()
        result = loop.run_until_complete(mock_obj.prop)
        assert result == 42

    def test_cached_property_none_obj(self):
        class MockClass:
            @cached_property
            def prop(self):
                return 42

        assert MockClass.prop.__get__(None, MockClass) is MockClass.prop
