# file: tqdm/contrib/itertools.py:14-36
# asked: {"lines": [14, 22, 23, 24, 25, 26, 27, 29, 30, 31, 32, 33, 34, 35, 36], "branches": [[30, 31], [30, 32], [34, 0], [34, 35]]}
# gained: {"lines": [14, 22, 23, 24, 25, 26, 27, 29, 30, 31, 32, 33, 34, 35, 36], "branches": [[30, 31], [30, 32], [34, 0], [34, 35]]}

import pytest
from tqdm.contrib.itertools import product
from unittest.mock import MagicMock

def test_product_with_len():
    iterables = ([1, 2], [3, 4])
    mock_tqdm = MagicMock()
    mock_tqdm.return_value.__enter__.return_value = mock_tqdm
    results = list(product(*iterables, tqdm_class=mock_tqdm))
    assert results == [(1, 3), (1, 4), (2, 3), (2, 4)]
    assert mock_tqdm.update.call_count == 4

def test_product_without_len():
    iterables = (iter([1, 2]), iter([3, 4]))
    mock_tqdm = MagicMock()
    mock_tqdm.return_value.__enter__.return_value = mock_tqdm
    results = list(product(*iterables, tqdm_class=mock_tqdm))
    assert results == [(1, 3), (1, 4), (2, 3), (2, 4)]
    assert mock_tqdm.update.call_count == 4

@pytest.fixture(autouse=True)
def cleanup(monkeypatch):
    yield
    monkeypatch.undo()
