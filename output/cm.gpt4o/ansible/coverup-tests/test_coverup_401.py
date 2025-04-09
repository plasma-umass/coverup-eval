# file lib/ansible/cli/arguments/option_helpers.py:190-207
# lines [190, 195, 196, 197, 198, 199, 200, 202, 205, 206, 207]
# branches []

import pytest
import argparse
from ansible.cli.arguments.option_helpers import create_base_parser
from ansible.cli.arguments.option_helpers import AnsibleVersion, add_verbosity_options
from unittest.mock import patch

def test_create_base_parser(mocker):
    prog = "test_prog"
    usage = "test_usage"
    desc = "test_desc"
    epilog = "test_epilog"

    # Mocking add_verbosity_options to ensure it is called
    mock_add_verbosity_options = mocker.patch('ansible.cli.arguments.option_helpers.add_verbosity_options')

    parser = create_base_parser(prog, usage, desc, epilog)

    # Assertions to verify the parser is created correctly
    assert parser.prog == prog
    assert parser.description == desc
    assert parser.epilog == epilog

    # Check if the version argument is added correctly
    version_arg = parser._option_string_actions.get('--version')
    assert version_arg is not None
    assert version_arg.help == "show program's version number, config file location, configured module search path, module location, executable location and exit"
    assert version_arg.nargs == 0
    assert isinstance(version_arg, argparse.Action)
    assert isinstance(version_arg, AnsibleVersion)

    # Verify that add_verbosity_options was called with the parser
    mock_add_verbosity_options.assert_called_once_with(parser)
