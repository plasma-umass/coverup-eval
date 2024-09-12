# file: pymonet/validation.py:111-122
# asked: {"lines": [111, 118, 120, 121, 122], "branches": [[120, 121], [120, 122]]}
# gained: {"lines": [111, 118, 120, 121, 122], "branches": [[120, 121], [120, 122]]}

import pytest
from pymonet.validation import Validation
from pymonet.maybe import Maybe

class TestValidation:
    
    def test_to_maybe_success(self):
        class SuccessValidation(Validation):
            def __init__(self, value):
                self.value = value
                self.errors = []

        validation = SuccessValidation("test_value")
        maybe = validation.to_maybe()
        
        assert maybe == Maybe.just("test_value")
    
    def test_to_maybe_failure(self):
        class FailureValidation(Validation):
            def __init__(self):
                self.errors = ["error"]

        validation = FailureValidation()
        maybe = validation.to_maybe()
        
        assert maybe == Maybe.nothing()
