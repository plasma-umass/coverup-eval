# file pymonet/monad_try.py:19-20
# lines [19, 20]
# branches []

import pytest
from pymonet.monad_try import Try

def test_try_str_method():
    class SuccessTry(Try):
        def __init__(self, value):
            self.value = value
            self.is_success = True

    class FailureTry(Try):
        def __init__(self, value):
            self.value = value
            self.is_success = False

    success_try = SuccessTry("success_value")
    failure_try = FailureTry("failure_value")

    assert str(success_try) == 'Try[value=success_value, is_success=True]'
    assert str(failure_try) == 'Try[value=failure_value, is_success=False]'
