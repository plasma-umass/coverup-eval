# file string_utils/generation.py:41-60
# lines [41, 53, 54, 56, 57, 58, 60]
# branches ['53->54', '53->56']

import pytest
import string
import random
from string_utils.generation import random_string

def test_random_string_valid_size():
    result = random_string(10)
    assert len(result) == 10
    assert all(c in string.ascii_letters + string.digits for c in result)

def test_random_string_invalid_size_negative():
    with pytest.raises(ValueError, match='size must be >= 1'):
        random_string(-1)

def test_random_string_invalid_size_zero():
    with pytest.raises(ValueError, match='size must be >= 1'):
        random_string(0)

def test_random_string_invalid_size_non_integer():
    with pytest.raises(ValueError, match='size must be >= 1'):
        random_string('a')

@pytest.fixture(autouse=True)
def mock_random_choice(mocker):
    mocker.patch('random.choice', side_effect=lambda x: x[0])
