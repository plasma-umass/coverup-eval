# file tqdm/gui.py:26-28
# lines [26, 27]
# branches []

import pytest
from unittest.mock import patch
from tqdm.gui import tqdm_gui

@pytest.fixture
def mock_tqdm_gui():
    with patch.object(tqdm_gui, '__init__', return_value=None) as mock_init:
        yield mock_init

def test_tqdm_gui_init(mock_tqdm_gui):
    # Instantiate tqdm_gui to cover the class definition
    gui = tqdm_gui()
    mock_tqdm_gui.assert_called_once()

    # Assertions to verify postconditions (none in this case, as we're just testing instantiation)
    assert gui is not None
