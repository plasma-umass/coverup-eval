# file: pymonet/monad_try.py:19-20
# asked: {"lines": [19, 20], "branches": []}
# gained: {"lines": [19, 20], "branches": []}

import pytest
from pymonet.monad_try import Try

class TestTry:
    def test_try_str_success(self):
        # Create a mock Try class with the necessary attributes
        class MockSuccessTry(Try):
            def __init__(self):
                self.value = 42
                self.is_success = True

        # Create an instance of the mock class
        try_instance = MockSuccessTry()
        
        # Verify the string representation
        assert str(try_instance) == 'Try[value=42, is_success=True]'

    def test_try_str_failure(self):
        # Create a mock Try class with the necessary attributes
        class MockFailureTry(Try):
            def __init__(self):
                self.value = "error"
                self.is_success = False

        # Create an instance of the mock class
        try_instance = MockFailureTry()
        
        # Verify the string representation
        assert str(try_instance) == 'Try[value=error, is_success=False]'
