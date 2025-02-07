# file: lib/ansible/parsing/dataloader.py:75-76
# asked: {"lines": [75, 76], "branches": []}
# gained: {"lines": [75, 76], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.parsing.dataloader import DataLoader

def test_set_vault_secrets():
    dataloader = DataLoader()
    mock_vault_secrets = {'secret_key': 'secret_value'}
    
    dataloader.set_vault_secrets(mock_vault_secrets)
    
    assert dataloader._vault.secrets == mock_vault_secrets
