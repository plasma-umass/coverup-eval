# file: tqdm/rich.py:129-139
# asked: {"lines": [129, 137, 138, 139], "branches": [[137, 138], [137, 139]]}
# gained: {"lines": [129, 137, 138, 139], "branches": [[137, 138], [137, 139]]}

import pytest
from unittest.mock import MagicMock
from tqdm.rich import tqdm_rich

@pytest.fixture
def mock_progress():
    mock_prog = MagicMock()
    mock_prog.reset = MagicMock()
    return mock_prog

@pytest.fixture
def mock_tqdm_rich(monkeypatch, mock_progress):
    # Mock the Progress class to avoid initialization issues
    monkeypatch.setattr("tqdm.rich.Progress", lambda *args, **kwargs: mock_progress)
    tr = tqdm_rich(disable=False, total=100)
    return tr

def test_tqdm_rich_reset_with_prog(mock_tqdm_rich, mock_progress):
    tr = mock_tqdm_rich
    
    # Call reset with a specific total
    tr.reset(total=100)
    
    # Assert that the progress bar's reset method was called with the correct total
    mock_progress.reset.assert_called_once_with(total=100)
    
    # Assert that the parent class's reset method was also called
    assert tr.total == 100

def test_tqdm_rich_reset_without_prog(monkeypatch):
    # Create an instance of tqdm_rich without a progress bar
    tr = tqdm_rich(disable=False, total=100)
    
    # Ensure _prog attribute does not exist
    if hasattr(tr, '_prog'):
        delattr(tr, '_prog')
    
    # Call reset with a specific total
    tr.reset(total=100)
    
    # Assert that the parent class's reset method was called
    assert tr.total == 100
