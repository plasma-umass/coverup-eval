# file: tqdm/_tqdm_pandas.py:7-24
# asked: {"lines": [12, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24], "branches": [[14, 16], [14, 21]]}
# gained: {"lines": [12, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24], "branches": [[14, 16], [14, 21]]}

import pytest
import sys
from unittest.mock import MagicMock, patch
from tqdm import TqdmDeprecationWarning
from tqdm._tqdm_pandas import tqdm_pandas

class MockTqdm:
    @staticmethod
    def pandas(**kwargs):
        pass

class MockTqdmInstance:
    def __init__(self):
        self.fp = sys.stderr

    @staticmethod
    def pandas(deprecated_t):
        pass

@pytest.fixture
def mock_tqdm_class():
    return MockTqdm

@pytest.fixture
def mock_tqdm_instance():
    return MockTqdmInstance()

def test_tqdm_pandas_with_class(mock_tqdm_class, monkeypatch):
    mock_warning = MagicMock()
    monkeypatch.setattr('tqdm.TqdmDeprecationWarning', mock_warning)
    tqdm_pandas(mock_tqdm_class)
    mock_warning.assert_called_once_with(
        'Please use `tqdm.pandas(...)` instead of `tqdm_pandas(tqdm, ...)`.',
        fp_write=sys.stderr.write
    )

def test_tqdm_pandas_with_instance(mock_tqdm_instance, monkeypatch):
    mock_warning = MagicMock()
    monkeypatch.setattr('tqdm.TqdmDeprecationWarning', mock_warning)
    tqdm_pandas(mock_tqdm_instance)
    mock_warning.assert_called_once_with(
        'Please use `tqdm.pandas(...)` instead of `tqdm_pandas(tqdm(...))`.',
        fp_write=sys.stderr.write
    )
