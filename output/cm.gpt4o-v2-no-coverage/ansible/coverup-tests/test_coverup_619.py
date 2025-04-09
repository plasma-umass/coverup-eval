# file: lib/ansible/parsing/dataloader.py:53-72
# asked: {"lines": [53, 55, 59, 64, 70, 71, 72], "branches": []}
# gained: {"lines": [53, 55, 59, 64, 70, 71, 72], "branches": []}

import pytest
from ansible.parsing.dataloader import DataLoader
from ansible.parsing.vault import VaultLib

@pytest.fixture
def dataloader():
    return DataLoader()

def test_dataloader_initialization(dataloader):
    assert dataloader._basedir == '.'
    assert isinstance(dataloader._FILE_CACHE, dict)
    assert isinstance(dataloader._tempfiles, set)
    assert dataloader._vaults == {}
    assert isinstance(dataloader._vault, VaultLib)
    assert dataloader._vault.secrets is None

def test_set_vault_secrets(dataloader):
    secrets = {'secret_key': 'secret_value'}
    dataloader.set_vault_secrets(secrets)
    assert dataloader._vault.secrets == secrets

    # Clean up
    dataloader.set_vault_secrets(None)
    assert dataloader._vault.secrets is None
