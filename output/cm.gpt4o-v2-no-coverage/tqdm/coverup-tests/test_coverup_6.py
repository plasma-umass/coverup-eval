# file: tqdm/rich.py:124-127
# asked: {"lines": [124, 125, 126, 127], "branches": [[125, 126], [125, 127]]}
# gained: {"lines": [124, 125, 126, 127], "branches": [[125, 126], [125, 127]]}

import pytest
from unittest.mock import MagicMock
from tqdm.rich import tqdm_rich

@pytest.fixture
def mock_progress():
    mock_prog = MagicMock()
    mock_prog.update = MagicMock()
    return mock_prog

def test_display_with_prog(mock_progress, monkeypatch):
    # Create an instance of tqdm_rich with a mock progress
    tr = tqdm_rich(total=100)
    tr._prog = mock_progress
    tr._task_id = 1
    tr.n = 50
    tr.desc = "Test"

    # Call the display method
    tr.display()

    # Assert that the update method was called with the correct parameters
    mock_progress.update.assert_called_once_with(1, completed=50, description="Test")

def test_display_without_prog():
    # Create an instance of tqdm_rich without a progress
    tr = tqdm_rich(total=100)

    # Ensure _prog attribute does not exist
    if hasattr(tr, '_prog'):
        delattr(tr, '_prog')

    # Call the display method
    tr.display()

    # No assertion needed as we are just ensuring no exceptions are raised

