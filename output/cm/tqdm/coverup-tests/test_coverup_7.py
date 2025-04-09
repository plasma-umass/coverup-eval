# file tqdm/gui.py:181-186
# lines [181, 186]
# branches []

import pytest
from tqdm.gui import tqdm_gui, tgrange

# Since the actual GUI part of tqdm is not easily testable in an automated fashion,
# we will mock the tqdm_gui function to ensure that it is being called correctly.

def test_tgrange(mocker):
    # Mock tqdm_gui to simply return its arguments for inspection
    mock_tqdm_gui = mocker.patch('tqdm.gui.tqdm_gui', return_value='mocked tqdm_gui')

    # Call tgrange with some arguments
    result = tgrange(10, desc='Test Progress Bar')

    # Assert that tqdm_gui was called with the correct arguments
    mock_tqdm_gui.assert_called_once_with(range(10), desc='Test Progress Bar')

    # Assert that the result is what the mocked tqdm_gui returned
    assert result == 'mocked tqdm_gui'

    # Clean up by stopping the mock
    mocker.stopall()
