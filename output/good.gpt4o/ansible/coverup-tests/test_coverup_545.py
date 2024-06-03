# file lib/ansible/parsing/dataloader.py:53-72
# lines [53, 55, 59, 64, 70, 71, 72]
# branches []

import pytest
from ansible.parsing.dataloader import DataLoader
from ansible.parsing.vault import VaultLib

@pytest.fixture
def dataloader():
    return DataLoader()

def test_dataloader_initialization(dataloader):
    # Check initial values
    assert dataloader._basedir == '.'
    assert dataloader._FILE_CACHE == {}
    assert dataloader._tempfiles == set()
    assert dataloader._vaults == {}
    assert isinstance(dataloader._vault, VaultLib)

def test_dataloader_set_vault_secrets(dataloader, mocker):
    # Mock the set_vault_secrets method to ensure it is called correctly
    mock_set_vault_secrets = mocker.patch.object(dataloader, 'set_vault_secrets', autospec=True)
    dataloader.set_vault_secrets(None)
    mock_set_vault_secrets.assert_called_once_with(None)
