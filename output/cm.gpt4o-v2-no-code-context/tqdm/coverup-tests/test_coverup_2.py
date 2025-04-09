# file: tqdm/contrib/telegram.py:149-154
# asked: {"lines": [149, 154], "branches": []}
# gained: {"lines": [149, 154], "branches": []}

import pytest
from tqdm.contrib.telegram import tqdm as tqdm_telegram

def test_ttgrange(monkeypatch):
    from tqdm.contrib.telegram import ttgrange

    # Mock tqdm_telegram to verify it is called with the correct arguments
    def mock_tqdm_telegram(iterable, **kwargs):
        return list(iterable)  # Convert to list to force iteration

    monkeypatch.setattr('tqdm.contrib.telegram.tqdm_telegram', mock_tqdm_telegram)

    # Test with a range of numbers
    result = ttgrange(5)
    assert result == [0, 1, 2, 3, 4]

    # Test with additional keyword arguments
    result = ttgrange(3, desc="Test")
    assert result == [0, 1, 2]

    # Test with start, stop, and step arguments
    result = ttgrange(1, 5, 2)
    assert result == [1, 3]
