# file: lib/ansible/cli/arguments/option_helpers.py:190-207
# asked: {"lines": [190, 195, 196, 197, 198, 199, 200, 202, 205, 206, 207], "branches": []}
# gained: {"lines": [190, 195, 196, 197, 198, 199, 200, 202, 205, 206, 207], "branches": []}

import pytest
import argparse
from ansible.cli.arguments.option_helpers import create_base_parser, SortingHelpFormatter, AnsibleVersion, add_verbosity_options

def test_create_base_parser(monkeypatch):
    # Mocking add_verbosity_options to avoid side effects
    def mock_add_verbosity_options(parser):
        parser.add_argument('--mock-verbosity', action='store_true', help='mock verbosity option')

    monkeypatch.setattr('ansible.cli.arguments.option_helpers.add_verbosity_options', mock_add_verbosity_options)

    prog = 'test_prog'
    desc = 'test_desc'
    epilog = 'test_epilog'

    parser = create_base_parser(prog, desc=desc, epilog=epilog)

    assert isinstance(parser, argparse.ArgumentParser)
    assert parser.prog == prog
    assert parser.description == desc
    assert parser.epilog == epilog

    # Check if the --version argument is added correctly
    version_arg = parser._option_string_actions.get('--version')
    assert version_arg is not None
    assert version_arg.help.startswith("show program's version number")

    # Check if the mock verbosity option is added correctly
    mock_verbosity_arg = parser._option_string_actions.get('--mock-verbosity')
    assert mock_verbosity_arg is not None
    assert mock_verbosity_arg.help == 'mock verbosity option'
