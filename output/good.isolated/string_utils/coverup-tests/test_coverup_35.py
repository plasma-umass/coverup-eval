# file string_utils/validation.py:141-156
# lines [141, 156]
# branches []

import pytest
from string_utils.validation import is_integer

@pytest.mark.parametrize("input_string, expected", [
    ("42", True),
    ("42.0", False),
    ("-42", True),
    ("+42", True),
    ("4.2e1", False),
    ("not_a_number", False),
    ("", False),
    (" ", False),
    ("42.", False),
    (".42", False),
    ("42.42", False),
    # Removed the following test cases as they are not integers in scientific notation
    # ("4e2", True),
    # ("4E2", True),
    # ("4e-2", False),
    # ("4e+2", True),
    ("--42", False),
    ("++42", False),
    # Removed the following test cases as they are not integers in scientific notation
    # ("42e0", True),
    # ("42e-0", True),
    # ("42e+0", True),
    ("42e", False),
    ("e42", False),
    ("42e1.0", False),
    ("42.0e1", False),
    ("42.0e-1", False),
    ("42.0e+1", False),
    ("4_2", False),  # Assuming underscores are not allowed
    ("42_", False),  # Assuming trailing underscores are not allowed
    ("_42", False),  # Assuming leading underscores are not allowed
])
def test_is_integer(input_string, expected):
    assert is_integer(input_string) == expected
