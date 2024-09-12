# file: lib/ansible/cli/arguments/option_helpers.py:277-280
# asked: {"lines": [279, 280], "branches": []}
# gained: {"lines": [279, 280], "branches": []}

import pytest
from argparse import ArgumentParser, Namespace
from unittest.mock import patch

# Mocking the C module and its DEFAULT_FORKS attribute
class MockC:
    DEFAULT_FORKS = 5

@patch('ansible.cli.arguments.option_helpers.C', new=MockC)
def test_add_fork_options(monkeypatch):
    from ansible.cli.arguments.option_helpers import add_fork_options

    parser = ArgumentParser()
    add_fork_options(parser)
    
    # Test default value
    args = parser.parse_args([])
    assert args.forks == MockC.DEFAULT_FORKS

    # Test custom value
    custom_forks = 10
    args = parser.parse_args(['-f', str(custom_forks)])
    assert args.forks == custom_forks

    args = parser.parse_args(['--forks', str(custom_forks)])
    assert args.forks == custom_forks
