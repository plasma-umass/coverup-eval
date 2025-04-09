# file: lib/ansible/cli/arguments/option_helpers.py:309-314
# asked: {"lines": [309, 311, 312, 313, 314], "branches": []}
# gained: {"lines": [309, 311, 312, 313, 314], "branches": []}

import pytest
from argparse import ArgumentParser

def test_add_output_options_one_line():
    from ansible.cli.arguments.option_helpers import add_output_options

    parser = ArgumentParser()
    add_output_options(parser)
    args = parser.parse_args(['--one-line'])
    assert args.one_line is True
    assert args.tree is None

def test_add_output_options_tree():
    from ansible.cli.arguments.option_helpers import add_output_options

    parser = ArgumentParser()
    add_output_options(parser)
    args = parser.parse_args(['--tree', '/some/directory'])
    assert args.one_line is False
    assert args.tree == '/some/directory'

def test_add_output_options_default():
    from ansible.cli.arguments.option_helpers import add_output_options

    parser = ArgumentParser()
    add_output_options(parser)
    args = parser.parse_args([])
    assert args.one_line is False
    assert args.tree is None
