# file: lib/ansible/cli/arguments/option_helpers.py:210-213
# asked: {"lines": [210, 212, 213], "branches": []}
# gained: {"lines": [210, 212, 213], "branches": []}

import pytest
from argparse import ArgumentParser
from ansible.cli.arguments.option_helpers import add_verbosity_options
from ansible import constants as C

def test_add_verbosity_options():
    parser = ArgumentParser()
    add_verbosity_options(parser)
    args = parser.parse_args(['-v'])
    assert args.verbosity == C.DEFAULT_VERBOSITY + 1

    args = parser.parse_args(['-vv'])
    assert args.verbosity == C.DEFAULT_VERBOSITY + 2

    args = parser.parse_args(['-vvv'])
    assert args.verbosity == C.DEFAULT_VERBOSITY + 3

    args = parser.parse_args(['-vvvv'])
    assert args.verbosity == C.DEFAULT_VERBOSITY + 4
