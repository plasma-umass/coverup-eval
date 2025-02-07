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
    mock_instance.wasion = False
    mock_instance.leave = False
    mock_instance.get_lock.return_value.__enter__.return_value = True
    mock_instance.get_lock.return_value.__exit__.return_value = False
    mock_instance.mpl = MagicMock()
    mock_instance.plt = MagicMock()
    mock_instance.fig = MagicMock()
    mock_instance._instances = [mock_instance]
    mock_instance.toolbar = 'None'
    monkeypatch.setattr(tqdm_gui, '__init__', lambda x, *args, **kwargs: None)
    return mock_instance

def test_close_wasion_false_leave_false(mock_tqdm_gui):
    mock_tqdm_gui.wasion = False
    mock_tqdm_gui.leave = False
    tqdm_gui.close(mock_tqdm_gui)
    assert mock_tqdm_gui.disable is True
    mock_tqdm_gui.plt.ioff.assert_called_once()
    mock_tqdm_gui.plt.close.assert_called_once_with(mock_tqdm_gui.fig)

def test_close_wasion_false_leave_true(mock_tqdm_gui):
    mock_tqdm_gui.wasion = False
    mock_tqdm_gui.leave = True
    tqdm_gui.close(mock_tqdm_gui)
    assert mock_tqdm_gui.disable is True
    mock_tqdm_gui.plt.ioff.assert_called_once()
    mock_tqdm_gui.display.assert_called_once()

def test_close_wasion_true_leave_false(mock_tqdm_gui):
    mock_tqdm_gui.wasion = True
    mock_tqdm_gui.leave = False
    tqdm_gui.close(mock_tqdm_gui)
    assert mock_tqdm_gui.disable is True
    mock_tqdm_gui.plt.ioff.assert_not_called()
    mock_tqdm_gui.plt.close.assert_called_once_with(mock_tqdm_gui.fig)

def test_close_wasion_true_leave_true(mock_tqdm_gui):
    mock_tqdm_gui.wasion = True
    mock_tqdm_gui.leave = True
    tqdm_gui.close(mock_tqdm_gui)
    assert mock_tqdm_gui.disable is True
    mock_tqdm_gui.plt.ioff.assert_not_called()
    mock_tqdm_gui.display.assert_called_once()
