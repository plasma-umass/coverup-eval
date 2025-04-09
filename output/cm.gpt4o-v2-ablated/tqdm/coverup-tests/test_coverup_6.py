# file: tqdm/gui.py:109-110
# asked: {"lines": [110], "branches": []}
# gained: {"lines": [110], "branches": []}

import pytest
from tqdm.gui import tqdm_gui

@pytest.fixture
def tqdm_instance():
    return tqdm_gui()

def test_tqdm_gui_clear(tqdm_instance):
    # Call the clear method and assert it does not raise any exceptions
    tqdm_instance.clear()
    assert True  # If no exception is raised, the test passes
