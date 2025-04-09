# file: tqdm/rich.py:115-119
# asked: {"lines": [115, 116, 117, 118, 119], "branches": [[116, 117], [116, 118]]}
# gained: {"lines": [115, 116, 117, 118, 119], "branches": [[116, 117], [116, 118]]}

import pytest
from unittest.mock import MagicMock, patch
from tqdm.rich import tqdm_rich

@pytest.fixture
def mock_progress():
    with patch('tqdm.rich.Progress') as MockProgress:
        yield MockProgress

def test_tqdm_rich_close(mock_progress):
    # Create an instance of tqdm_rich with disable=False
    tr = tqdm_rich(disable=False)
    tr._prog = MagicMock()
    
    # Call the close method
    tr.close()
    
    # Assert that the parent's close method was called
    tr._prog.__exit__.assert_called_once_with(None, None, None)

def test_tqdm_rich_close_disabled(mock_progress):
    # Create an instance of tqdm_rich with disable=True
    tr = tqdm_rich(disable=True)
    tr._prog = MagicMock()
    
    # Call the close method
    tr.close()
    
    # Assert that the parent's close method was not called
    tr._prog.__exit__.assert_not_called()
