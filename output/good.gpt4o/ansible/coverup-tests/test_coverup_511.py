# file lib/ansible/cli/arguments/option_helpers.py:232-240
# lines [232, 234, 235, 236, 237, 238, 239]
# branches []

import pytest
from argparse import ArgumentParser
from ansible.cli.arguments.option_helpers import add_check_options
from ansible import constants as C

def test_add_check_options():
    parser = ArgumentParser()
    add_check_options(parser)
    
    args = parser.parse_args(['--check'])
    assert args.check is True
    assert args.syntax is False
    assert args.diff == C.DIFF_ALWAYS

    args = parser.parse_args(['--syntax-check'])
    assert args.check is False
    assert args.syntax is True
    assert args.diff == C.DIFF_ALWAYS

    args = parser.parse_args(['--diff'])
    assert args.check is False
    assert args.syntax is False
    assert args.diff is True

    args = parser.parse_args(['--check', '--syntax-check', '--diff'])
    assert args.check is True
    assert args.syntax is True
    assert args.diff is True
