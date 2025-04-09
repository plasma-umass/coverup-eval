# file: tqdm/rich.py:129-139
# asked: {"lines": [129, 137, 138, 139], "branches": [[137, 138], [137, 139]]}
# gained: {"lines": [129, 137, 138, 139], "branches": [[137, 138], [137, 139]]}

import pytest
from unittest.mock import MagicMock, patch

# Assuming tqdm_rich is imported from tqdm/rich.py
from tqdm.rich import tqdm_rich

@pytest.fixture
def mock_tqdm_rich():
    with patch('tqdm.rich.Progress') as MockProgress:
        mock_prog = MockProgress.return_value
        instance = tqdm_rich()
        instance._prog = mock_prog
        yield instance, mock_prog

def test_reset_with_total(mock_tqdm_rich):
    instance, mock_prog = mock_tqdm_rich
    total = 100

    instance.reset(total=total)

    mock_prog.reset.assert_called_once_with(total=total)
    assert instance.n == 0

def test_reset_without_total(mock_tqdm_rich):
    instance, mock_prog = mock_tqdm_rich

    instance.reset()

    mock_prog.reset.assert_called_once_with(total=None)
    assert instance.n == 0

def test_reset_no_prog(monkeypatch):
    with patch('tqdm.rich.Progress') as MockProgress:
        instance = tqdm_rich()
        monkeypatch.delattr(instance, '_prog', raising=False)

        instance.reset(total=50)

        assert instance.n == 0
