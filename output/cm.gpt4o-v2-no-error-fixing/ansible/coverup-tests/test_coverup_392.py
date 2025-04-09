# file: lib/ansible/inventory/host.py:153-159
# asked: {"lines": [153, 154, 155, 156, 157, 159], "branches": []}
# gained: {"lines": [153, 154, 155, 156, 157, 159], "branches": []}

import pytest
from ansible.inventory.host import Host

@pytest.fixture
def host():
    return Host(name="test.example.com")

def test_get_magic_vars(host, mocker):
    mock_group = mocker.Mock()
    mock_group.name = "group1"
    host.groups = [mock_group]

    results = host.get_magic_vars()

    assert results['inventory_hostname'] == "test.example.com"
    assert results['inventory_hostname_short'] == "test"
    assert results['group_names'] == ["group1"]
