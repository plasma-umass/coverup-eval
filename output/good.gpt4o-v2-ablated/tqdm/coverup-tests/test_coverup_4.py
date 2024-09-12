# file: tqdm/gui.py:181-186
# asked: {"lines": [186], "branches": []}
# gained: {"lines": [186], "branches": []}

import pytest
from unittest.mock import patch
from tqdm.gui import tqdm as tqdm_gui

# Import the function to be tested
from tqdm.gui import tgrange

@pytest.fixture
def mock_tqdm_gui(mocker):
    return mocker.patch('tqdm.gui.tqdm_gui')

def test_tgrange_with_args(mock_tqdm_gui):
    # Test with positional arguments
    tgrange(10)
    mock_tqdm_gui.assert_called_once_with(range(10))

def test_tgrange_with_kwargs(mock_tqdm_gui):
    # Test with keyword arguments
    tgrange(10, desc="Progress")
    mock_tqdm_gui.assert_called_once_with(range(10), desc="Progress")

def test_tgrange_with_args_and_kwargs(mock_tqdm_gui):
    # Test with both positional and keyword arguments
    tgrange(1, 10, 2, desc="Progress")
    mock_tqdm_gui.assert_called_once_with(range(1, 10, 2), desc="Progress")
