# file: tqdm/notebook.py:149-198
# asked: {"lines": [174, 186, 187, 191, 192, 193, 194, 197, 198], "branches": [[159, 166], [169, 183], [171, 174], [179, 183], [183, 186], [186, 187], [186, 190], [190, 191], [196, 197]]}
# gained: {"lines": [174, 186, 187, 191, 192, 193, 194, 197, 198], "branches": [[159, 166], [169, 183], [171, 174], [183, 186], [186, 187], [190, 191], [196, 197]]}

import pytest
from unittest.mock import MagicMock, patch
from tqdm.notebook import tqdm_notebook

@pytest.fixture
def mock_container():
    container = MagicMock()
    container.children = [MagicMock(), MagicMock(), MagicMock()]
    return container

@pytest.fixture
def tqdm_instance(mock_container):
    instance = tqdm_notebook(total=100)
    instance.container = mock_container
    instance.n = 50
    instance._format_dict = {
        'bar_format': '{l_bar}<bar/>{r_bar}',
        'n': 50,
        'total': 100,
        'elapsed': 1,
        'ncols': 10,
        'prefix': '',
        'ascii': False,
        'unit': 'it',
        'unit_scale': False,
        'rate': None,
        'postfix': None,
        'unit_divisor': 1000,
        'initial': 0,
        'dynamic_ncols': False,
        'smoothing': 0.3,
        'mininterval': 0.1,
        'maxinterval': 10.0,
        'miniters': 1,
        'disable': False,
        'leave': True,
        'gui': False,
        'file': None,
        'nrows': None,
        'colour': None,
        'position': None,
        'write_bytes': False,
        'lock_args': None,
    }
    return instance

def test_display_no_msg_no_close(tqdm_instance):
    tqdm_instance.display()
    ltext, pbar, rtext = tqdm_instance.container.children
    assert pbar.value == 50

def test_display_with_msg(tqdm_instance):
    tqdm_instance.display(msg="Test message")
    ltext, pbar, rtext = tqdm_instance.container.children
    assert ltext.value == ''
    assert rtext.value == 'Test message'

def test_display_with_bar_style(tqdm_instance):
    tqdm_instance.display(bar_style="success")
    ltext, pbar, rtext = tqdm_instance.container.children
    assert pbar.bar_style == "success"

def test_display_with_close(tqdm_instance):
    tqdm_instance.display(close=True)
    tqdm_instance.container.close.assert_called_once()

def test_display_with_close_and_exception(tqdm_instance):
    tqdm_instance.container.close.side_effect = AttributeError
    tqdm_instance.display(close=True)
    assert not tqdm_instance.container.visible

def test_display_with_check_delay(tqdm_instance):
    tqdm_instance.delay = 1
    tqdm_instance.displayed = False
    with patch("tqdm.notebook.display") as mock_display:
        tqdm_instance.display()
        mock_display.assert_called_once_with(tqdm_instance.container)
        assert tqdm_instance.displayed
