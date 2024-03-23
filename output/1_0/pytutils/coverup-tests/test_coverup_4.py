# file pytutils/debug.py:5-20
# lines [5, 7, 9, 11, 14, 15, 18, 20]
# branches []

import pytest
from unittest.mock import patch
from pytutils.debug import interact

def test_interact():
    with patch("pytutils.debug.inspect.currentframe") as mock_currentframe, \
         patch("pytutils.debug.code.interact") as mock_interact:
        
        # Mock the frame to simulate the caller's environment
        mock_frame = mock_currentframe.return_value
        mock_frame.f_back = mock_frame
        mock_frame.f_globals = {'global_var': 1}
        mock_frame.f_locals = {'local_var': 2}

        # Call the interact function
        interact()

        # Assert that code.interact was called with the correct local variables
        mock_interact.assert_called_once()
        interact_locals = mock_interact.call_args[1]['local']
        assert interact_locals['global_var'] == 1
        assert interact_locals['local_var'] == 2
        assert 'banner' in mock_interact.call_args[1]

        # Clean up by deleting the mock frame
        del mock_frame
