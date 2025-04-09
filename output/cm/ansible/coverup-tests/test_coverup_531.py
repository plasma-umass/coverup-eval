# file lib/ansible/cli/arguments/option_helpers.py:283-290
# lines [283, 285, 286, 287, 288, 289, 290]
# branches []

import pytest
from ansible.cli.arguments.option_helpers import add_inventory_options
from argparse import ArgumentParser
from unittest.mock import MagicMock

@pytest.fixture
def parser():
    return ArgumentParser()

def test_add_inventory_options(parser):
    add_inventory_options(parser)
    args = parser.parse_args(['-i', 'localhost,', '--list-hosts', '-l', 'web'])
    assert 'localhost,' in args.inventory
    assert args.listhosts is True
    assert args.subset == 'web'

    args = parser.parse_args(['--inventory', 'localhost,', '--inventory-file', 'test_inventory'])
    assert 'localhost,' in args.inventory
    assert 'test_inventory' in args.inventory

    args = parser.parse_args(['--limit', 'all'])
    assert args.subset == 'all'

    # Cleanup is not necessary as the parser is a local fixture and does not affect global state.
