# file: tqdm/auto.py:38-42
# asked: {"lines": [38, 42], "branches": []}
# gained: {"lines": [38, 42], "branches": []}

import pytest
from tqdm.auto import trange, tqdm

def test_trange_executes_all_lines(monkeypatch):
    # Mock tqdm to ensure our trange function is called
    def mock_tqdm(iterable, **kwargs):
        return list(iterable)
    
    monkeypatch.setattr('tqdm.auto.tqdm', mock_tqdm)

    # Test with a simple range
    result = trange(5)
    assert result == [0, 1, 2, 3, 4]

    # Test with a range and additional tqdm parameters
    result = trange(5, desc="Test")
    assert result == [0, 1, 2, 3, 4]

    # Test with a range and step
    result = trange(0, 10, 2)
    assert result == [0, 2, 4, 6, 8]

    # Test with a range, step, and additional tqdm parameters
    result = trange(0, 10, 2, desc="Test")
    assert result == [0, 2, 4, 6, 8]
