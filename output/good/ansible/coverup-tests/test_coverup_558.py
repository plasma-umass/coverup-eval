# file lib/ansible/parsing/dataloader.py:53-72
# lines [53, 55, 59, 64, 70, 71, 72]
# branches []

import pytest
from ansible.parsing.dataloader import DataLoader
from ansible.parsing.vault import VaultLib

@pytest.fixture
def data_loader():
    return DataLoader()

def test_data_loader_initialization(data_loader):
    assert data_loader._basedir == '.'
    assert isinstance(data_loader._FILE_CACHE, dict)
    assert data_loader._FILE_CACHE == {}
    assert isinstance(data_loader._tempfiles, set)
    assert data_loader._tempfiles == set()
    assert isinstance(data_loader._vaults, dict)
    assert data_loader._vaults == {}
    assert isinstance(data_loader._vault, VaultLib)
