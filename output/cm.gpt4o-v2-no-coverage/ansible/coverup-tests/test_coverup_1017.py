# file: lib/ansible/parsing/dataloader.py:75-76
# asked: {"lines": [75, 76], "branches": []}
# gained: {"lines": [75, 76], "branches": []}

import pytest
from ansible.parsing.dataloader import DataLoader
from ansible.parsing.vault import VaultLib

@pytest.fixture
def dataloader():
    return DataLoader()

def test_set_vault_secrets(dataloader):
    secrets = {'secret1': 'value1', 'secret2': 'value2'}
    dataloader.set_vault_secrets(secrets)
    assert dataloader._vault.secrets == secrets

def test_set_vault_secrets_none(dataloader):
    dataloader.set_vault_secrets(None)
    assert dataloader._vault.secrets is None
