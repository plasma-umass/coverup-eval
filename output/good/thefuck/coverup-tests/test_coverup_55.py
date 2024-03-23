# file thefuck/types.py:26-29
# lines [26, 27, 28, 29]
# branches []

import pytest
from thefuck.types import Command
from unittest.mock import patch

def test_command_stdout_deprecation_warning():
    with patch('thefuck.types.logs.warn') as mock_warn:
        cmd = Command(script='fake_script', output='expected output')
        assert cmd.stdout == 'expected output'
        mock_warn.assert_called_once_with('`stdout` is deprecated, please use `output` instead')
