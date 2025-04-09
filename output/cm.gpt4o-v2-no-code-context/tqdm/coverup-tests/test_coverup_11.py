# file: tqdm/gui.py:90-107
# asked: {"lines": [90, 91, 92, 94, 96, 97, 100, 102, 103, 104, 105, 107], "branches": [[91, 92], [91, 94], [102, 103], [102, 104], [104, 105], [104, 107]]}
# gained: {"lines": [90, 91, 92, 94, 96, 97, 100, 102, 103, 104, 105, 107], "branches": [[91, 92], [91, 94], [102, 103], [104, 105], [104, 107]]}

import pytest
from unittest.mock import MagicMock, patch

# Assuming tqdm_gui and std_tqdm are imported from tqdm.gui
from tqdm.gui import tqdm_gui

@pytest.fixture
def tqdm_gui_instance(monkeypatch):
    # Mocking necessary attributes and methods
    instance = tqdm_gui()
    instance.disable = False
    instance.get_lock = MagicMock()
    instance._instances = [instance]
    instance.mpl = MagicMock()
    instance.mpl.rcParams = {}
    instance.toolbar = 'toolbar'
    instance.wasion = False
    instance.plt = MagicMock()
    instance.leave = False
    instance.display = MagicMock()
    instance.fig = 'fig'
    
    yield instance

    # Clean up
    instance._instances = []
    instance.disable = True

def test_close_disable(tqdm_gui_instance):
    tqdm_gui_instance.disable = True
    tqdm_gui_instance.close()
    assert tqdm_gui_instance.disable is True

def test_close_enable(tqdm_gui_instance):
    tqdm_gui_instance.close()
    assert tqdm_gui_instance.disable is True
    tqdm_gui_instance.get_lock.assert_called_once()
    assert tqdm_gui_instance not in tqdm_gui_instance._instances
    assert tqdm_gui_instance.mpl.rcParams['toolbar'] == 'toolbar'
    tqdm_gui_instance.plt.ioff.assert_called_once()
    tqdm_gui_instance.plt.close.assert_called_once_with('fig')

def test_close_leave(tqdm_gui_instance):
    tqdm_gui_instance.leave = True
    tqdm_gui_instance.close()
    tqdm_gui_instance.display.assert_called_once()
    tqdm_gui_instance.plt.close.assert_not_called()
