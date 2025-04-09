# file: tqdm/notebook.py:205-208
# asked: {"lines": [205, 206, 207, 208], "branches": [[207, 0], [207, 208]]}
# gained: {"lines": [205, 206, 207, 208], "branches": [[207, 0], [207, 208]]}

import pytest
from unittest.mock import MagicMock, patch
from tqdm.notebook import tqdm_notebook
from IPython.display import display

@pytest.fixture
def mock_container():
    class MockContainer:
        def __init__(self):
            self.children = [MagicMock(), MagicMock(), MagicMock()]
    return MockContainer()

def test_tqdm_notebook_colour_setter(mock_container):
    # Create an instance of tqdm_notebook with necessary parameters
    with patch('tqdm.notebook.tqdm_notebook.status_printer', return_value=mock_container), \
         patch('IPython.display.display', new=MagicMock()):
        bar = tqdm_notebook(total=10, colour='blue')
    
    # Set the colour and verify the change
    new_colour = 'red'
    bar.colour = new_colour
    assert bar.container.children[-2].style.bar_color == new_colour

    # Clean up
    del bar
