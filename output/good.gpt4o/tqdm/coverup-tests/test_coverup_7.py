# file tqdm/gui.py:181-186
# lines [181, 186]
# branches []

import pytest
from unittest import mock
from tqdm.gui import tqdm_gui

def test_tgrange(mocker):
    # Mock tqdm_gui to avoid actual GUI operations
    mock_tqdm_gui = mocker.patch('tqdm.gui.tqdm_gui')

    # Import the function to be tested
    from tqdm.gui import tgrange

    # Test with a simple range
    tgrange(5)
    mock_tqdm_gui.assert_called_once_with(range(5))

    # Test with additional arguments
    tgrange(1, 5, 2)
    mock_tqdm_gui.assert_called_with(range(1, 5, 2))

    # Test with keyword arguments
    tgrange(5, desc="Test")
    mock_tqdm_gui.assert_called_with(range(5), desc="Test")

    # Test with both positional and keyword arguments
    tgrange(1, 5, 2, desc="Test")
    mock_tqdm_gui.assert_called_with(range(1, 5, 2), desc="Test")
