# file: lib/ansible/cli/arguments/option_helpers.py:232-240
# asked: {"lines": [234, 235, 236, 237, 238, 239], "branches": []}
# gained: {"lines": [234, 235, 236, 237, 238, 239], "branches": []}

import pytest
from argparse import ArgumentParser
from ansible.cli.arguments.option_helpers import add_check_options

@pytest.fixture
def parser():
    return ArgumentParser()

def test_add_check_options(parser):
    add_check_options(parser)
    args = parser.parse_args(['--check'])
    assert args.check is True
    args = parser.parse_args(['--syntax-check'])
    assert args.syntax is True
    args = parser.parse_args(['--diff'])
    assert args.diff is True
