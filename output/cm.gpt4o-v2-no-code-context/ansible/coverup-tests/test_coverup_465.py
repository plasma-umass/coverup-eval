# file: lib/ansible/cli/arguments/option_helpers.py:283-290
# asked: {"lines": [283, 285, 286, 287, 288, 289, 290], "branches": []}
# gained: {"lines": [283, 285, 286, 287, 288, 289, 290], "branches": []}

import pytest
from argparse import ArgumentParser
from ansible.cli.arguments.option_helpers import add_inventory_options
from ansible import constants as C

@pytest.fixture
def parser():
    return ArgumentParser()

def test_add_inventory_options_inventory(parser):
    add_inventory_options(parser)
    args = parser.parse_args(['-i', 'inventory_path'])
    assert args.inventory == ['inventory_path']

def test_add_inventory_options_inventory_file(parser):
    add_inventory_options(parser)
    args = parser.parse_args(['--inventory-file', 'inventory_path'])
    assert args.inventory == ['inventory_path']

def test_add_inventory_options_list_hosts(parser):
    add_inventory_options(parser)
    args = parser.parse_args(['--list-hosts'])
    assert args.listhosts is True

def test_add_inventory_options_limit(parser):
    add_inventory_options(parser)
    args = parser.parse_args(['-l', 'pattern'])
    assert args.subset == 'pattern'

def test_add_inventory_options_default_limit(parser):
    add_inventory_options(parser)
    args = parser.parse_args([])
    assert args.subset == C.DEFAULT_SUBSET
