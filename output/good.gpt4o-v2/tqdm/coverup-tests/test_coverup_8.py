# file: tqdm/rich.py:124-127
# asked: {"lines": [124, 125, 126, 127], "branches": [[125, 126], [125, 127]]}
# gained: {"lines": [124, 125, 127], "branches": [[125, 127]]}

import pytest
from unittest.mock import MagicMock
from tqdm.rich import tqdm_rich

@pytest.fixture
def tqdm_rich_instance(monkeypatch):
    # Mock the Progress class to avoid side effects during testing
    mock_progress = MagicMock()
    monkeypatch.setattr("tqdm.rich.Progress", mock_progress)
    
    instance = tqdm_rich()
    instance._prog = MagicMock()
    instance._task_id = 1
    instance.n = 5
    instance.desc = "Test"
    return instance

def test_display_with_prog(tqdm_rich_instance):
    tqdm_rich_instance.display()
    tqdm_rich_instance._prog.update.assert_called_once_with(1, completed=5, description="Test")

def test_display_without_prog(monkeypatch):
    # Mock the Progress class to avoid side effects during testing
    mock_progress = MagicMock()
    monkeypatch.setattr("tqdm.rich.Progress", mock_progress)
    
    instance = tqdm_rich()
    instance.display()
    # No assertion needed, just ensuring no exception is raised
