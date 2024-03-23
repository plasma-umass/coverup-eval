# file thefuck/rules/git_push_pull.py:17-20
# lines [17, 18, 19, 20]
# branches []

import pytest
from thefuck.types import Command
from thefuck.rules.git_push_pull import get_new_command
from thefuck.shells import shell
from unittest.mock import Mock

@pytest.fixture
def mock_git_support(mocker):
    return mocker.patch('thefuck.rules.git_push_pull.git_support', lambda x: x)

def test_get_new_command_with_push_to_pull(mock_git_support):
    command = Command('git push origin master', '')
    new_command = get_new_command(command)
    assert new_command == shell.and_('git pull origin master', 'git push origin master')
