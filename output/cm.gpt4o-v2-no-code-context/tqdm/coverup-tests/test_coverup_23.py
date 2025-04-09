# file: tqdm/rich.py:115-119
# asked: {"lines": [117], "branches": [[116, 117]]}
# gained: {"lines": [117], "branches": [[116, 117]]}

import pytest
from unittest.mock import MagicMock, patch

# Assuming tqdm_rich is imported from the module where it is defined
from tqdm.rich import tqdm_rich

@pytest.fixture
def mock_tqdm_rich(monkeypatch):
    mock_prog = MagicMock()
    mock_instance = tqdm_rich(disable=True)
    mock_instance._prog = mock_prog
    monkeypatch.setattr(mock_instance, 'disable', True)
    return mock_instance

def test_tqdm_rich_close_disable(mock_tqdm_rich):
    mock_tqdm_rich.close()
    assert not mock_tqdm_rich._prog.__exit__.called

@pytest.fixture
def mock_tqdm_rich_enabled(monkeypatch):
    mock_prog = MagicMock()
    with patch('tqdm.rich.Progress') as MockProgress:
        MockProgress.return_value = mock_prog
        mock_instance = tqdm_rich(disable=False)
        mock_instance._prog = mock_prog
        monkeypatch.setattr(mock_instance, 'disable', False)
        return mock_instance

def test_tqdm_rich_close_enabled(mock_tqdm_rich_enabled):
    mock_tqdm_rich_enabled.close()
    assert mock_tqdm_rich_enabled._prog.__exit__.called
