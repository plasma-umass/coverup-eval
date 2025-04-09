# file pysnooper/pycompat.py:90-97
# lines [91, 92, 93, 95, 96, 97]
# branches []

import pytest
from datetime import timedelta as timedelta_module
from unittest import mock

# Assuming the function timedelta_parse is imported from pysnooper.pycompat
from pysnooper.pycompat import timedelta_parse

def test_timedelta_parse():
    # Test case to cover lines 91-97
    input_str = "1:2:3.4"
    expected_result = timedelta_module(hours=1, minutes=2, seconds=3, microseconds=4)
    
    result = timedelta_parse(input_str)
    
    assert result == expected_result

    # Clean up if necessary (not needed in this case as no external state is modified)
