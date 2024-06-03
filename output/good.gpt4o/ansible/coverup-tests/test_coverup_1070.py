# file lib/ansible/plugins/action/include_vars.py:218-247
# lines [226, 227, 228, 229, 230, 231, 233, 234, 236, 237, 238, 239, 240, 241, 242, 244, 245, 247]
# branches ['229->230', '229->233', '238->239', '238->240', '240->241', '240->244']

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.action.include_vars import ActionModule
from ansible.errors import AnsibleError

@pytest.fixture
def action_module():
    action = ActionModule(task=MagicMock(), connection=MagicMock(), play_context=MagicMock(), loader=MagicMock(), templar=MagicMock(), shared_loader_obj=MagicMock())
    action._loader = MagicMock()
    action.valid_extensions = ['yml', 'yaml', 'json']
    action.included_files = []
    return action

def test_load_files_invalid_extension(action_module):
    filename = 'invalid_extension.txt'
    action_module._is_valid_file_ext = MagicMock(return_value=False)
    
    failed, err_msg, results = action_module._load_files(filename, validate_extensions=True)
    
    assert failed is True
    assert err_msg == f'{filename} does not have a valid extension: yml, yaml, json'
    assert results == {}

def test_load_files_not_dict(action_module):
    filename = 'not_a_dict.yml'
    action_module._is_valid_file_ext = MagicMock(return_value=True)
    action_module._loader._get_file_contents = MagicMock(return_value=(b'not_a_dict_content', False))
    action_module._loader.load = MagicMock(return_value='not_a_dict_content')
    
    failed, err_msg, results = action_module._load_files(filename, validate_extensions=True)
    
    assert failed is True
    assert err_msg == f'{filename} must be stored as a dictionary/hash'
    assert results == {}

def test_load_files_success(action_module):
    filename = 'valid_file.yml'
    action_module._is_valid_file_ext = MagicMock(return_value=True)
    action_module._loader._get_file_contents = MagicMock(return_value=(b'key: value', False))
    action_module._loader.load = MagicMock(return_value={'key': 'value'})
    
    failed, err_msg, results = action_module._load_files(filename, validate_extensions=True)
    
    assert failed is False
    assert err_msg == ''
    assert results == {'key': 'value'}
    assert filename in action_module.included_files
