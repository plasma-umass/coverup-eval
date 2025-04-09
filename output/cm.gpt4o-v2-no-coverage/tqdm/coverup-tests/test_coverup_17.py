# file: tqdm/gui.py:90-107
# asked: {"lines": [90, 91, 92, 94, 96, 97, 100, 102, 103, 104, 105, 107], "branches": [[91, 92], [91, 94], [102, 103], [102, 104], [104, 105], [104, 107]]}
# gained: {"lines": [90, 91, 92, 94, 96, 97, 100, 102, 103, 104, 105, 107], "branches": [[91, 92], [91, 94], [102, 103], [104, 105], [104, 107]]}

import pytest
from unittest.mock import MagicMock, patch
from tqdm.gui import tqdm_gui

@pytest.fixture
def mock_tqdm_gui():
    with patch('tqdm.gui.tqdm_gui.__init__', lambda x, *args, **kwargs: None):
        instance = tqdm_gui()
        instance.disable = False
        instance.get_lock = MagicMock()
        instance._instances = MagicMock()
        instance.mpl = MagicMock()
        instance.plt = MagicMock()
        instance.leave = False
        instance.fig = MagicMock()
        instance.wasion = False
        instance.toolbar = 'None'
        instance.mpl.rcParams = {'toolbar': 'None'}
        return instance

def test_close_disable(mock_tqdm_gui):
    mock_tqdm_gui.disable = True
    mock_tqdm_gui.close()
    assert mock_tqdm_gui.disable is True

def test_close_enable(mock_tqdm_gui):
    mock_tqdm_gui.close()

    assert mock_tqdm_gui.disable is True
    mock_tqdm_gui.get_lock.assert_called_once()
    mock_tqdm_gui._instances.remove.assert_called_once_with(mock_tqdm_gui)
    assert mock_tqdm_gui.mpl.rcParams['toolbar'] == 'None'
    mock_tqdm_gui.plt.ioff.assert_called_once()
    mock_tqdm_gui.plt.close.assert_called_once_with(mock_tqdm_gui.fig)

def test_close_leave(mock_tqdm_gui):
    mock_tqdm_gui.leave = True
    mock_tqdm_gui.display = MagicMock()

    mock_tqdm_gui.close()

    assert mock_tqdm_gui.disable is True
    mock_tqdm_gui.get_lock.assert_called_once()
    mock_tqdm_gui._instances.remove.assert_called_once_with(mock_tqdm_gui)
    assert mock_tqdm_gui.mpl.rcParams['toolbar'] == 'None'
    mock_tqdm_gui.plt.ioff.assert_called_once()
    mock_tqdm_gui.display.assert_called_once()
