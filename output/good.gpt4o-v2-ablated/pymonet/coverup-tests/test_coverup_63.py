# file: pymonet/monad_try.py:107-114
# asked: {"lines": [107, 114], "branches": []}
# gained: {"lines": [107, 114], "branches": []}

import pytest
from pymonet.monad_try import Try

class TestTry:
    def test_get_success(self):
        class Success(Try):
            def __init__(self, value):
                self.value = value

        success_instance = Success(10)
        assert success_instance.get() == 10

    def test_get_failure(self):
        class Failure(Try):
            def __init__(self, exception):
                self.value = exception

        failure_instance = Failure(ValueError("An error occurred"))
        assert isinstance(failure_instance.get(), ValueError)
        assert str(failure_instance.get()) == "An error occurred"
