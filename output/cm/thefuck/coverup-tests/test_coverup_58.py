# file thefuck/types.py:31-34
# lines [31, 32, 33, 34]
# branches []

import pytest
from thefuck.types import Command
from unittest.mock import patch

def test_command_stderr_deprecation_warning():
    with patch('thefuck.logs.warn') as mock_warn:
        command = Command(script='fake_script', output='mocked output')
        assert command.stderr == 'mocked output'
        mock_warn.assert_called_once_with('`stderr` is deprecated, please use `output` instead')
