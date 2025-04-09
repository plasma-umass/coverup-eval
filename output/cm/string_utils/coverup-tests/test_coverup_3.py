# file string_utils/generation.py:41-60
# lines [41, 53, 54, 56, 57, 58, 60]
# branches ['53->54', '53->56']

import pytest
from string_utils.generation import random_string
import string

def test_random_string_size_type_error():
    with pytest.raises(ValueError) as excinfo:
        random_string(0)
    assert str(excinfo.value) == 'size must be >= 1'

    with pytest.raises(ValueError) as excinfo:
        random_string(-1)
    assert str(excinfo.value) == 'size must be >= 1'

    with pytest.raises(ValueError) as excinfo:
        random_string('a')
    assert str(excinfo.value) == 'size must be >= 1'

def test_random_string_output_length():
    size = 10
    result = random_string(size)
    assert len(result) == size
    assert all(c in string.ascii_letters + string.digits for c in result)
