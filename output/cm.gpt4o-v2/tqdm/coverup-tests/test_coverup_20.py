# file: tqdm/notebook.py:205-208
# asked: {"lines": [207, 208], "branches": [[207, 0], [207, 208]]}
# gained: {"lines": [207, 208], "branches": [[207, 0], [207, 208]]}

import pytest
from unittest.mock import MagicMock
from tqdm.notebook import tqdm_notebook

def test_tqdm_notebook_colour_setter():
    # Create a mock container with children
    mock_container = MagicMock()
    mock_container.children = [MagicMock(), MagicMock()]
    
    # Create an instance of tqdm_notebook with the mock container
    tqdm_instance = tqdm_notebook(total=10)
    tqdm_instance.container = mock_container
    
    # Set the colour and check if the bar_color is set correctly
    tqdm_instance.colour = 'red'
    assert mock_container.children[-2].style.bar_color == 'red'
    
    # Clean up
    del tqdm_instance

