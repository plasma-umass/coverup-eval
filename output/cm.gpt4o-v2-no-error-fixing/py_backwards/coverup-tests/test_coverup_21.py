# file: py_backwards/utils/helpers.py:12-17
# asked: {"lines": [12, 13, 14, 15, 17], "branches": []}
# gained: {"lines": [12, 13, 14, 15, 17], "branches": []}

import pytest
from typing import Iterable, List, Any, Callable
from functools import wraps

# Assuming the eager function is defined in py_backwards/utils/helpers.py
from py_backwards.utils.helpers import eager

def test_eager_decorator():
    # Define a sample generator function to use with the eager decorator
    def sample_gen(n: int) -> Iterable[int]:
        for i in range(n):
            yield i

    # Apply the eager decorator to the sample generator function
    eager_sample_gen = eager(sample_gen)

    # Test the decorated function
    result = eager_sample_gen(5)
    
    # Verify the result is a list and contains the expected values
    assert isinstance(result, list)
    assert result == [0, 1, 2, 3, 4]

    # Test with an empty generator
    result = eager_sample_gen(0)
    assert isinstance(result, list)
    assert result == []

    # Test with a different range
    result = eager_sample_gen(3)
    assert isinstance(result, list)
    assert result == [0, 1, 2]

@pytest.fixture(autouse=True)
def run_around_tests(monkeypatch):
    # Setup: (if needed, e.g., patching)
    yield
    # Teardown: (cleanup if necessary)
