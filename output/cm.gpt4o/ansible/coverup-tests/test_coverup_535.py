# file lib/ansible/utils/helpers.py:25-34
# lines [25, 30, 31, 32, 34]
# branches ['30->31', '30->34']

import pytest
from ansible.utils.helpers import pct_to_int

def test_pct_to_int():
    # Test percentage conversion
    assert pct_to_int("50%", 100) == 50
    assert pct_to_int("0%", 100) == 1  # min_value should be applied
    assert pct_to_int("100%", 100) == 100

    # Test integer conversion
    assert pct_to_int("10", 100) == 10
    assert pct_to_int(10, 100) == 10

    # Test edge cases
    assert pct_to_int("0%", 0) == 1  # min_value should be applied
    assert pct_to_int("100%", 0) == 1  # min_value should be applied

    # Test non-string input
    assert pct_to_int(0, 100) == 0
    assert pct_to_int(1, 100) == 1

    # Test with min_value parameter
    assert pct_to_int("0%", 100, min_value=5) == 5
    assert pct_to_int("100%", 100, min_value=5) == 100
    assert pct_to_int("50%", 100, min_value=5) == 50
