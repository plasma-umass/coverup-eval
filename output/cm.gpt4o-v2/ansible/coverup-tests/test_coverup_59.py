# file: lib/ansible/modules/command.py:233-266
# asked: {"lines": [233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 246, 247, 249, 252, 254, 255, 256, 257, 258, 260, 261, 262, 263, 265, 266], "branches": [[243, 244], [243, 246], [254, 255], [254, 260], [260, 261], [260, 265], [265, 0], [265, 266]]}
# gained: {"lines": [233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 246, 247, 249, 252, 254, 255, 256, 257, 258, 260, 261, 262, 263, 265, 266], "branches": [[243, 244], [243, 246], [254, 255], [254, 260], [260, 261], [260, 265], [265, 0], [265, 266]]}

import pytest
from unittest.mock import Mock
import os
from ansible.modules.command import check_command

@pytest.fixture
def mock_module():
    return Mock()

def test_check_command_with_arguments(mock_module):
    commandline = "chown"
    check_command(mock_module, commandline)
    mock_module.warn.assert_called_once_with(
        "Consider using the file module with owner rather than running 'chown'.  "
        "If you need to use 'chown' because the file module is insufficient you can add 'warn: false' to this command task or set 'command_warnings=False' in the defaults section of ansible.cfg to get rid of this message."
    )

def test_check_command_with_commands(mock_module):
    commandline = "curl"
    check_command(mock_module, commandline)
    mock_module.warn.assert_called_once_with(
        "Consider using the get_url or uri module rather than running 'curl'.  "
        "If you need to use 'curl' because the get_url or uri module is insufficient you can add 'warn: false' to this command task or set 'command_warnings=False' in the defaults section of ansible.cfg to get rid of this message."
    )

def test_check_command_with_become(mock_module):
    commandline = "sudo"
    check_command(mock_module, commandline)
    mock_module.warn.assert_called_once_with(
        "Consider using 'become', 'become_method', and 'become_user' rather than running sudo"
    )

def test_check_command_with_list_commandline(mock_module):
    commandline = ["chown"]
    check_command(mock_module, commandline)
    mock_module.warn.assert_called_once_with(
        "Consider using the file module with owner rather than running 'chown'.  "
        "If you need to use 'chown' because the file module is insufficient you can add 'warn: false' to this command task or set 'command_warnings=False' in the defaults section of ansible.cfg to get rid of this message."
    )

def test_check_command_with_non_matching_command(mock_module):
    commandline = "nonexistentcommand"
    check_command(mock_module, commandline)
    mock_module.warn.assert_not_called()
