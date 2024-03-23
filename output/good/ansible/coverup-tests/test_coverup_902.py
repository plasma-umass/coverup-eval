# file lib/ansible/plugins/filter/core.py:87-88
# lines [87, 88]
# branches []

import pytest
import datetime
from ansible.plugins.filter.core import to_datetime

# Test function to cover to_datetime function
def test_to_datetime():
    test_string = "2023-01-01 12:00:00"
    expected_datetime = datetime.datetime(2023, 1, 1, 12, 0, 0)
    
    # Test with default format
    assert to_datetime(test_string) == expected_datetime
    
    # Test with custom format
    test_string_custom_format = "01/01/2023 12-00-00"
    custom_format = "%d/%m/%Y %H-%M-%S"
    assert to_datetime(test_string_custom_format, custom_format) == expected_datetime
