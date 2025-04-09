# file: lib/ansible/cli/arguments/option_helpers.py:277-280
# asked: {"lines": [277, 279, 280], "branches": []}
# gained: {"lines": [277, 279, 280], "branches": []}

import pytest
from argparse import ArgumentParser, Namespace
from ansible.cli.arguments.option_helpers import add_fork_options
import ansible.constants as C

@pytest.fixture
def parser():
    return ArgumentParser()

def test_add_fork_options(parser, monkeypatch):
    # Set a default value for C.DEFAULT_FORKS to ensure the test is isolated
    monkeypatch.setattr(C, 'DEFAULT_FORKS', 5)
    
    add_fork_options(parser)
    args = parser.parse_args(['--forks', '10'])
    
    assert hasattr(args, 'forks')
    assert args.forks == 10

def test_add_fork_options_default(parser, monkeypatch):
    # Set a default value for C.DEFAULT_FORKS to ensure the test is isolated
    monkeypatch.setattr(C, 'DEFAULT_FORKS', 5)
    
    add_fork_options(parser)
    args = parser.parse_args([])
    
    assert hasattr(args, 'forks')
    assert args.forks == 5
