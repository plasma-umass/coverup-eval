# file sanic/mixins/exceptions.py:6-39
# lines [11]
# branches []

import pytest
from sanic.mixins.exceptions import ExceptionMixin

class FutureException:
    def __init__(self, handler, exceptions):
        self.handler = handler
        self.exceptions = exceptions

@pytest.fixture
def exception_mixin():
    return ExceptionMixin()

def test_apply_exception_handler_not_implemented(exception_mixin):
    with pytest.raises(NotImplementedError):
        exception_mixin._apply_exception_handler(FutureException(None, (Exception,)))

def test_exception_decorator_apply_false_does_not_raise(exception_mixin):
    @exception_mixin.exception(Exception, apply=False)
    def handler():
        pass

    assert handler in (future_exception.handler for future_exception in exception_mixin._future_exceptions)

def test_exception_decorator_apply_true_raises_not_implemented(exception_mixin):
    with pytest.raises(NotImplementedError):
        @exception_mixin.exception(Exception, apply=True)
        def handler():
            pass
