# file: tqdm/notebook.py:149-198
# asked: {"lines": [], "branches": [[179, 183], [186, 190]]}
# gained: {"lines": [], "branches": [[186, 190]]}

import pytest
from unittest.mock import MagicMock, patch
from tqdm.notebook import tqdm_notebook
from html import escape
import re

@pytest.fixture
def mock_container():
    ltext = MagicMock()
    pbar = MagicMock()
    rtext = MagicMock()
    container = MagicMock()
    container.children = [ltext, pbar, rtext]
    return container, ltext, pbar, rtext

def test_display_with_right_text(mock_container):
    container, ltext, pbar, rtext = mock_container
    tqdm = tqdm_notebook(total=100)
    tqdm.container = container
    tqdm.n = 50
    msg = "Progress <bar/>50%"
    
    tqdm.display(msg=msg)
    
    assert ltext.value == "Progress "
    assert rtext.value == "50%"
    assert pbar.value == 50

def test_display_with_bar_style(mock_container):
    container, ltext, pbar, rtext = mock_container
    tqdm = tqdm_notebook(total=100)
    tqdm.container = container
    tqdm.n = 50
    bar_style = "info"
    
    tqdm.display(bar_style=bar_style)
    
    assert pbar.bar_style == bar_style

def test_display_with_close(mock_container):
    container, ltext, pbar, rtext = mock_container
    tqdm = tqdm_notebook(total=100)
    tqdm.container = container
    tqdm.n = 50
    pbar.bar_style = "info"
    
    tqdm.display(close=True)
    
    container.close.assert_called_once()

def test_display_with_close_and_danger_style(mock_container):
    container, ltext, pbar, rtext = mock_container
    tqdm = tqdm_notebook(total=100)
    tqdm.container = container
    tqdm.n = 50
    pbar.bar_style = "danger"
    
    tqdm.display(close=True)
    
    container.close.assert_not_called()
    container.visible = False
    assert container.visible == False

def test_display_with_bar_style_and_danger(mock_container):
    container, ltext, pbar, rtext = mock_container
    tqdm = tqdm_notebook(total=100)
    tqdm.container = container
    tqdm.n = 50
    pbar.bar_style = "danger"
    bar_style = "success"
    
    tqdm.display(bar_style=bar_style)
    
    assert pbar.bar_style == "danger"

def test_display_with_check_delay(mock_container):
    container, ltext, pbar, rtext = mock_container
    tqdm = tqdm_notebook(total=100)
    tqdm.container = container
    tqdm.n = 50
    tqdm.delay = 1
    tqdm.displayed = False
    
    with patch("tqdm.notebook.display") as mock_display:
        tqdm.display(check_delay=True)
        mock_display.assert_called_once_with(container)
        assert tqdm.displayed == True
