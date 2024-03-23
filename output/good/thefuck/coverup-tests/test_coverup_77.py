# file thefuck/rules/rm_root.py:14-16
# lines [14, 15, 16]
# branches []

import pytest
from thefuck.types import Command
from thefuck.rules.rm_root import get_new_command
from unittest.mock import Mock

@pytest.fixture
def mock_sudo_support(mocker):
    mocker.patch('thefuck.rules.rm_root.sudo_support')

def test_get_new_command(mock_sudo_support):
    command = Command('rm -rf /', '')
    new_command = get_new_command(command)
    assert new_command == 'rm -rf / --no-preserve-root'
