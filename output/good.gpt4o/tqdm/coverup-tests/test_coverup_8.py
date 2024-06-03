# file tqdm/gui.py:26-28
# lines [26, 27]
# branches []

import pytest
from unittest.mock import patch, MagicMock
from tqdm.gui import tqdm_gui
from tqdm import tqdm as std_tqdm

@pytest.fixture
def mock_tqdm_gui(mocker):
    mocker.patch('tqdm.gui.std_tqdm', autospec=True)
    mocker.patch('tqdm.gui.tqdm_gui.__init__', return_value=None)
    return tqdm_gui

def test_tqdm_gui_initialization(mock_tqdm_gui):
    instance = mock_tqdm_gui()
    assert isinstance(instance, std_tqdm)

def test_tqdm_gui_write_method(mock_tqdm_gui):
    with patch.object(mock_tqdm_gui, 'write', autospec=True) as mock_write:
        instance = mock_tqdm_gui()
        instance.write("Test message")
        mock_write.assert_called_once_with(instance, "Test message")
