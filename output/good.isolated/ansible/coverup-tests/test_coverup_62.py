# file lib/ansible/modules/command.py:233-266
# lines [233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 246, 247, 249, 252, 254, 255, 256, 257, 258, 260, 261, 262, 263, 265, 266]
# branches ['243->244', '243->246', '254->255', '254->260', '260->261', '260->265', '265->exit', '265->266']

import os
import pytest
from unittest.mock import MagicMock

# Assuming the check_command function is part of the module ansible.modules.command
from ansible.modules.command import check_command

@pytest.fixture
def mock_module(mocker):
    mock_module = MagicMock()
    mock_module.warn = MagicMock()
    return mock_module

@pytest.mark.parametrize("commandline, expected_warning_start", [
    (["chown", "user", "file"], "Consider using the file module with owner rather than running 'chown'."),
    (["curl", "-O", "http://example.com/file"], "Consider using the get_url or uri module rather than running 'curl'."),
    (["sudo", "whoami"], "Consider using 'become', 'become_method', and 'become_user' rather than running sudo"),
])
def test_check_command_warnings(mock_module, commandline, expected_warning_start):
    check_command(mock_module, commandline)
    args, _ = mock_module.warn.call_args
    assert args[0].startswith(expected_warning_start)

def test_check_command_no_warnings(mock_module):
    commandline = ["echo", "Hello, World!"]
    check_command(mock_module, commandline)
    mock_module.warn.assert_not_called()
