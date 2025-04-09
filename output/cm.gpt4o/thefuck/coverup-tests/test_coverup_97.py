# file thefuck/rules/rm_root.py:14-16
# lines [14, 15, 16]
# branches []

import pytest
from thefuck.rules.rm_root import get_new_command
from thefuck.types import Command
from thefuck.specific.sudo import sudo_support

@pytest.fixture
def mock_sudo_support(mocker):
    return mocker.patch('thefuck.rules.rm_root.sudo_support', side_effect=lambda x: x)

def test_get_new_command(mock_sudo_support):
    command = Command(script='rm -rf /', output='')
    new_command = get_new_command(command)
    assert new_command == 'rm -rf / --no-preserve-root'
