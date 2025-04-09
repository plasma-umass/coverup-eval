# file sanic/mixins/exceptions.py:6-39
# lines [6, 7, 8, 10, 11, 13, 26, 30, 31, 33, 34, 35, 36, 37, 39]
# branches ['30->31', '30->33', '35->36', '35->37']

import pytest
from sanic.mixins.exceptions import ExceptionMixin

class FutureException:
    def __init__(self, handler, exceptions):
        self.handler = handler
        self.exceptions = exceptions

@pytest.fixture
def exception_mixin():
    return ExceptionMixin()

def test_exception_decorator_apply_false(mocker, exception_mixin):
    mock_apply_exception_handler = mocker.patch.object(
        exception_mixin, '_apply_exception_handler'
    )

    @exception_mixin.exception(Exception, apply=False)
    def handler():
        pass

    assert handler in [fe.handler for fe in exception_mixin._future_exceptions]
    mock_apply_exception_handler.assert_not_called()

def test_exception_decorator_with_list_of_exceptions(mocker, exception_mixin):
    mock_apply_exception_handler = mocker.patch.object(
        exception_mixin, '_apply_exception_handler'
    )

    @exception_mixin.exception([ValueError, KeyError])
    def handler():
        pass

    assert handler in [fe.handler for fe in exception_mixin._future_exceptions]
    assert any(ValueError in fe.exceptions for fe in exception_mixin._future_exceptions)
    assert any(KeyError in fe.exceptions for fe in exception_mixin._future_exceptions)
    mock_apply_exception_handler.assert_called_once()
