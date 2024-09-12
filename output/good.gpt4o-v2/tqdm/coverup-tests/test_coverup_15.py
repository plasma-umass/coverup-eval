# file: tqdm/rich.py:129-139
# asked: {"lines": [129, 137, 138, 139], "branches": [[137, 138], [137, 139]]}
# gained: {"lines": [129, 137, 138, 139], "branches": [[137, 138], [137, 139]]}

import pytest
from unittest.mock import MagicMock
from tqdm.rich import tqdm_rich

@pytest.fixture
def mock_progress():
    mock_prog = MagicMock()
    return mock_prog

def test_tqdm_rich_reset_with_prog(mock_progress, monkeypatch):
    # Create an instance of tqdm_rich with a mocked progress
    bar = tqdm_rich(total=100)
    monkeypatch.setattr(bar, '_prog', mock_progress)
    
    # Call reset and check if _prog.reset is called
    bar.reset(total=50)
    mock_progress.reset.assert_called_once_with(total=50)
    assert bar.total == 50

def test_tqdm_rich_reset_without_prog(monkeypatch):
    # Create an instance of tqdm_rich without a mocked progress
    bar = tqdm_rich(total=100)
    
    # Ensure _prog is not set
    monkeypatch.delattr(bar, '_prog', raising=False)
    
    # Call reset and check if it falls back to the superclass method
    bar.reset(total=50)
    assert bar.total == 50
