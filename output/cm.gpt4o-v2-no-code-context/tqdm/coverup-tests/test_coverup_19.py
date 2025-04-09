# file: tqdm/contrib/itertools.py:14-36
# asked: {"lines": [14, 22, 23, 24, 25, 26, 27, 29, 30, 31, 32, 33, 34, 35, 36], "branches": [[30, 31], [30, 32], [34, 0], [34, 35]]}
# gained: {"lines": [14, 22, 23, 24, 25, 26, 27, 29, 30, 31, 32, 33, 34, 35, 36], "branches": [[30, 31], [30, 32], [34, 0], [34, 35]]}

import pytest
from unittest import mock
from tqdm.contrib.itertools import product
import itertools
from tqdm import tqdm as tqdm_auto

def test_product_with_len():
    iterables = [[1, 2], [3, 4]]
    result = list(product(*iterables))
    expected = list(itertools.product(*iterables))
    assert result == expected

def test_product_without_len():
    iterables = [iter([1, 2]), iter([3, 4])]
    result = list(product(*iterables))
    expected = list(itertools.product([1, 2], [3, 4]))  # Recreate the iterables for expected
    assert result == expected

def test_product_with_custom_tqdm_class(monkeypatch):
    class MockTqdm:
        def __init__(self, **kwargs):
            self.kwargs = kwargs
            self.total = kwargs.get('total', None)
            self.updated = 0

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            pass

        def update(self):
            self.updated += 1

    monkeypatch.setattr('tqdm.contrib.itertools.tqdm_auto', MockTqdm)
    iterables = [[1, 2], [3, 4]]
    result = list(product(*iterables, tqdm_class=MockTqdm))
    expected = list(itertools.product(*iterables))
    assert result == expected

def test_product_with_empty_iterable():
    iterables = [[], [1, 2, 3]]
    result = list(product(*iterables))
    expected = list(itertools.product(*iterables))
    assert result == expected
