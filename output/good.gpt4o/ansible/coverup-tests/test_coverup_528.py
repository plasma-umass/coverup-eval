# file lib/ansible/cli/arguments/option_helpers.py:283-290
# lines [283, 285, 286, 287, 288, 289, 290]
# branches []

import pytest
from argparse import ArgumentParser
from ansible.cli.arguments.option_helpers import add_inventory_options
from ansible import constants as C

def test_add_inventory_options():
    parser = ArgumentParser()
    add_inventory_options(parser)
    
    args = parser.parse_args(['-i', 'inventory_path', '--list-hosts', '-l', 'subset_pattern'])
    
    assert args.inventory == ['inventory_path']
    assert args.listhosts is True
    assert args.subset == 'subset_pattern'

    args = parser.parse_args(['--inventory', 'inventory_path', '--inventory-file', 'deprecated_path'])
    
    assert args.inventory == ['inventory_path', 'deprecated_path']
    assert args.listhosts is False
    assert args.subset == C.DEFAULT_SUBSET  # Use the actual default value from constants

@pytest.fixture(autouse=True)
def cleanup(mocker):
    yield
    mocker.stopall()
