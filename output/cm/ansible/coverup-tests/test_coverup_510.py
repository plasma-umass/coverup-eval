# file lib/ansible/module_utils/urls.py:1169-1183
# lines [1169, 1177, 1178, 1179, 1180, 1181, 1182, 1183]
# branches []

import pytest
from ansible.module_utils.urls import rfc2822_date_string
from time import gmtime

def test_rfc2822_date_string():
    # Create a fixed time tuple
    fixed_time_tuple = (2023, 4, 1, 12, 30, 45, 5)
    # Expected format: 'Sat, 01 Apr 2023 12:30:45 -0000'
    expected_date_string = 'Sat, 01 Apr 2023 12:30:45 -0000'
    
    # Call the function with the fixed time tuple
    result = rfc2822_date_string(fixed_time_tuple)
    
    # Assert the result matches the expected date string
    assert result == expected_date_string

    # Test with a different timezone
    zone = '+0200'
    expected_date_string_with_zone = 'Sat, 01 Apr 2023 12:30:45 +0200'
    result_with_zone = rfc2822_date_string(fixed_time_tuple, zone)
    
    # Assert the result matches the expected date string with timezone
    assert result_with_zone == expected_date_string_with_zone

# Note: No cleanup is necessary for this test as it does not modify any external state.
