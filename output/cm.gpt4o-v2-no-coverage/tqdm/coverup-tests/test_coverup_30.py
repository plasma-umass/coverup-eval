# file: tqdm/notebook.py:279-291
# asked: {"lines": [282, 285, 286, 288, 289, 291], "branches": [[280, 282], [285, 286], [285, 288], [288, 289], [288, 291]]}
# gained: {"lines": [282, 285, 286, 288, 289, 291], "branches": [[280, 282], [285, 286], [285, 288], [288, 289], [288, 291]]}

import pytest
from unittest.mock import MagicMock, patch
from tqdm.notebook import tqdm_notebook

@pytest.fixture
def mock_display():
    with patch.object(tqdm_notebook, 'display', autospec=True) as mock_display:
        yield mock_display

def test_tqdm_notebook_close_disable(mock_display):
    # Arrange
    tqdm = tqdm_notebook(disable=True)
    
    # Act
    tqdm.close()
    
    # Assert
    mock_display.assert_not_called()

def test_tqdm_notebook_close_no_error(mock_display):
    # Arrange
    tqdm = tqdm_notebook(total=100, leave=True)
    tqdm.n = 100
    
    # Act
    mock_display.reset_mock()
    tqdm.close()
    
    # Assert
    mock_display.assert_called_with(tqdm, bar_style='success', check_delay=False)

def test_tqdm_notebook_close_with_error(mock_display):
    # Arrange
    tqdm = tqdm_notebook(total=100, leave=True)
    tqdm.n = 50
    
    # Act
    mock_display.reset_mock()
    tqdm.close()
    
    # Assert
    mock_display.assert_called_with(tqdm, bar_style='danger', check_delay=False)

def test_tqdm_notebook_close_no_leave(mock_display):
    # Arrange
    tqdm = tqdm_notebook(total=100, leave=False)
    tqdm.n = 100
    
    # Act
    mock_display.reset_mock()
    tqdm.close()
    
    # Assert
    mock_display.assert_called_with(tqdm, close=True, check_delay=False)
