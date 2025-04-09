# file: tqdm/_tqdm_pandas.py:7-24
# asked: {"lines": [12, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24], "branches": [[14, 16], [14, 21]]}
# gained: {"lines": [12, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24], "branches": [[14, 16], [14, 21]]}

import pytest
from unittest.mock import MagicMock, patch
from tqdm import TqdmDeprecationWarning
import sys

# Mock class to simulate tclass behavior
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

def test_tqdm_pandas_class(mock_tqdm_class, monkeypatch):
    from tqdm._tqdm_pandas import tqdm_pandas

    mock_warning = MagicMock()
    monkeypatch.setattr('tqdm.TqdmDeprecationWarning', mock_warning)

    tqdm_pandas(mock_tqdm_class, file=sys.stderr)
    
    mock_warning.assert_called_once_with(
        "Please use `tqdm.pandas(...)` instead of `tqdm_pandas(tqdm, ...)`.",
        fp_write=sys.stderr.write
    )

def test_tqdm_pandas_instance(mock_tqdm_instance, monkeypatch):
    from tqdm._tqdm_pandas import tqdm_pandas

    mock_warning = MagicMock()
    monkeypatch.setattr('tqdm.TqdmDeprecationWarning', mock_warning)

    tqdm_pandas(mock_tqdm_instance)
    
    mock_warning.assert_called_once_with(
        "Please use `tqdm.pandas(...)` instead of `tqdm_pandas(tqdm(...))`.",
        fp_write=sys.stderr.write
    )
