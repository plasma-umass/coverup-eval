# file: tqdm/rich.py:78-113
# asked: {"lines": [], "branches": [[100, 111]]}
# gained: {"lines": [], "branches": [[100, 111]]}

import pytest
from unittest.mock import patch, MagicMock
from tqdm.std import TqdmExperimentalWarning
from rich.progress import Progress, BarColumn, TimeElapsedColumn, TimeRemainingColumn
from tqdm.rich import tqdm_rich

@pytest.fixture
def mock_progress():
    with patch('tqdm.rich.Progress', autospec=True) as mock:
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
        mock_warn.assert_called_once_with("rich is experimental/alpha", TqdmExperimentalWarning, stacklevel=2)
        mock_progress.assert_called_once()

def test_tqdm_rich_progress_none(mock_progress):
    with patch('tqdm.rich.warn') as mock_warn:
        tr = tqdm_rich(disable=False, progress=None)
        assert tr.disable is False
        mock_warn.assert_called_once_with("rich is experimental/alpha", TqdmExperimentalWarning, stacklevel=2)
        mock_progress.assert_called_once()
        assert isinstance(tr._prog, Progress)

def test_tqdm_rich_custom_progress(mock_progress):
    custom_progress = ("custom",)
    with patch('tqdm.rich.warn') as mock_warn:
        tr = tqdm_rich(disable=False, progress=custom_progress)
        assert tr.disable is False
        mock_warn.assert_called_once_with("rich is experimental/alpha", TqdmExperimentalWarning, stacklevel=2)
        mock_progress.assert_called_once_with(*custom_progress, transient=not tr.leave)
        assert isinstance(tr._prog, Progress)
