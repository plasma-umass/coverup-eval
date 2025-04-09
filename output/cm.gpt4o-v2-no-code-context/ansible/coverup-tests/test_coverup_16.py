# file: lib/ansible/vars/manager.py:452-522
# asked: {"lines": [452, 458, 459, 460, 461, 463, 465, 467, 470, 473, 476, 479, 481, 483, 484, 485, 486, 487, 488, 489, 491, 492, 493, 494, 495, 496, 498, 500, 501, 502, 503, 505, 506, 507, 511, 514, 516, 517, 519, 520, 522], "branches": [[463, 465], [463, 483], [483, 484], [483, 491], [484, 485], [484, 491], [491, 492], [491, 514], [493, 494], [493, 514], [495, 496], [495, 498], [500, 501], [500, 502], [502, 503], [502, 505], [516, 517], [516, 519], [519, 520], [519, 522]]}
# gained: {"lines": [452, 458, 459, 460, 461, 463, 465, 467, 470, 473, 476, 479, 481, 483, 484, 485, 486, 487, 488, 489, 491, 492, 493, 494, 495, 498, 500, 501, 502, 503, 505, 506, 507, 511, 514, 516, 517, 519, 520, 522], "branches": [[463, 465], [463, 483], [483, 484], [483, 491], [484, 485], [491, 492], [493, 494], [493, 514], [495, 498], [500, 501], [502, 503], [516, 517], [516, 519], [519, 520], [519, 522]]}

import pytest
import os
import sys
from unittest.mock import MagicMock, patch
from ansible.vars.manager import VariableManager
from ansible.template import Templar
from ansible.utils.vars import load_options_vars

@pytest.fixture
def variable_manager():
    vm = VariableManager()
    vm._loader = MagicMock()
    vm._loader.get_basedir.return_value = '/fake/dir'
    vm._inventory = MagicMock()
    vm._omit_token = 'OMIT'
    vm._options_vars = {'option1': 'value1', 'option2': 'value2'}
    vm._hostvars = {'host1': {'var1': 'value1'}}
    return vm

@pytest.fixture
def play():
    play = MagicMock()
    play.roles = []
    play.get_name.return_value = 'test_play'
    play.hosts = 'all'
    play.finalized = False
    play._removed_hosts = []
    return play

@pytest.fixture
def task():
    task = MagicMock()
    task._role = MagicMock()
    task._role.get_name.return_value = 'test_role'
    task._role._role_path = '/fake/role/path'
    task._role._uuid = '1234-5678'
    task._role._role_collection = 'test_collection'
    return task

def test_get_magic_variables_play(variable_manager, play):
    result = variable_manager._get_magic_variables(play, None, None, False, False)
    assert result['playbook_dir'] == os.path.abspath('/fake/dir')
    assert result['ansible_playbook_python'] == sys.executable
    assert 'ansible_config_file' in result
    assert result['ansible_play_name'] == 'test_play'

def test_get_magic_variables_task(variable_manager, task):
    result = variable_manager._get_magic_variables(None, None, task, False, False)
    assert result['role_name'] == 'test_role'
    assert result['role_path'] == '/fake/role/path'
    assert result['role_uuid'] == '1234-5678'
    assert result['ansible_collection_name'] == 'test_collection'
    assert result['ansible_role_name'] == 'test_role'

def test_get_magic_variables_inventory(variable_manager, play):
    variable_manager._inventory.get_groups_dict.return_value = {'group1': ['host1']}
    host1 = MagicMock()
    host1.name = 'host1'
    host2 = MagicMock()
    host2.name = 'host2'
    variable_manager._inventory.get_hosts.return_value = [host1, host2]
    templar = Templar(loader=variable_manager._loader)
    with patch.object(Templar, 'is_template', return_value=False):
        result = variable_manager._get_magic_variables(play, None, None, False, False)
    assert result['groups'] == {'group1': ['host1']}
    assert result['ansible_play_hosts_all'] == ['host1', 'host2']
    assert result['ansible_play_hosts'] == ['host1', 'host2']
    assert result['ansible_play_batch'] == ['host1', 'host2']
    assert result['play_hosts'] == ['host1', 'host2']

def test_get_magic_variables_options_vars(variable_manager):
    result = variable_manager._get_magic_variables(None, None, None, False, False)
    assert result['option1'] == 'value1'
    assert result['option2'] == 'value2'

def test_get_magic_variables_hostvars(variable_manager):
    result = variable_manager._get_magic_variables(None, None, None, True, False)
    assert result['hostvars'] == {'host1': {'var1': 'value1'}}
