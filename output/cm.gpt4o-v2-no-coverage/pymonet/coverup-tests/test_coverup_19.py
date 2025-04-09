# file: pymonet/validation.py:98-109
# asked: {"lines": [98, 105, 107, 108, 109], "branches": [[107, 108], [107, 109]]}
# gained: {"lines": [98, 105, 107, 108, 109], "branches": [[107, 108], [107, 109]]}

import pytest
from pymonet.either import Left, Right
from pymonet.validation import Validation

class TestValidation:
    
    @pytest.fixture
    def validation_success(self):
        class MockValidation(Validation):
            def __init__(self):
                self.value = "success"
                self.errors = []
                
            def is_success(self):
                return True
        
        return MockValidation()
    
    @pytest.fixture
    def validation_failure(self):
        class MockValidation(Validation):
            def __init__(self):
                self.value = None
                self.errors = ["error"]
                
            def is_success(self):
                return False
        
        return MockValidation()
    
    def test_to_either_success(self, validation_success):
        result = validation_success.to_either()
        assert isinstance(result, Right)
        assert result.value == "success"
    
    def test_to_either_failure(self, validation_failure):
        result = validation_failure.to_either()
        assert isinstance(result, Left)
        assert result.value == ["error"]
