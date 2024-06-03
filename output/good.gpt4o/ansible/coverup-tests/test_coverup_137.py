# file lib/ansible/cli/inventory.py:59-96
# lines [59, 60, 61, 62, 64, 65, 66, 67, 70, 71, 73, 76, 77, 78, 79, 80, 81, 84, 85, 86, 87, 88, 89, 92, 93, 95, 96]
# branches []

import pytest
from unittest import mock
from ansible.cli.inventory import InventoryCLI
import argparse

@pytest.fixture
def mock_opt_help(mocker):
    opt_help = mocker.Mock()
    opt_help.UnrecognizedArgument = argparse.Action
    mocker.patch('ansible.cli.inventory.opt_help', opt_help)
    return opt_help

def test_inventory_cli_init_parser(mock_opt_help):
    cli = InventoryCLI(['test'])
    cli.parser = argparse.ArgumentParser()
    cli.init_parser()

    # Check if the parser has the expected arguments
    args = cli.parser.parse_args(['--list'])
    assert args.list is True
    assert args.host is None
    assert args.graph is False
    assert args.yaml is False
    assert args.toml is False
    assert args.show_vars is False
    assert args.export == False
    assert args.output_file is None

    args = cli.parser.parse_args(['--host', 'localhost'])
    assert args.list is False
    assert args.host == 'localhost'
    assert args.graph is False
    assert args.yaml is False
    assert args.toml is False
    assert args.show_vars is False
    assert args.export == False
    assert args.output_file is None

    args = cli.parser.parse_args(['--graph'])
    assert args.list is False
    assert args.host is None
    assert args.graph is True
    assert args.yaml is False
    assert args.toml is False
    assert args.show_vars is False
    assert args.export == False
    assert args.output_file is None

    args = cli.parser.parse_args(['--list', '--yaml'])
    assert args.list is True
    assert args.host is None
    assert args.graph is False
    assert args.yaml is True
    assert args.toml is False
    assert args.show_vars is False
    assert args.export == False
    assert args.output_file is None

    args = cli.parser.parse_args(['--list', '--toml'])
    assert args.list is True
    assert args.host is None
    assert args.graph is False
    assert args.yaml is False
    assert args.toml is True
    assert args.show_vars is False
    assert args.export == False
    assert args.output_file is None

    args = cli.parser.parse_args(['--graph', '--vars'])
    assert args.list is False
    assert args.host is None
    assert args.graph is True
    assert args.yaml is False
    assert args.toml is False
    assert args.show_vars is True
    assert args.export == False
    assert args.output_file is None

    args = cli.parser.parse_args(['--list', '--export'])
    assert args.list is True
    assert args.host is None
    assert args.graph is False
    assert args.yaml is False
    assert args.toml is False
    assert args.show_vars is False
    assert args.export == True
    assert args.output_file is None

    args = cli.parser.parse_args(['--list', '--output', 'output.txt'])
    assert args.list is True
    assert args.host is None
    assert args.graph is False
    assert args.yaml is False
    assert args.toml is False
    assert args.show_vars is False
    assert args.export == False
    assert args.output_file == 'output.txt'
