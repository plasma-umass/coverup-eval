# file: tqdm/notebook.py:279-291
# asked: {"lines": [280, 281, 282, 285, 286, 288, 289, 291], "branches": [[280, 281], [280, 282], [285, 286], [285, 288], [288, 289], [288, 291]]}
# gained: {"lines": [280, 281, 282, 285, 286, 288, 289, 291], "branches": [[280, 281], [280, 282], [285, 286], [285, 288], [288, 289], [288, 291]]}

import pytest
from unittest.mock import MagicMock, patch
from tqdm.notebook import tqdm_notebook

@pytest.fixture
def mock_tqdm_notebook():
    with patch('tqdm.notebook.std_tqdm') as MockTqdm:
        yield MockTqdm

def test_close_disable(mock_tqdm_notebook):
    instance = tqdm_notebook(disable=True)
    instance.close = tqdm_notebook.close.__get__(instance)
    instance.close()
    assert not mock_tqdm_notebook.close.called

def test_close_total_less_than_n(mock_tqdm_notebook):
    instance = tqdm_notebook(total=10)
    instance.n = 5
    instance.disp = MagicMock()
    instance.close = tqdm_notebook.close.__get__(instance)
    instance.close()
    instance.disp.assert_called_once_with(bar_style='danger', check_delay=False)

def test_close_leave_true(mock_tqdm_notebook):
    instance = tqdm_notebook(total=10, leave=True)
    instance.n = 10
    instance.disp = MagicMock()
    instance.close = tqdm_notebook.close.__get__(instance)
    instance.close()
    instance.disp.assert_called_once_with(bar_style='success', check_delay=False)

def test_close_leave_false(mock_tqdm_notebook):
    instance = tqdm_notebook(total=10, leave=False)
    instance.n = 10
    instance.disp = MagicMock()
    instance.close = tqdm_notebook.close.__get__(instance)
    instance.close()
    instance.disp.assert_called_once_with(close=True, check_delay=False)
