# file: tqdm/gui.py:181-186
# asked: {"lines": [181, 186], "branches": []}
# gained: {"lines": [181, 186], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
from tqdm.gui import tgrange

@pytest.fixture
def mock_tqdm_gui():
    with patch('tqdm.gui.tqdm_gui', autospec=True) as mock:
        yield mock

def test_tgrange_with_args(mock_tqdm_gui):
    mock_instance = mock_tqdm_gui.return_value
    result = tgrange(10, foo='bar')
    mock_tqdm_gui.assert_called_once_with(range(10), foo='bar')
    assert result == mock_instance

def test_tgrange_no_args(mock_tqdm_gui):
    mock_instance = mock_tqdm_gui.return_value
    result = tgrange(0)
    mock_tqdm_gui.assert_called_once_with(range(0),)
    assert result == mock_instance
