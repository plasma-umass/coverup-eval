# file: lib/ansible/parsing/dataloader.py:53-72
# asked: {"lines": [53, 55, 59, 64, 70, 71, 72], "branches": []}
# gained: {"lines": [53, 55, 59, 64, 70, 71, 72], "branches": []}

import pytest
from ansible.parsing.dataloader import DataLoader
from ansible.parsing.vault import VaultLib

def test_dataloader_init(monkeypatch):
    # Arrange
    def mock_set_vault_secrets(self, vault_secrets):
        self._vault.secrets = vault_secrets

    monkeypatch.setattr(DataLoader, 'set_vault_secrets', mock_set_vault_secrets)

    # Act
    loader = DataLoader()

    # Assert
    assert loader._basedir == '.'
    assert loader._FILE_CACHE == {}
    assert loader._tempfiles == set()
    assert loader._vaults == {}
    assert isinstance(loader._vault, VaultLib)
    assert loader._vault.secrets is None
