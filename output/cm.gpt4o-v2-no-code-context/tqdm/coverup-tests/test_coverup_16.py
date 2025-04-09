# file: tqdm/gui.py:109-110
# asked: {"lines": [110], "branches": []}
# gained: {"lines": [110], "branches": []}

import pytest
from tqdm.gui import tqdm_gui

def test_tqdm_gui_clear():
    # Create an instance of tqdm_gui
    gui = tqdm_gui()

    # Call the clear method
    gui.clear()

    # Assert that the clear method does not raise any exceptions
    assert True
