# file py_backwards/utils/helpers.py:32-36
# lines [32, 34, 35, 36]
# branches []

import pytest
from py_backwards.utils.helpers import get_source

# Test function to be used for getting source
def dummy_function():
    a = 1
    b = 2
    return a + b

# Expected source of the dummy_function without padding
expected_source = "def dummy_function():\n    a = 1\n    b = 2\n    return a + b"

def test_get_source():
    # Test get_source with a simple function
    source = get_source(dummy_function)
    assert source.strip() == expected_source.strip()

# Run the test
if __name__ == "__main__":
    pytest.main()
