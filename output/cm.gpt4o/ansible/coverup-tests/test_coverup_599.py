# file lib/ansible/cli/arguments/option_helpers.py:309-314
# lines [309, 311, 312, 313, 314]
# branches []

import pytest
from argparse import ArgumentParser
from ansible.cli.arguments.option_helpers import add_output_options

def test_add_output_options(mocker):
    parser = ArgumentParser()
    add_output_options(parser)
    
    # Test the '--one-line' option
    args = parser.parse_args(['--one-line'])
    assert args.one_line is True
    
    # Test the '-o' option
    args = parser.parse_args(['-o'])
    assert args.one_line is True
    
    # Test the '--tree' option
    args = parser.parse_args(['--tree', '/some/directory'])
    assert args.tree == '/some/directory'
    
    # Test the '-t' option
    args = parser.parse_args(['-t', '/some/directory'])
    assert args.tree == '/some/directory'
    
    # Test default values
    args = parser.parse_args([])
    assert args.one_line is False
    assert args.tree is None
