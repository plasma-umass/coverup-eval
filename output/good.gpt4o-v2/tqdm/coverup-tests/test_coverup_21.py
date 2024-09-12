# file: tqdm/notebook.py:200-203
# asked: {"lines": [202, 203], "branches": [[202, 0], [202, 203]]}
# gained: {"lines": [202, 203], "branches": [[202, 203]]}

import pytest
from unittest.mock import MagicMock
from tqdm.notebook import tqdm_notebook

def test_tqdm_notebook_colour_property():
    # Create a mock container with the necessary structure
    mock_container = MagicMock()
    mock_container.children = [MagicMock(), MagicMock()]
    mock_container.children[-2].style.bar_color = 'blue'

    # Create an instance of tqdm_notebook and set the mock container
    tqdm_instance = tqdm_notebook()
    tqdm_instance.container = mock_container

    # Access the colour property to trigger the lines in question
    assert tqdm_instance.colour == 'blue'

    # Clean up
    del tqdm_instance

