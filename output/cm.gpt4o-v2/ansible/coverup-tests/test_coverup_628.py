# file: lib/ansible/cli/inventory.py:52-57
# asked: {"lines": [52, 54, 55, 56, 57], "branches": []}
# gained: {"lines": [52, 54, 55, 56, 57], "branches": []}

import pytest
from ansible.cli.inventory import InventoryCLI
from ansible.cli import CLI

def test_inventory_cli_init(monkeypatch):
    # Mock the CLI __init__ to avoid side effects
    def mock_cli_init(self, args, callback=None):
        self.args = args
        self.parser = None
        self.callback = callback

    monkeypatch.setattr(CLI, "__init__", mock_cli_init)

    args = ["arg1", "arg2"]
    cli = InventoryCLI(args)

    assert cli.args == args
    assert cli.vm is None
    assert cli.loader is None
    assert cli.inventory is None
