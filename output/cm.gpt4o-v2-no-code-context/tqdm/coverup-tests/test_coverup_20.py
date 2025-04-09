# file: tqdm/gui.py:90-107
# asked: {"lines": [], "branches": [[102, 104]]}
# gained: {"lines": [], "branches": [[102, 104]]}

import pytest
from unittest.mock import MagicMock, patch
from tqdm.gui import tqdm_gui

@pytest.fixture
def mock_tqdm_gui(monkeypatch):
    mock_instance = MagicMock(spec=tqdm_gui)
    mock_instance.disable = False
    mock_instance.leave = False
    mock_instance.wasion = False
    mock_instance.get_lock.return_value.__enter__.return_value = None
    mock_instance.get_lock.return_value.__exit__.return_value = None
    mock_instance._instances = [mock_instance]
    
    # Mock mpl and plt attributes
    mock_instance.mpl = MagicMock()
    mock_instance.mpl.rcParams = {'toolbar': 'original'}
    mock_instance.toolbar = 'original'
    mock_instance.plt = MagicMock()
    mock_instance.fig = MagicMock()
    
    return mock_instance

def test_close_disable(mock_tqdm_gui):
    mock_tqdm_gui.disable = True
    tqdm_gui.close(mock_tqdm_gui)
    assert mock_tqdm_gui.disable is True
    assert mock_tqdm_gui._instances == [mock_tqdm_gui]

def test_close_wasion(mock_tqdm_gui):
    mock_tqdm_gui.wasion = True
    tqdm_gui.close(mock_tqdm_gui)
    assert mock_tqdm_gui.plt.ioff.call_count == 0

def test_close_leave(mock_tqdm_gui):
    mock_tqdm_gui.leave = True
    tqdm_gui.close(mock_tqdm_gui)
    assert mock_tqdm_gui.display.call_count == 1

def test_close_no_leave(mock_tqdm_gui):
    tqdm_gui.close(mock_tqdm_gui)
    assert mock_tqdm_gui.plt.close.call_count == 1
    assert mock_tqdm_gui.plt.close.call_args[0][0] == mock_tqdm_gui.fig

def test_close_full(mock_tqdm_gui):
    tqdm_gui.close(mock_tqdm_gui)
    assert mock_tqdm_gui.disable is True
    assert mock_tqdm_gui._instances == []
    assert mock_tqdm_gui.mpl.rcParams['toolbar'] == 'original'
    assert mock_tqdm_gui.plt.ioff.call_count == 1
    assert mock_tqdm_gui.plt.close.call_count == 1
    assert mock_tqdm_gui.plt.close.call_args[0][0] == mock_tqdm_gui.fig
