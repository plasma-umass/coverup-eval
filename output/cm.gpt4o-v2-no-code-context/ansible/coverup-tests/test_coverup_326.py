# file: lib/ansible/cli/arguments/option_helpers.py:340-358
# asked: {"lines": [340, 347, 348, 350, 352, 353, 354, 355, 356, 358], "branches": [[347, 348], [347, 350]]}
# gained: {"lines": [340, 347, 348, 350, 352, 353, 354, 355, 356, 358], "branches": [[347, 348], [347, 350]]}

import pytest
from argparse import ArgumentParser
from ansible.cli.arguments.option_helpers import add_runas_prompt_options
from ansible import constants as C

@pytest.fixture
def parser():
    return ArgumentParser()

def test_add_runas_prompt_options_with_runas_group(parser):
    runas_group_name = "Runas Group"
    add_runas_prompt_options(parser, runas_group=runas_group_name)
    
    # Check if the runas_group was added
    assert any(group.title == runas_group_name for group in parser._action_groups)

def test_add_runas_prompt_options_without_runas_group(parser):
    add_runas_prompt_options(parser)
    
    # Check if the mutually exclusive group was added
    assert any(group.title is None for group in parser._mutually_exclusive_groups)
    
    # Check if the arguments were added to the mutually exclusive group
    args = parser.parse_args(['-K'])
    assert args.become_ask_pass == True
    assert args.become_password_file == C.BECOME_PASSWORD_FILE

    args = parser.parse_args(['--become-password-file', '/path/to/file'])
    assert args.become_ask_pass == False
    assert args.become_password_file == '/path/to/file'

def test_add_runas_prompt_options_argument_conflict(parser):
    with pytest.raises(SystemExit):
        parser.parse_args(['-K', '--become-password-file', '/path/to/file'])

@pytest.fixture(autouse=True)
def cleanup(monkeypatch):
    # Clean up any state pollution
    monkeypatch.undo()
