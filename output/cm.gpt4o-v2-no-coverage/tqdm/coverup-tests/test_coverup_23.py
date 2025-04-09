# file: tqdm/auto.py:38-42
# asked: {"lines": [42], "branches": []}
# gained: {"lines": [42], "branches": []}

import pytest
from tqdm.auto import tqdm, trange

def test_trange(monkeypatch):
    # Mock tqdm to track calls and arguments
    def mock_tqdm(iterable, **kwargs):
        mock_tqdm.called = True
        mock_tqdm.iterable = iterable
        mock_tqdm.kwargs = kwargs
        return list(iterable)  # Simulate tqdm by returning the list

    monkeypatch.setattr('tqdm.auto.tqdm', mock_tqdm)

    # Test trange with positional arguments
    result = trange(5)
    assert mock_tqdm.called
    assert mock_tqdm.iterable == range(5)
    assert result == list(range(5))

    # Test trange with keyword arguments
    result = trange(5, desc="Test")
    assert mock_tqdm.called
    assert mock_tqdm.iterable == range(5)
    assert mock_tqdm.kwargs['desc'] == "Test"
    assert result == list(range(5))

    # Test trange with start, stop, step
    result = trange(1, 5, 2)
    assert mock_tqdm.called
    assert mock_tqdm.iterable == range(1, 5, 2)
    assert result == list(range(1, 5, 2))
