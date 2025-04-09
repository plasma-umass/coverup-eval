# file: lib/ansible/vars/manager.py:452-522
# asked: {"lines": [496], "branches": [[484, 491], [491, 514], [495, 496], [500, 502], [502, 505]]}
# gained: {"lines": [496], "branches": [[495, 496]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.vars.manager import VariableManager

@pytest.fixture
def variable_manager():
    vm = VariableManager()
    vm._loader = MagicMock()
    vm._loader.get_basedir.return_value = '/fake/dir'
    vm._inventory = MagicMock()
    vm._inventory.get_groups_dict.return_value = {'group1': ['host1']}
    host1 = MagicMock()
    host1.name = 'host1'
    host2 = MagicMock()
    host2.name = 'host2'
    vm._inventory.get_hosts.side_effect = lambda pattern=None, ignore_restrictions=False: [host1, host2]
    vm._omit_token = 'OMIT'
    vm._options_vars = {'option1': 'value1'}
    vm._hostvars = {'host1': {'var1': 'value1'}}
    return vm

def test_get_magic_variables_with_task_and_inventory(variable_manager):
    play = MagicMock()
    play.roles = []
    play.get_name.return_value = 'test_play'
    play.hosts = 'all'
    play.finalized = False
    play._removed_hosts = []

    task = MagicMock()
    task._role = MagicMock()
    task._role.get_name.return_value = 'test_role'
    task._role._role_path = '/fake/role/path'
    task._role._uuid = '1234-uuid'
    task._role._role_collection = 'test_collection'

    with patch('ansible.vars.manager.Templar') as TemplarMock:
        templar_instance = TemplarMock.return_value
        templar_instance.is_template.return_value = True

        variables = variable_manager._get_magic_variables(play, None, task, include_hostvars=True, include_delegate_to=False)

        assert variables['role_name'] == 'test_role'
        assert variables['role_path'] == '/fake/role/path'
        assert variables['role_uuid'] == '1234-uuid'
        assert variables['ansible_collection_name'] == 'test_collection'
        assert variables['ansible_role_name'] == 'test_role'
        assert variables['groups'] == {'group1': ['host1']}
        assert variables['ansible_play_hosts_all'] == ['host1', 'host2']
        assert variables['ansible_play_hosts'] == ['host1', 'host2']
        assert variables['ansible_play_batch'] == ['host1', 'host2']
        assert variables['play_hosts'] == ['host1', 'host2']
        assert variables['omit'] == 'OMIT'
        assert variables['option1'] == 'value1'
        assert variables['hostvars'] == {'host1': {'var1': 'value1'}}

def test_get_magic_variables_without_task(variable_manager):
    play = MagicMock()
    play.roles = []
    play.get_name.return_value = 'test_play'
    play.hosts = 'all'
    play.finalized = False
    play._removed_hosts = []

    with patch('ansible.vars.manager.Templar') as TemplarMock:
        templar_instance = TemplarMock.return_value
        templar_instance.is_template.return_value = True

        variables = variable_manager._get_magic_variables(play, None, None, include_hostvars=True, include_delegate_to=False)

        assert 'role_name' not in variables
        assert 'role_path' not in variables
        assert 'role_uuid' not in variables
        assert 'ansible_collection_name' not in variables
        assert 'ansible_role_name' not in variables
        assert variables['groups'] == {'group1': ['host1']}
        assert variables['ansible_play_hosts_all'] == ['host1', 'host2']
        assert variables['ansible_play_hosts'] == ['host1', 'host2']
        assert variables['ansible_play_batch'] == ['host1', 'host2']
        assert variables['play_hosts'] == ['host1', 'host2']
        assert variables['omit'] == 'OMIT'
        assert variables['option1'] == 'value1'
        assert variables['hostvars'] == {'host1': {'var1': 'value1'}}
