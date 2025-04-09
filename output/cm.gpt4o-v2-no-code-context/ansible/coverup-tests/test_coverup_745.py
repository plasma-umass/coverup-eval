# file: lib/ansible/playbook/role/metadata.py:112-119
# asked: {"lines": [112, 119], "branches": []}
# gained: {"lines": [112], "branches": []}

import pytest
from ansible.playbook.role.metadata import RoleMetadata

class MockBase:
    pass

class MockCollectionSearch:
    pass

class MockGalaxyInfo:
    pass

@pytest.fixture
def role_metadata(monkeypatch):
    class MockRoleMetadata(RoleMetadata, MockBase, MockCollectionSearch):
        def __init__(self):
            pass

    def mock_galaxy_info(self, attr, ds):
        return MockGalaxyInfo()

    monkeypatch.setattr(MockRoleMetadata, '_load_galaxy_info', mock_galaxy_info)
    return MockRoleMetadata()

def test_load_galaxy_info(role_metadata):
    attr = 'galaxy_info'
    ds = {'some_key': 'some_value'}
    
    result = role_metadata._load_galaxy_info(attr, ds)
    
    assert isinstance(result, MockGalaxyInfo)
    assert result is not None
