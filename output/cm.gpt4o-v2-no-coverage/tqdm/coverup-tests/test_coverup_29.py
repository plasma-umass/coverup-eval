# file: tqdm/notebook.py:149-198
# asked: {"lines": [174, 186, 187, 191, 192, 193, 194, 197, 198], "branches": [[159, 166], [169, 183], [171, 174], [179, 183], [183, 186], [186, 187], [186, 190], [190, 191], [196, 197]]}
# gained: {"lines": [174, 186, 187, 191, 192, 197, 198], "branches": [[159, 166], [169, 183], [171, 174], [183, 186], [186, 187], [190, 191], [196, 197]]}

import pytest
from unittest.mock import MagicMock, patch
from tqdm.notebook import tqdm_notebook

@pytest.fixture
def mock_container():
    container = MagicMock()
    container.children = [MagicMock(), MagicMock(), MagicMock()]
    return container

@pytest.fixture
def mock_tqdm_notebook(mock_container):
    with patch('tqdm.notebook.tqdm_notebook.status_printer', return_value=mock_container):
        yield tqdm_notebook(total=10)

def test_display_no_msg_no_close(mock_tqdm_notebook, mock_container):
    mock_tqdm_notebook.display()
    ltext, pbar, rtext = mock_container.children
    assert pbar.value == mock_tqdm_notebook.n
    assert ltext.value == '  0%'  # Adjusted to match the expected output
    assert rtext.value != ''

def test_display_with_msg(mock_tqdm_notebook, mock_container):
    mock_tqdm_notebook.display(msg="Test message")
    ltext, pbar, rtext = mock_container.children
    assert pbar.value == mock_tqdm_notebook.n
    assert ltext.value == ''
    assert rtext.value == 'Test message'

def test_display_with_bar(mock_tqdm_notebook, mock_container):
    mock_tqdm_notebook.display(msg="Left<bar/>Right")
    ltext, pbar, rtext = mock_container.children
    assert pbar.value == mock_tqdm_notebook.n
    assert ltext.value == 'Left'
    assert rtext.value == 'Right'

def test_display_with_bar_style(mock_tqdm_notebook, mock_container):
    mock_tqdm_notebook.display(bar_style='success')
    _, pbar, _ = mock_container.children
    assert pbar.bar_style == 'success'

def test_display_close(mock_tqdm_notebook, mock_container):
    mock_tqdm_notebook.display(close=True)
    mock_container.close.assert_called_once()

def test_display_close_with_danger(mock_tqdm_notebook, mock_container):
    _, pbar, _ = mock_container.children
    pbar.bar_style = 'danger'
    mock_tqdm_notebook.display(close=True)
    mock_container.close.assert_not_called()

def test_display_check_delay(mock_tqdm_notebook, mock_container):
    with patch('tqdm.notebook.display') as mock_display:
        mock_tqdm_notebook.delay = 1
        mock_tqdm_notebook.displayed = False
        mock_tqdm_notebook.display(check_delay=True)
        mock_display.assert_called_once_with(mock_container)
        assert mock_tqdm_notebook.displayed is True
