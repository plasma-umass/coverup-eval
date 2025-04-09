# file: lib/ansible/cli/arguments/option_helpers.py:283-290
# asked: {"lines": [283, 285, 286, 287, 288, 289, 290], "branches": []}
# gained: {"lines": [283, 285, 286, 287, 288, 289, 290], "branches": []}

import pytest
from argparse import ArgumentParser
from ansible.cli.arguments.option_helpers import add_inventory_options
from ansible import constants as C

def test_add_inventory_options():
    parser = ArgumentParser()
    add_inventory_options(parser)
    args = parser.parse_args(['-i', 'inventory_path', '--list-hosts', '-l', 'subset_pattern'])

    assert 'inventory' in args
    assert args.inventory == ['inventory_path']
    assert 'listhosts' in args
    assert args.listhosts is True
    assert 'subset' in args
    assert args.subset == 'subset_pattern'

def test_add_inventory_options_defaults():
    parser = ArgumentParser()
    add_inventory_options(parser)
    args = parser.parse_args([])

    assert 'inventory' in args
    assert args.inventory is None
    assert 'listhosts' in args
    assert args.listhosts is False
    assert 'subset' in args
    assert args.subset == C.DEFAULT_SUBSET
