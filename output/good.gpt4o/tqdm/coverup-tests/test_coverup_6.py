# file tqdm/rich.py:129-139
# lines [129, 137, 138, 139]
# branches ['137->138', '137->139']

import pytest
from unittest.mock import MagicMock, patch
from tqdm.rich import tqdm_rich

@pytest.fixture
def mock_prog():
    return MagicMock()

@pytest.fixture
def tqdm_rich_instance(mock_prog):
    with patch('tqdm.rich.Progress') as MockProgress:
        MockProgress.return_value = mock_prog
        instance = tqdm_rich()
        instance._prog = mock_prog
        return instance

def test_tqdm_rich_reset_with_total(tqdm_rich_instance, mock_prog):
    total = 100
    tqdm_rich_instance.reset(total=total)
    mock_prog.reset.assert_called_once_with(total=total)
    assert tqdm_rich_instance.n == 0

def test_tqdm_rich_reset_without_total(tqdm_rich_instance, mock_prog):
    tqdm_rich_instance.reset()
    mock_prog.reset.assert_called_once_with(total=None)
    assert tqdm_rich_instance.n == 0

def test_tqdm_rich_reset_no_prog():
    with patch('tqdm.rich.Progress') as MockProgress:
        instance = tqdm_rich()
        with patch.object(instance, 'reset', wraps=instance.reset) as mock_reset:
            instance.reset(total=50)
            mock_reset.assert_called_once_with(total=50)
            assert instance.n == 0
