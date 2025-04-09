# file: string_utils/generation.py:41-60
# asked: {"lines": [41, 53, 54, 56, 57, 58, 60], "branches": [[53, 54], [53, 56]]}
# gained: {"lines": [41, 53, 54, 56, 57, 58, 60], "branches": [[53, 54], [53, 56]]}

import pytest
import string
import string_utils.generation as gen

def test_random_string_valid_size():
    result = gen.random_string(10)
    assert isinstance(result, str)
    assert len(result) == 10
    assert all(c in (string.ascii_letters + string.digits) for c in result)

def test_random_string_invalid_size_zero():
    with pytest.raises(ValueError, match="size must be >= 1"):
        gen.random_string(0)

def test_random_string_invalid_size_negative():
    with pytest.raises(ValueError, match="size must be >= 1"):
        gen.random_string(-5)

def test_random_string_invalid_size_non_integer():
    with pytest.raises(ValueError, match="size must be >= 1"):
        gen.random_string("ten")
