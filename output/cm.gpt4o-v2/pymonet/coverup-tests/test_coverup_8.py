# file: pymonet/maybe.py:166-177
# asked: {"lines": [166, 173, 175, 176, 177], "branches": [[175, 176], [175, 177]]}
# gained: {"lines": [166, 173, 175, 176, 177], "branches": [[175, 176], [175, 177]]}

import pytest
from pymonet.maybe import Maybe
from pymonet.validation import Validation

class TestMaybeToValidation:
    
    def test_to_validation_with_nothing(self):
        maybe = Maybe.nothing()
        validation = maybe.to_validation()
        assert validation == Validation.success(None)
    
    def test_to_validation_with_value(self):
        value = 42
        maybe = Maybe.just(value)
        validation = maybe.to_validation()
        assert validation == Validation.success(value)
