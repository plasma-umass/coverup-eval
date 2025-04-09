# file: lib/ansible/inventory/group.py:260-264
# asked: {"lines": [260, 262, 263, 264], "branches": [[262, 263], [262, 264]]}
# gained: {"lines": [260, 262, 263, 264], "branches": [[262, 263], [262, 264]]}

import pytest
from ansible.inventory.group import Group

@pytest.fixture
def group():
    return Group(name="test_group")

def test_get_hosts_cache_none(group, mocker):
    mocker.patch.object(group, '_get_hosts', return_value=['host1', 'host2'])
    group._hosts_cache = None
    hosts = group.get_hosts()
    assert hosts == ['host1', 'host2']
    assert group._hosts_cache == ['host1', 'host2']

def test_get_hosts_cache_not_none(group, mocker):
    group._hosts_cache = ['host1', 'host2']
    hosts = group.get_hosts()
    assert hosts == ['host1', 'host2']
