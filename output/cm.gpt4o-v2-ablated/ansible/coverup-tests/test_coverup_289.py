# file: lib/ansible/cli/arguments/option_helpers.py:210-213
# asked: {"lines": [210, 212, 213], "branches": []}
# gained: {"lines": [210, 212, 213], "branches": []}

import pytest
from argparse import ArgumentParser, Namespace
from ansible.cli.arguments.option_helpers import add_verbosity_options
import ansible.constants as C

@pytest.fixture
def parser():
    return ArgumentParser()

def test_add_verbosity_options_default(parser):
    add_verbosity_options(parser)
    args = parser.parse_args([])
    assert args.verbosity == C.DEFAULT_VERBOSITY

def test_add_verbosity_options_single_v(parser):
    add_verbosity_options(parser)
    args = parser.parse_args(['-v'])
    assert args.verbosity == C.DEFAULT_VERBOSITY + 1

def test_add_verbosity_options_double_v(parser):
    add_verbosity_options(parser)
    args = parser.parse_args(['-vv'])
    assert args.verbosity == C.DEFAULT_VERBOSITY + 2

def test_add_verbosity_options_triple_v(parser):
    add_verbosity_options(parser)
    args = parser.parse_args(['-vvv'])
    assert args.verbosity == C.DEFAULT_VERBOSITY + 3

def test_add_verbosity_options_quadruple_v(parser):
    add_verbosity_options(parser)
    args = parser.parse_args(['-vvvv'])
    assert args.verbosity == C.DEFAULT_VERBOSITY + 4

def test_add_verbosity_options_verbose(parser):
    add_verbosity_options(parser)
    args = parser.parse_args(['--verbose'])
    assert args.verbosity == C.DEFAULT_VERBOSITY + 1

def test_add_verbosity_options_verbose_verbose(parser):
    add_verbosity_options(parser)
    args = parser.parse_args(['--verbose', '--verbose'])
    assert args.verbosity == C.DEFAULT_VERBOSITY + 2
