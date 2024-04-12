# file thefuck/rules/tsuru_not_command.py:11-15
# lines [11, 12, 13, 14, 15]
# branches []

import pytest
from thefuck.types import Command
from thefuck.rules.tsuru_not_command import get_new_command, match
from unittest.mock import Mock

@pytest.fixture
def tsuru_not_command_output():
    return '''tsuru: "app-infoo" is not a tsuru command. See "tsuru help".
Did you mean?
	app-info
	app-list
	app-remove'''

def test_get_new_command(tsuru_not_command_output, mocker):
    mocker.patch(
        'thefuck.rules.tsuru_not_command.get_all_matched_commands',
        return_value=['app-info', 'app-list', 'app-remove']
    )
    command = Command('tsuru app-infoo', tsuru_not_command_output)
    new_commands = get_new_command(command)
    assert new_commands == ['tsuru app-info', 'tsuru app-list', 'tsuru app-remove']
