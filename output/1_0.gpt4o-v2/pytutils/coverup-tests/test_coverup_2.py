# file: pytutils/debug.py:5-20
# asked: {"lines": [5, 7, 9, 11, 14, 15, 18, 20], "branches": []}
# gained: {"lines": [5, 7, 9, 11, 14, 15, 18, 20], "branches": []}

import pytest
import code
import inspect
from unittest.mock import patch

from pytutils.debug import interact

def test_interact(monkeypatch):
    # Mock the interactive console to prevent it from actually running
    with patch('code.interact') as mock_interact:
        # Call the function
        interact()

        # Ensure the interactive console was called
        mock_interact.assert_called_once()

        # Ensure the banner is correct
        args, kwargs = mock_interact.call_args
        assert kwargs['banner'] == '(debug shell)'

        # Ensure the local variables passed to the console include at least some known globals
        assert 'inspect' in kwargs['local']
        assert 'code' in kwargs['local']
