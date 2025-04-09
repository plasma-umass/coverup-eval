# file: lib/ansible/cli/arguments/option_helpers.py:277-280
# asked: {"lines": [277, 279, 280], "branches": []}
# gained: {"lines": [277, 279, 280], "branches": []}

import pytest
from argparse import ArgumentParser
from ansible.cli.arguments.option_helpers import add_fork_options
from ansible import constants as C

def test_add_fork_options():
    parser = ArgumentParser()
    add_fork_options(parser)
    args = parser.parse_args(['--forks', '10'])
    assert args.forks == 10

    args = parser.parse_args([])
    assert args.forks == C.DEFAULT_FORKS
