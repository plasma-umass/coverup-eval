# file: lib/ansible/cli/vault.py:431-438
# asked: {"lines": [431, 434, 435, 437, 438], "branches": [[434, 435], [434, 437]]}
# gained: {"lines": [431, 434, 435, 437, 438], "branches": [[434, 435], [434, 437]]}

import pytest
from ansible.cli.vault import VaultCLI
from ansible.errors import AnsibleOptionsError
from ansible import context
from ansible.utils.context_objects import CLIArgs

def test_execute_create_with_valid_args(monkeypatch):
    # Arrange
    cli = VaultCLI(['create'])
    test_args = ['testfile.yml']
    monkeypatch.setattr(context, 'CLIARGS', CLIArgs({'args': test_args}))

    class MockEditor:
        def create_file(self, filename, secret, vault_id=None):
            assert filename == 'testfile.yml'
            assert secret is None
            assert vault_id is None

    cli.editor = MockEditor()

    # Act
    cli.execute_create()

def test_execute_create_with_invalid_args(monkeypatch):
    # Arrange
    cli = VaultCLI(['create'])
    monkeypatch.setattr(context, 'CLIARGS', CLIArgs({'args': ['file1.yml', 'file2.yml']}))

    # Act & Assert
    with pytest.raises(AnsibleOptionsError, match="ansible-vault create can take only one filename argument"):
        cli.execute_create()
