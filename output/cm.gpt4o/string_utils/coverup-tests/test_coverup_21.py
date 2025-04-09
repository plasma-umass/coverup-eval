# file string_utils/validation.py:368-390
# lines [368, 385, 387, 388, 390]
# branches ['387->388', '387->390']

import pytest
from string_utils.validation import is_uuid

def test_is_uuid():
    # Test valid UUID
    assert is_uuid('6f8aa2f9-686c-4ac3-8766-5712354a04cf') == True
    
    # Test invalid UUID
    assert is_uuid('6f8aa2f9686c4ac387665712354a04cf') == False
    
    # Test valid UUID hex representation with allow_hex=True
    assert is_uuid('6f8aa2f9686c4ac387665712354a04cf', allow_hex=True) == True
    
    # Test invalid UUID hex representation with allow_hex=False
    assert is_uuid('6f8aa2f9686c4ac387665712354a04cf', allow_hex=False) == False
    
    # Test invalid input (not a UUID)
    assert is_uuid('not-a-uuid') == False
    
    # Test invalid input with allow_hex=True
    assert is_uuid('not-a-uuid', allow_hex=True) == False

    # Test empty string
    assert is_uuid('') == False
    
    # Test None input
    assert is_uuid(None) == False
    
    # Test integer input
    assert is_uuid(123456) == False
    
    # Test valid UUID with uppercase letters
    assert is_uuid('6F8AA2F9-686C-4AC3-8766-5712354A04CF') == True
    
    # Test valid UUID hex representation with uppercase letters and allow_hex=True
    assert is_uuid('6F8AA2F9686C4AC387665712354A04CF', allow_hex=True) == True
