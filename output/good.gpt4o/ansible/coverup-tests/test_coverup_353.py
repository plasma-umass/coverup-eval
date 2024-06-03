# file lib/ansible/cli/arguments/option_helpers.py:340-358
# lines [340, 347, 348, 350, 352, 353, 354, 355, 356, 358]
# branches ['347->348', '347->350']

import pytest
from unittest import mock
from argparse import ArgumentParser
from ansible.cli.arguments.option_helpers import add_runas_prompt_options

@pytest.fixture
def parser():
    return ArgumentParser()

def test_add_runas_prompt_options_with_runas_group(parser):
    runas_group = 'runas_group'
    add_runas_prompt_options(parser, runas_group)
    
    # Check if the runas_group is added
    assert any(group.title == runas_group for group in parser._action_groups)

def test_add_runas_prompt_options_without_runas_group(parser):
    add_runas_prompt_options(parser)
    
    # Check if the mutually exclusive group is added
    assert any(group.title is None for group in parser._mutually_exclusive_groups)
    
    # Check if the arguments are added
    args = parser.parse_args(['-K'])
    assert args.become_ask_pass is True

    args = parser.parse_args(['--become-password-file', 'some_file'])
    assert args.become_password_file == 'some_file'

@pytest.fixture(autouse=True)
def mock_constants(mocker):
    mocker.patch('ansible.cli.arguments.option_helpers.C.DEFAULT_BECOME_ASK_PASS', False)
    mocker.patch('ansible.cli.arguments.option_helpers.C.BECOME_PASSWORD_FILE', 'default_file')
    mocker.patch('ansible.cli.arguments.option_helpers.unfrack_path', return_value=str)

def test_add_runas_prompt_options_defaults(parser):
    add_runas_prompt_options(parser)
    
    args = parser.parse_args([])
    assert args.become_ask_pass is False
    assert args.become_password_file == 'default_file'
