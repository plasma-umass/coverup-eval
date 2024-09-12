# file: lib/ansible/inventory/host.py:161-162
# asked: {"lines": [161, 162], "branches": []}
# gained: {"lines": [161, 162], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.inventory.host import Host
from ansible.utils.vars import combine_vars

@pytest.fixture
def host():
    host = Host()
    host.vars = {'var1': 'value1'}
    host.name = 'testhost'
    host.get_groups = MagicMock(return_value=[])
    return host

def test_get_vars(host, mocker):
    mocker.patch('ansible.inventory.host.Host.get_magic_vars', return_value={'inventory_hostname': 'testhost', 'inventory_hostname_short': 'testhost', 'group_names': []})
    result = host.get_vars()
    expected = combine_vars({'var1': 'value1'}, {'inventory_hostname': 'testhost', 'inventory_hostname_short': 'testhost', 'group_names': []})
    assert result == expected
