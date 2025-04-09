# file: pymonet/validation.py:98-109
# asked: {"lines": [98, 105, 107, 108, 109], "branches": [[107, 108], [107, 109]]}
# gained: {"lines": [98, 105, 107, 108, 109], "branches": [[107, 108], [107, 109]]}

import pytest
from pymonet.validation import Validation
from pymonet.either import Left, Right

class TestValidation:
    def test_to_either_success(self, mocker):
        # Create a Validation instance with success state
        validation = Validation(value='success_value', errors=[])
        mocker.patch.object(validation, 'is_success', return_value=True)
        
        result = validation.to_either()
        
        assert isinstance(result, Right)
        assert result.value == 'success_value'

    def test_to_either_failure(self, mocker):
        # Create a Validation instance with failure state
        validation = Validation(value=None, errors=['error1', 'error2'])
        mocker.patch.object(validation, 'is_success', return_value=False)
        
        result = validation.to_either()
        
        assert isinstance(result, Left)
        assert result.value == ['error1', 'error2']
