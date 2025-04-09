# file pymonet/monad_try.py:107-114
# lines [107, 114]
# branches []

import pytest
from pymonet.monad_try import Try

def test_try_get():
    class Success(Try):
        def __init__(self, value):
            self.value = value

    class Failure(Try):
        def __init__(self, exception):
            self.exception = exception

    # Test Success case
    success_instance = Success(42)
    assert success_instance.get() == 42

    # Test Failure case
    failure_instance = Failure(ValueError("An error occurred"))
    with pytest.raises(AttributeError):
        failure_instance.get()
