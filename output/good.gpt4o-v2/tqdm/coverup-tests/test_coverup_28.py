# file: tqdm/contrib/itertools.py:14-36
# asked: {"lines": [14, 22, 23, 24, 25, 26, 27, 29, 30, 31, 32, 33, 34, 35, 36], "branches": [[30, 31], [30, 32], [34, 0], [34, 35]]}
# gained: {"lines": [14, 22, 23, 24, 25, 26, 27, 29, 30, 31, 32, 33, 34, 35, 36], "branches": [[30, 31], [30, 32], [34, 0], [34, 35]]}

import pytest
from tqdm.contrib.itertools import product
from tqdm.auto import tqdm as tqdm_auto
import itertools

def test_product_with_lengths(monkeypatch):
    # Mock tqdm to avoid actual progress bar display
    class MockTqdm:
        def __init__(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs
            self.updated = False

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            pass

        def update(self):
            self.updated = True

    monkeypatch.setattr(tqdm_auto, '__call__', MockTqdm)

    iterables = ([1, 2], [3, 4])
    result = list(product(*iterables))
    assert result == [(1, 3), (1, 4), (2, 3), (2, 4)]

def test_product_without_lengths(monkeypatch):
    # Mock tqdm to avoid actual progress bar display
    class MockTqdm:
        def __init__(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs
            self.updated = False

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            pass

        def update(self):
            self.updated = True

    monkeypatch.setattr(tqdm_auto, '__call__', MockTqdm)

    iterables = (iter([1, 2]), iter([3, 4]))
    result = list(product(*iterables))
    assert result == [(1, 3), (1, 4), (2, 3), (2, 4)]

def test_product_with_custom_tqdm_class(monkeypatch):
    # Custom tqdm class
    class CustomTqdm:
        def __init__(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs
            self.updated = False

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            pass

        def update(self):
            self.updated = True

    iterables = ([1, 2], [3, 4])
    result = list(product(*iterables, tqdm_class=CustomTqdm))
    assert result == [(1, 3), (1, 4), (2, 3), (2, 4)]
