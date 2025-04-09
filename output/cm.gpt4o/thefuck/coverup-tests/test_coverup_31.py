# file thefuck/rules/sudo_command_from_user_path.py:5-8
# lines [5, 6, 7, 8]
# branches ['7->exit', '7->8']

import pytest
import re
from thefuck.rules.sudo_command_from_user_path import _get_command_name

def test_get_command_name_found():
    command = type('Command', (object,), {'output': 'sudo: testcmd: command not found'})
    assert _get_command_name(command) == 'testcmd'

def test_get_command_name_not_found():
    command = type('Command', (object,), {'output': 'some other output'})
    assert _get_command_name(command) is None
