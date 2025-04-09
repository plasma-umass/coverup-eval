# file: lib/ansible/inventory/host.py:144-148
# asked: {"lines": [146], "branches": [[145, 146]]}
# gained: {"lines": [146], "branches": [[145, 146]]}

import pytest
from unittest.mock import MagicMock
from ansible.inventory.host import Host
from ansible.module_utils.common._collections_compat import MutableMapping, Mapping

class TestHost:
    @pytest.fixture
    def host(self):
        return Host()

    def test_set_variable_with_mapping(self, host, mocker):
        mocker.patch.object(host, 'vars', new_callable=dict)
        host.vars = {'existing_key': MagicMock(spec=MutableMapping)}
        new_value = MagicMock(spec=Mapping)
        
        host.set_variable('existing_key', new_value)
        
        assert 'existing_key' in host.vars
        assert host.vars['existing_key'] == new_value

    def test_set_variable_without_mapping(self, host, mocker):
        mocker.patch.object(host, 'vars', new_callable=dict)
        host.vars = {'existing_key': 'existing_value'}
        new_value = 'new_value'
        
        host.set_variable('existing_key', new_value)
        
        assert host.vars['existing_key'] == new_value
