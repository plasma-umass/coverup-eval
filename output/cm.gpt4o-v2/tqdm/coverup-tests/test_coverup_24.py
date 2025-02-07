# file: tqdm/notebook.py:279-291
# asked: {"lines": [282, 285, 286, 288, 289, 291], "branches": [[280, 282], [285, 286], [285, 288], [288, 289], [288, 291]]}
# gained: {"lines": [282, 285, 286, 288, 289, 291], "branches": [[280, 282], [285, 286], [285, 288], [288, 289], [288, 291]]}

import pytest
from tqdm.notebook import tqdm_notebook

@pytest.fixture
def tqdm_instance():
    return tqdm_notebook(total=100, leave=True)

def test_close_disable(tqdm_instance, mocker):
    mocker.patch.object(tqdm_instance, 'disable', True)
    tqdm_instance.close()
    assert tqdm_instance.disable is True

def test_close_with_error(tqdm_instance, mocker):
    mocker.patch.object(tqdm_instance, 'n', 50)
    mocker.patch.object(tqdm_instance, 'total', 100)
    mock_disp = mocker.patch.object(tqdm_instance, 'disp')
    tqdm_instance.close()
    mock_disp.assert_called_once_with(bar_style='danger', check_delay=False)

def test_close_leave(tqdm_instance, mocker):
    mocker.patch.object(tqdm_instance, 'n', 100)
    mocker.patch.object(tqdm_instance, 'total', 100)
    mock_disp = mocker.patch.object(tqdm_instance, 'disp')
    tqdm_instance.close()
    mock_disp.assert_called_once_with(bar_style='success', check_delay=False)

def test_close_no_leave(tqdm_instance, mocker):
    mocker.patch.object(tqdm_instance, 'n', 100)
    mocker.patch.object(tqdm_instance, 'total', 100)
    mocker.patch.object(tqdm_instance, 'leave', False)
    mock_disp = mocker.patch.object(tqdm_instance, 'disp')
    tqdm_instance.close()
    mock_disp.assert_called_once_with(close=True, check_delay=False)
