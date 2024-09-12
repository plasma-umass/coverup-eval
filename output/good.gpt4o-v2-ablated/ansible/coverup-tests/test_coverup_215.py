# file: lib/ansible/cli/arguments/option_helpers.py:232-240
# asked: {"lines": [232, 234, 235, 236, 237, 238, 239], "branches": []}
# gained: {"lines": [232, 234, 235, 236, 237, 238, 239], "branches": []}

import pytest
from argparse import ArgumentParser, Namespace
from ansible.cli.arguments.option_helpers import add_check_options
import ansible.constants as C

@pytest.fixture
def parser():
    return ArgumentParser()

def test_add_check_options_check(parser):
    add_check_options(parser)
    args = parser.parse_args(['--check'])
    assert args.check is True
    assert args.syntax is False
    assert args.diff == C.DIFF_ALWAYS

def test_add_check_options_syntax_check(parser):
    add_check_options(parser)
    args = parser.parse_args(['--syntax-check'])
    assert args.check is False
    assert args.syntax is True
    assert args.diff == C.DIFF_ALWAYS

def test_add_check_options_diff(parser):
    add_check_options(parser)
    args = parser.parse_args(['--diff'])
    assert args.check is False
    assert args.syntax is False
    assert args.diff is True

def test_add_check_options_no_args(parser):
    add_check_options(parser)
    args = parser.parse_args([])
    assert args.check is False
    assert args.syntax is False
    assert args.diff == C.DIFF_ALWAYS
