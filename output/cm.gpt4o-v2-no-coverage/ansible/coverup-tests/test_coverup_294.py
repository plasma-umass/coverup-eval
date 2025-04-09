# file: lib/ansible/inventory/host.py:105-113
# asked: {"lines": [105, 107, 108, 109, 111, 112, 113], "branches": [[107, 108], [107, 111], [108, 0], [108, 109], [111, 0], [111, 112], [112, 111], [112, 113]]}
# gained: {"lines": [105, 107, 108, 109, 111, 112, 113], "branches": [[107, 108], [107, 111], [108, 0], [108, 109], [111, 0], [111, 112], [112, 111], [112, 113]]}

import pytest
from ansible.inventory.host import Host

@pytest.fixture
def host():
    return Host(name="test_host")

def test_populate_ancestors_no_additions(host, mocker):
    mock_add_group = mocker.patch.object(host, 'add_group')
    host.groups = ['group1', 'group2']
    
    host.populate_ancestors()
    
    mock_add_group.assert_any_call('group1')
    mock_add_group.assert_any_call('group2')
    assert mock_add_group.call_count == 2

def test_populate_ancestors_with_additions(host):
    host.groups = ['group1']
    additions = ['group2', 'group3']
    
    host.populate_ancestors(additions)
    
    assert 'group2' in host.groups
    assert 'group3' in host.groups
    assert len(host.groups) == 3

def test_populate_ancestors_with_existing_additions(host):
    host.groups = ['group1']
    additions = ['group1', 'group2']
    
    host.populate_ancestors(additions)
    
    assert 'group1' in host.groups
    assert 'group2' in host.groups
    assert len(host.groups) == 2
