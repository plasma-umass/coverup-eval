# file lib/ansible/module_utils/urls.py:1169-1183
# lines [1169, 1177, 1178, 1179, 1180, 1181, 1182, 1183]
# branches []

import pytest
from ansible.module_utils.urls import rfc2822_date_string

def test_rfc2822_date_string():
    timetuple = (2001, 11, 9, 1, 8, 47, 4)  # Corresponds to Fri, 09 Nov 2001 01:08:47
    zone = '-0000'
    expected_date_string = 'Fri, 09 Nov 2001 01:08:47 -0000'
    
    result = rfc2822_date_string(timetuple, zone)
    
    assert result == expected_date_string, f"Expected {expected_date_string} but got {result}"

    # Test with a different timezone
    zone = '+0200'
    expected_date_string = 'Fri, 09 Nov 2001 01:08:47 +0200'
    
    result = rfc2822_date_string(timetuple, zone)
    
    assert result == expected_date_string, f"Expected {expected_date_string} but got {result}"

    # Test with default timezone
    expected_date_string = 'Fri, 09 Nov 2001 01:08:47 -0000'
    
    result = rfc2822_date_string(timetuple)
    
    assert result == expected_date_string, f"Expected {expected_date_string} but got {result}"
