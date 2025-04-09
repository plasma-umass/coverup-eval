# file: lib/ansible/cli/arguments/option_helpers.py:340-358
# asked: {"lines": [340, 347, 348, 350, 352, 353, 354, 355, 356, 358], "branches": [[347, 348], [347, 350]]}
# gained: {"lines": [340, 347, 348, 350, 352, 353, 354, 355, 356, 358], "branches": [[347, 348], [347, 350]]}

import pytest
from argparse import ArgumentParser
from ansible.cli.arguments.option_helpers import add_runas_prompt_options
from ansible import constants as C
from ansible.utils.path import unfrackpath

@pytest.fixture
def parser():
    return ArgumentParser()

def test_add_runas_prompt_options_with_runas_group(parser):
    runas_group = 'Runas Group'
    add_runas_prompt_options(parser, runas_group)
    args = parser.parse_args([])

    assert any(group.title == runas_group for group in parser._action_groups)
    assert any(action.dest == 'become_ask_pass' for action in parser._actions)
    assert any(action.dest == 'become_password_file' for action in parser._actions)

def test_add_runas_prompt_options_without_runas_group(parser):
    add_runas_prompt_options(parser)
    args = parser.parse_args([])

    assert any(action.dest == 'become_ask_pass' for action in parser._actions)
    assert any(action.dest == 'become_password_file' for action in parser._actions)

def test_add_runas_prompt_options_ask_become_pass(parser):
    add_runas_prompt_options(parser)
    args = parser.parse_args(['-K'])

    assert args.become_ask_pass is True
    assert args.become_password_file == C.BECOME_PASSWORD_FILE

def test_add_runas_prompt_options_become_password_file(parser, monkeypatch):
    test_file = '/tmp/test_become_pass_file'
    monkeypatch.setattr('ansible.cli.arguments.option_helpers.unfrack_path', lambda: lambda x: x)
    add_runas_prompt_options(parser)
    args = parser.parse_args(['--become-password-file', test_file])

    assert args.become_ask_pass == C.DEFAULT_BECOME_ASK_PASS
    assert args.become_password_file == test_file
