# file: lib/ansible/parsing/dataloader.py:53-72
# asked: {"lines": [53, 55, 59, 64, 70, 71, 72], "branches": []}
# gained: {"lines": [53, 55, 59, 64, 70, 71, 72], "branches": []}

import pytest
from ansible.parsing.dataloader import DataLoader
from ansible.parsing.vault import VaultLib

@pytest.fixture
def dataloader():
    return DataLoader()

def test_dataloader_initialization(mocker):
    mock_vault_lib = mocker.patch('ansible.parsing.dataloader.VaultLib', autospec=True)
    mock_set_vault_secrets = mocker.patch.object(DataLoader, 'set_vault_secrets', return_value=None)
    
    dl = DataLoader()
    
    assert dl._basedir == '.'
    assert isinstance(dl._FILE_CACHE, dict)
    assert isinstance(dl._tempfiles, set)
    assert isinstance(dl._vaults, dict)
    assert dl._vault == mock_vault_lib.return_value
    mock_set_vault_secrets.assert_called_once_with(None)
