# file: tqdm/contrib/itertools.py:14-36
# asked: {"lines": [14, 22, 23, 24, 25, 26, 27, 29, 30, 31, 32, 33, 34, 35, 36], "branches": [[30, 31], [30, 32], [34, 0], [34, 35]]}
# gained: {"lines": [14, 22, 23, 24, 25, 26, 27, 29, 30, 31, 32, 33, 34, 35, 36], "branches": [[30, 31], [30, 32], [34, 0], [34, 35]]}

import pytest
from unittest import mock
from tqdm.contrib.itertools import product
import itertools
from tqdm import tqdm as tqdm_auto

def test_product_basic():
    result = list(product([1, 2], [3, 4]))
    expected = list(itertools.product([1, 2], [3, 4]))
    assert result == expected

def test_product_with_tqdm_class(monkeypatch):
    mock_tqdm = mock.MagicMock()
    monkeypatch.setattr('tqdm.contrib.itertools.tqdm_auto', mock_tqdm)
    
    result = list(product([1, 2], [3, 4], tqdm_class=mock_tqdm))
    expected = list(itertools.product([1, 2], [3, 4]))
    assert result == expected
    assert mock_tqdm.call_count == 1

def test_product_with_empty_iterable():
    result = list(product([], [1, 2, 3]))
    expected = list(itertools.product([], [1, 2, 3]))
    assert result == expected

def test_product_with_non_sized_iterable():
    def generator():
        yield 1
        yield 2

    result = list(product(generator(), [3, 4]))
    expected = list(itertools.product(generator(), [3, 4]))
    assert result == expected

def test_product_with_total_calculation(monkeypatch):
    mock_tqdm = mock.MagicMock()
    monkeypatch.setattr('tqdm.contrib.itertools.tqdm_auto', mock_tqdm)
    
    result = list(product([1, 2], [3, 4], tqdm_class=mock_tqdm))
    expected = list(itertools.product([1, 2], [3, 4]))
    assert result == expected
    assert mock_tqdm.call_args[1]['total'] == 4

def test_product_with_kwargs(monkeypatch):
    mock_tqdm = mock.MagicMock()
    monkeypatch.setattr('tqdm.contrib.itertools.tqdm_auto', mock_tqdm)
    
    result = list(product([1, 2], [3, 4], tqdm_class=mock_tqdm, desc="Test"))
    expected = list(itertools.product([1, 2], [3, 4]))
    assert result == expected
    assert mock_tqdm.call_args[1]['desc'] == "Test"
