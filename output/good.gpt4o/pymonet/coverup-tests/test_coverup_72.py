# file pymonet/lazy.py:151-160
# lines [151, 158, 160]
# branches []

import pytest
from pymonet.lazy import Lazy
from pymonet.validation import Validation

class MockLazy(Lazy):
    def __init__(self):
        super().__init__(lambda: "mocked_value")
    
    def get(self, *args):
        return "mocked_value"

def test_lazy_to_validation(mocker):
    # Arrange
    lazy_instance = MockLazy()
    
    # Act
    validation_result = lazy_instance.to_validation()
    
    # Assert
    assert isinstance(validation_result, Validation)
    assert validation_result.is_success()
    assert validation_result.value == "mocked_value"
