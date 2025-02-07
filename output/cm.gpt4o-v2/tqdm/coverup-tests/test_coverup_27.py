# file: tqdm/notebook.py:149-198
# asked: {"lines": [159, 160, 162, 163, 164, 166, 167, 169, 171, 172, 174, 177, 179, 180, 183, 186, 187, 190, 191, 192, 193, 194, 196, 197, 198], "branches": [[159, 160], [159, 166], [169, 171], [169, 183], [171, 172], [171, 174], [179, 180], [179, 183], [183, 186], [183, 190], [186, 187], [186, 190], [190, 191], [190, 196], [196, 0], [196, 197]]}
# gained: {"lines": [159, 160, 162, 163, 164, 166, 167, 169, 171, 172, 174, 177, 179, 180, 183, 186, 187, 190, 191, 192, 193, 194, 196, 197, 198], "branches": [[159, 160], [159, 166], [169, 171], [169, 183], [171, 172], [171, 174], [179, 180], [183, 186], [183, 190], [186, 187], [190, 191], [190, 196], [196, 0], [196, 197]]}

import pytest
from unittest.mock import MagicMock, patch
from tqdm.notebook import tqdm_notebook

@pytest.fixture
def mock_container():
    ltext = MagicMock()
    pbar = MagicMock()
    rtext = MagicMock()
    container = MagicMock()
    container.children = [ltext, pbar, rtext]
    return container, ltext, pbar, rtext

def test_display_no_msg_no_close(mock_container):
    container, ltext, pbar, rtext = mock_container
    tn = tqdm_notebook(total=100)
    tn.container = container
    tn.n = 50
    tn.bar_format = '{l_bar}{bar}{r_bar}'
    tn.format_meter = MagicMock(return_value='formatted_meter')
    
    tn.display()
    
    tn.format_meter.assert_called_once()
    assert pbar.value == 50

def test_display_with_msg(mock_container):
    container, ltext, pbar, rtext = mock_container
    tn = tqdm_notebook(total=100)
    tn.container = container
    tn.n = 50
    
    tn.display(msg='test message')
    
    assert ltext.value == ''
    assert rtext.value == 'test message'

def test_display_with_bar(mock_container):
    container, ltext, pbar, rtext = mock_container
    tn = tqdm_notebook(total=100)
    tn.container = container
    tn.n = 50
    
    tn.display(msg='left<bar/>right')
    
    assert ltext.value == 'left'
    assert rtext.value == 'right'

def test_display_with_bar_style(mock_container):
    container, ltext, pbar, rtext = mock_container
    tn = tqdm_notebook(total=100)
    tn.container = container
    tn.n = 50
    
    tn.display(bar_style='success')
    
    assert pbar.bar_style == 'success'

def test_display_close(mock_container):
    container, ltext, pbar, rtext = mock_container
    tn = tqdm_notebook(total=100)
    tn.container = container
    tn.n = 50
    
    tn.display(close=True)
    
    container.close.assert_called_once()

def test_display_close_with_exception(mock_container):
    container, ltext, pbar, rtext = mock_container
    tn = tqdm_notebook(total=100)
    tn.container = container
    tn.n = 50
    del container.close
    tn.container.visible = True
    
    tn.display(close=True)
    
    assert not tn.container.visible

@patch('tqdm.notebook.display')
def test_display_check_delay(mock_display, mock_container):
    container, ltext, pbar, rtext = mock_container
    tn = tqdm_notebook(total=100, delay=1)
    tn.container = container
    tn.n = 50
    tn.displayed = False
    
    tn.display(check_delay=True)
    
    mock_display.assert_called_once_with(container)
    assert tn.displayed
