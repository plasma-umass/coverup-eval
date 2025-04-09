# file: pymonet/validation.py:16-19
# asked: {"lines": [16, 17, 18, 19], "branches": [[17, 18], [17, 19]]}
# gained: {"lines": [16, 17, 18, 19], "branches": [[17, 18], [17, 19]]}

import pytest
from pymonet.validation import Validation

class TestValidation:
    
    def test_validation_str_success(self, mocker):
        # Mock the is_success method to return True
        validation = Validation(value='test_value', errors=None)
        mocker.patch.object(validation, 'is_success', return_value=True)
        
        result = str(validation)
        
        assert result == 'Validation.success[test_value]'
    
    def test_validation_str_fail(self, mocker):
        # Mock the is_success method to return False
        validation = Validation(value='test_value', errors='test_errors')
        mocker.patch.object(validation, 'is_success', return_value=False)
        
        result = str(validation)
        
        assert result == 'Validation.fail[test_value, test_errors]'
