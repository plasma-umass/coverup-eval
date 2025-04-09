# file: lib/ansible/cli/arguments/option_helpers.py:283-290
# asked: {"lines": [285, 286, 287, 288, 289, 290], "branches": []}
# gained: {"lines": [285, 286, 287, 288, 289, 290], "branches": []}

import pytest
from argparse import ArgumentParser, Namespace
from ansible.cli.arguments.option_helpers import add_inventory_options

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
    args = parser.parse_args(['-l', 'some_pattern'])
    assert args.subset == 'some_pattern'

def test_add_inventory_options_default_limit(parser, monkeypatch):
    from ansible import constants as C
    monkeypatch.setattr(C, 'DEFAULT_SUBSET', 'default_pattern')
    add_inventory_options(parser)
    args = parser.parse_args([])
    assert args.subset == 'default_pattern'
