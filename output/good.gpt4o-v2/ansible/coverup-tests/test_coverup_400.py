# file: lib/ansible/cli/arguments/option_helpers.py:190-207
# asked: {"lines": [190, 195, 196, 197, 198, 199, 200, 202, 205, 206, 207], "branches": []}
# gained: {"lines": [190, 195, 196, 197, 198, 199, 200, 202, 205, 206, 207], "branches": []}

import pytest
import argparse
from ansible.cli.arguments.option_helpers import create_base_parser, SortingHelpFormatter, AnsibleVersion, add_verbosity_options

def test_create_base_parser(monkeypatch):
    # Mock the add_verbosity_options to ensure it is called
    def mock_add_verbosity_options(parser):
        parser.add_argument('--mock-verbosity', action='store_true', help='mock verbosity option')

    monkeypatch.setattr('ansible.cli.arguments.option_helpers.add_verbosity_options', mock_add_verbosity_options)

    # Create the parser
    parser = create_base_parser(prog='test_prog', usage='test_usage', desc='test_desc', epilog='test_epilog')

    # Check if the parser is an instance of argparse.ArgumentParser
    assert isinstance(parser, argparse.ArgumentParser)

    # Check if the parser has the correct program name
    assert parser.prog == 'test_prog'

    # Check if the parser has the correct usage
    assert parser.usage == 'test_usage' or parser.usage is None

    # Check if the parser has the correct description
    assert parser.description == 'test_desc'

    # Check if the parser has the correct epilog
    assert parser.epilog == 'test_epilog'

    # Check if the parser has the --version argument
    version_action = parser._option_string_actions.get('--version')
    assert version_action is not None
    assert isinstance(version_action, AnsibleVersion)
    assert version_action.help.startswith("show program's version number")

    # Check if the mock verbosity option is added
    mock_verbosity_action = parser._option_string_actions.get('--mock-verbosity')
    assert mock_verbosity_action is not None
    assert mock_verbosity_action.help == 'mock verbosity option'
