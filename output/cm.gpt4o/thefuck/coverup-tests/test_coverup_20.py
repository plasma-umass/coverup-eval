# file thefuck/logs.py:84-90
# lines [84, 85, 86, 87, 88, 90]
# branches []

import pytest
from contextlib import contextmanager
from datetime import datetime, timedelta
from unittest.mock import patch

# Assuming the debug_time function is defined in thefuck.logs module
from thefuck.logs import debug_time

@patch('thefuck.logs.debug')
def test_debug_time(mock_debug):
    msg = "Test message"
    with debug_time(msg):
        # Simulate some processing time
        pass

    # Check that the debug function was called with the correct message
    assert mock_debug.called
    call_args = mock_debug.call_args[0][0]
    assert msg in call_args
    assert "took: " in call_args
    assert isinstance(call_args.split("took: ")[1], str)
