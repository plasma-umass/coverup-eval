# file: tqdm/rich.py:142-147
# asked: {"lines": [147], "branches": []}
# gained: {"lines": [147], "branches": []}

import pytest
from tqdm.rich import trrange
from tqdm.rich import tqdm_rich
from tqdm.utils import _range

def test_trrange():
    # Test with a simple range
    result = trrange(5)
    assert isinstance(result, tqdm_rich)
    assert list(result) == list(range(5))

    # Test with range and additional kwargs
    result = trrange(5, desc="Test")
    assert isinstance(result, tqdm_rich)
    assert result.desc == "Test"
    assert list(result) == list(range(5))

    # Test with multiple arguments
    result = trrange(1, 5, 2)
    assert isinstance(result, tqdm_rich)
    assert list(result) == list(range(1, 5, 2))

    # Test with multiple arguments and kwargs
    result = trrange(1, 5, 2, desc="Test")
    assert isinstance(result, tqdm_rich)
    assert result.desc == "Test"
    assert list(result) == list(range(1, 5, 2))
