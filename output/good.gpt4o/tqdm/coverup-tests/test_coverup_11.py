# file tqdm/rich.py:78-113
# lines [78, 88, 89, 91, 92, 93, 95, 96, 98, 99, 100, 101, 102, 104, 105, 106, 107, 108, 109, 111, 112, 113]
# branches ['95->96', '95->98', '100->101', '100->111']

import pytest
from unittest.mock import patch, MagicMock
from tqdm.rich import tqdm_rich
from tqdm import TqdmExperimentalWarning
from rich.progress import Progress, BarColumn, TextColumn, TimeElapsedColumn, TimeRemainingColumn

@pytest.fixture
def mock_progress(mocker):
    mock_progress = mocker.patch('tqdm.rich.Progress', autospec=True)
    mock_progress.return_value.__enter__.return_value = mock_progress
    return mock_progress

def test_tqdm_rich_initialization(mocker, mock_progress):
    with patch('tqdm.rich.warn') as mock_warn:
        # Test with disable=False
        tr = tqdm_rich(disable=False)
        assert tr.disable is False
        mock_warn.assert_called_once_with("rich is experimental/alpha", TqdmExperimentalWarning, stacklevel=2)
        assert tr._prog == mock_progress.return_value
        assert tr._task_id is not None

        # Test with disable=True
        mock_warn.reset_mock()
        tr = tqdm_rich(disable=True)
        assert tr.disable is True
        mock_warn.assert_not_called()

def test_tqdm_rich_custom_progress(mocker, mock_progress):
    custom_progress = (
        "[progress.description]{task.description}",
        BarColumn(bar_width=None),
        "[", TimeElapsedColumn(), "<", TimeRemainingColumn(), "]"
    )
    tr = tqdm_rich(progress=custom_progress, disable=False)
    assert tr._prog == mock_progress.return_value
    assert tr._task_id is not None
    mock_progress.assert_called_once_with(*custom_progress, transient=not tr.leave)

@pytest.fixture(autouse=True)
def cleanup():
    yield
    # Cleanup code if necessary
