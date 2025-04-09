# file: tqdm/notebook.py:200-203
# asked: {"lines": [], "branches": [[202, 0]]}
# gained: {"lines": [], "branches": [[202, 0]]}

import pytest
from unittest.mock import MagicMock
from tqdm.notebook import tqdm_notebook

def test_tqdm_notebook_colour_property():
    # Create a mock container with the expected structure
    mock_container = MagicMock()
    mock_container.children = [MagicMock(), MagicMock()]
    mock_container.children[-2].style.bar_color = 'blue'

    # Instantiate tqdm_notebook and set the mock container
    tqdm = tqdm_notebook(disable=True)
    tqdm.container = mock_container

    # Assert that the colour property returns the correct value
    assert tqdm.colour == 'blue'

    # Clean up
    del tqdm

def test_tqdm_notebook_no_container():
    # Instantiate tqdm_notebook without a container
    tqdm = tqdm_notebook(disable=True)

    # Assert that the colour property returns None when there is no container
    assert tqdm.colour is None

    # Clean up
    del tqdm
