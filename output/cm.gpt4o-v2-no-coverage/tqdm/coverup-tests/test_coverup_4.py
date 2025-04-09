# file: tqdm/rich.py:121-122
# asked: {"lines": [121, 122], "branches": []}
# gained: {"lines": [121, 122], "branches": []}

import pytest
from tqdm.rich import tqdm_rich
from unittest.mock import patch, MagicMock

@pytest.fixture
def mock_progress():
    with patch('tqdm.rich.Progress') as mock:
        yield mock

def test_tqdm_rich_init_disable(mock_progress):
    with patch('tqdm.rich.warn') as mock_warn:
        tr = tqdm_rich(disable=True)
        assert tr.disable is True
        mock_warn.assert_not_called()
        mock_progress.assert_not_called()

def test_tqdm_rich_init_enable(mock_progress):
    with patch('tqdm.rich.warn') as mock_warn:
        tr = tqdm_rich(disable=False)
        assert tr.disable is False
        mock_warn.assert_called_once()
        mock_progress.assert_called_once()

def test_tqdm_rich_clear():
    tr = tqdm_rich(disable=True)
    tr.clear()
    # No assertion needed as clear() does nothing
