# file sanic/mixins/exceptions.py:6-39
# lines [11, 26, 30, 31, 33, 34, 35, 36, 37, 39]
# branches ['30->31', '30->33', '35->36', '35->37']

import pytest
from sanic.mixins.exceptions import ExceptionMixin

class FutureException:
    def __init__(self, handler, exceptions):
        self.handler = handler
        self.exceptions = exceptions

def test_exception_mixin_not_implemented_error():
    mixin = ExceptionMixin()
    with pytest.raises(NotImplementedError):
        mixin._apply_exception_handler(None)

def test_exception_mixin_decorator(mocker):
    mixin = ExceptionMixin()
    mock_handler = mocker.Mock()
    mock_apply_exception_handler = mocker.patch.object(mixin, '_apply_exception_handler')

    @mixin.exception(ValueError, apply=True)
    def handler():
        pass

    assert len(mixin._future_exceptions) == 1
    future_exception = next(iter(mixin._future_exceptions))
    assert future_exception.handler == handler
    assert future_exception.exceptions == (ValueError,)
    mock_apply_exception_handler.assert_called_once_with(future_exception)

def test_exception_mixin_decorator_with_list(mocker):
    mixin = ExceptionMixin()
    mock_handler = mocker.Mock()
    mock_apply_exception_handler = mocker.patch.object(mixin, '_apply_exception_handler')

    @mixin.exception([ValueError, KeyError], apply=True)
    def handler():
        pass

    assert len(mixin._future_exceptions) == 1
    future_exception = next(iter(mixin._future_exceptions))
    assert future_exception.handler == handler
    assert future_exception.exceptions == (ValueError, KeyError)
    mock_apply_exception_handler.assert_called_once_with(future_exception)
