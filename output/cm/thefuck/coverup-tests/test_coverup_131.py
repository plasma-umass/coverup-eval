# file thefuck/rules/aws_cli.py:14-17
# lines [15, 16, 17]
# branches []

import pytest
from thefuck.types import Command
from thefuck.rules.aws_cli import get_new_command
from unittest.mock import Mock

@pytest.fixture
def aws_cli_invalid_choice():
    return '''\
    Invalid choice: 'ec', maybe you meant:
      * ecs
      * ec2
    '''

@pytest.fixture
def mock_command(mocker, aws_cli_invalid_choice):
    command = Command('aws ec', aws_cli_invalid_choice)
    mocker.patch('thefuck.rules.aws_cli.replace_argument', side_effect=lambda script, old, new: script.replace(old, new))
    return command

def test_aws_cli_invalid_choice(mock_command, aws_cli_invalid_choice):
    new_commands = get_new_command(mock_command)
    assert new_commands == ['aws ecs', 'aws ec2']
    assert mock_command.output == aws_cli_invalid_choice
