# file: tqdm/notebook.py:200-203
# asked: {"lines": [], "branches": [[202, 0]]}
# gained: {"lines": [], "branches": [[202, 0]]}

import pytest
from unittest.mock import MagicMock

# Assuming tqdm_notebook is imported from tqdm.notebook
from tqdm.notebook import tqdm_notebook

@pytest.fixture
def mock_container():
    container = MagicMock()
    container.children = [MagicMock(), MagicMock()]
    container.children[-2].style.bar_color = 'blue'
    return container

def test_tqdm_notebook_colour_with_container(mock_container):
    # Create an instance of tqdm_notebook
    tqdm_instance = tqdm_notebook()
    # Assign the mock container to the instance
    tqdm_instance.container = mock_container
    
    # Assert that the colour property returns the expected value
    assert tqdm_instance.colour == 'blue'

def test_tqdm_notebook_colour_without_container(monkeypatch):
    # Create an instance of tqdm_notebook without a container
    tqdm_instance = tqdm_notebook()
    
    # Use monkeypatch to remove the 'container' attribute if it exists
    monkeypatch.delattr(tqdm_instance, 'container', raising=False)
    
    # Assert that accessing the colour property returns None
    assert tqdm_instance.colour is None
