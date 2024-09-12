# file: flutils/decorators.py:71-79
# asked: {"lines": [71, 73, 74, 75, 76, 77, 79], "branches": []}
# gained: {"lines": [71], "branches": []}

import pytest
import asyncio
from flutils.decorators import cached_property

class TestCachedProperty:
    @pytest.fixture
    def mock_func(self, mocker):
        return mocker.Mock()

    @pytest.fixture
    def mock_obj(self, mocker):
        return mocker.Mock()

    @pytest.fixture
    def cached_prop(self, mock_func):
        class TestClass:
            @cached_property
            def test_method(self):
                return mock_func()
        return TestClass()

    @pytest.mark.asyncio
    async def test_wrap_in_coroutine(self, mock_func, mock_obj, cached_prop):
        mock_func.return_value = asyncio.Future()
        mock_func.return_value.set_result('test_result')

        cached_prop.func = mock_func
        coroutine = cached_prop._wrap_in_coroutine(mock_obj)
        result = await coroutine

        assert result == mock_func.return_value
        assert mock_obj.__dict__[mock_func.__name__] == mock_func.return_value

    @pytest.mark.asyncio
    async def test_wrap_in_coroutine_with_exception(self, mock_func, mock_obj, cached_prop):
        mock_func.side_effect = Exception('test_exception')

        cached_prop.func = mock_func
        coroutine = cached_prop._wrap_in_coroutine(mock_obj)

        with pytest.raises(Exception, match='test_exception'):
            await coroutine

        assert mock_func.__name__ not in mock_obj.__dict__
