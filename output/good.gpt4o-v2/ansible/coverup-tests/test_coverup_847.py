# file: lib/ansible/playbook/role/metadata.py:112-119
# asked: {"lines": [112, 119], "branches": []}
# gained: {"lines": [112, 119], "branches": []}

import pytest
from ansible.playbook.role.metadata import RoleMetadata

@pytest.fixture
def role_metadata():
    return RoleMetadata()

def test_load_galaxy_info(role_metadata, mocker):
    mock_attr = mocker.Mock()
    mock_ds = mocker.Mock()
    
    result = role_metadata._load_galaxy_info(mock_attr, mock_ds)
    
    assert result == mock_ds
