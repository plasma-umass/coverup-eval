# file tqdm/notebook.py:205-208
# lines [207, 208]
# branches ['207->exit', '207->208']

import pytest
from unittest.mock import Mock, patch
from tqdm.notebook import tqdm_notebook

@pytest.fixture
def mock_tqdm_notebook():
    with patch('tqdm.notebook.tqdm_notebook.status_printer') as mock_status_printer:
        mock_status_printer.return_value = Mock()
        with patch('tqdm.notebook.tqdm_notebook.__init__', return_value=None) as mock_init:
            yield tqdm_notebook

def test_tqdm_notebook_colour_setter(mock_tqdm_notebook):
    # Create a mock for the container and its children
    mock_container = Mock()
    mock_child = Mock()
    mock_child.style.bar_color = None
    mock_container.children = [Mock(), mock_child]
    
    # Instantiate tqdm_notebook and set the container attribute
    instance = mock_tqdm_notebook()
    instance.container = mock_container
    
    # Set the colour property, which should trigger the setter
    test_color = 'blue'
    instance.colour = test_color
    
    # Assert that the colour was set correctly
    assert instance.container.children[-2].style.bar_color == test_color
