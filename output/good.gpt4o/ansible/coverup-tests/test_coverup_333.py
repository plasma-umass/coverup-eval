# file lib/ansible/modules/debconf.py:113-126
# lines [113, 114, 115, 117, 118, 120, 122, 123, 124, 126]
# branches ['117->118', '117->120', '122->123', '122->126']

import pytest
from unittest import mock
from ansible.module_utils.basic import AnsibleModule

@pytest.fixture
def mock_module(mocker):
    mocker.patch('ansible.module_utils.basic._ANSIBLE_ARGS', b'{"ANSIBLE_MODULE_ARGS": {}}')
    module = AnsibleModule(argument_spec={})
    return module

def test_get_selections_success(mocker, mock_module):
    pkg = 'testpkg'
    
    mocker.patch.object(mock_module, 'get_bin_path', return_value='/usr/bin/debconf-show')
    mocker.patch.object(mock_module, 'run_command', return_value=(0, 'key1: value1\nkey2: value2\n*key3: value3', ''))
    
    from ansible.modules.debconf import get_selections
    selections = get_selections(mock_module, pkg)
    
    assert selections == {
        'key1': 'value1',
        'key2': 'value2',
        'key3': 'value3'
    }

def test_get_selections_failure(mocker, mock_module):
    pkg = 'testpkg'
    
    mocker.patch.object(mock_module, 'get_bin_path', return_value='/usr/bin/debconf-show')
    mocker.patch.object(mock_module, 'run_command', return_value=(1, '', 'error message'))
    mocker.patch.object(mock_module, 'fail_json', side_effect=Exception('error message'))
    
    from ansible.modules.debconf import get_selections
    
    with pytest.raises(Exception, match='error message'):
        get_selections(mock_module, pkg)
