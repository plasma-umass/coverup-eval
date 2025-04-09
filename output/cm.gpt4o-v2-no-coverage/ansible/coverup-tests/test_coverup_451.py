# file: lib/ansible/cli/arguments/option_helpers.py:190-207
# asked: {"lines": [190, 195, 196, 197, 198, 199, 200, 202, 205, 206, 207], "branches": []}
# gained: {"lines": [190, 195, 196, 197, 198, 199, 200, 202, 205, 206, 207], "branches": []}

import pytest
import argparse
from ansible.cli.arguments.option_helpers import create_base_parser, SortingHelpFormatter, AnsibleVersion, add_verbosity_options
from ansible import constants as C

def test_create_base_parser():
    prog = "test_prog"
    usage = "test_usage"
    desc = "test_desc"
    epilog = "test_epilog"

    parser = create_base_parser(prog, usage, desc, epilog)

    assert isinstance(parser, argparse.ArgumentParser)
    assert parser.prog == prog
    assert parser.description == desc
    assert parser.epilog == epilog
    assert parser.formatter_class == SortingHelpFormatter
    assert parser.conflict_handler == 'resolve'

    # Check if --version argument is added correctly
    version_arg = parser._option_string_actions.get('--version')
    assert version_arg is not None
    assert isinstance(version_arg, AnsibleVersion)
    assert version_arg.help == "show program's version number, config file location, configured module search path, module location, executable location and exit"

    # Check if verbosity options are added correctly
    verbosity_arg = parser._option_string_actions.get('-v')
    assert verbosity_arg is not None
    assert verbosity_arg.dest == 'verbosity'
    assert verbosity_arg.default == C.DEFAULT_VERBOSITY
    assert isinstance(verbosity_arg, argparse._CountAction)
    assert verbosity_arg.help == 'verbose mode (-vvv for more, -vvvv to enable connection debugging)'

