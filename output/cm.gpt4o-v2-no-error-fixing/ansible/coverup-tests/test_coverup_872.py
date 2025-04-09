# file: lib/ansible/plugins/action/include_vars.py:218-247
# asked: {"lines": [226, 227, 228, 229, 230, 231, 233, 234, 236, 237, 238, 239, 240, 241, 242, 244, 245, 247], "branches": [[229, 230], [229, 233], [238, 239], [238, 240], [240, 241], [240, 244]]}
# gained: {"lines": [226, 227, 228, 229, 230, 231, 233, 234, 236, 237, 238, 239, 240, 241, 242, 244, 245, 247], "branches": [[229, 230], [229, 233], [238, 239], [238, 240], [240, 241], [240, 244]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.action.include_vars import ActionModule
from ansible.module_utils._text import to_native

@pytest.fixture
def action_module():
    module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    module._loader = MagicMock()
    module.included_files = []
    module.valid_extensions = ['yml', 'yaml', 'json']
    return module

def test_load_files_with_invalid_extension(action_module):
    action_module._is_valid_file_ext = MagicMock(return_value=False)
    filename = 'test.txt'
    
    failed, err_msg, results = action_module._load_files(filename, validate_extensions=True)
    
    assert failed is True
    assert err_msg == f'{to_native(filename)} does not have a valid extension: yml, yaml, json'
    assert results == {}

def test_load_files_with_valid_extension_and_empty_data(action_module):
    action_module._is_valid_file_ext = MagicMock(return_value=True)
    action_module._loader._get_file_contents = MagicMock(return_value=(b'', False))
    action_module._loader.load = MagicMock(return_value=None)
    filename = 'test.yml'
    
    failed, err_msg, results = action_module._load_files(filename, validate_extensions=True)
    
    assert failed is False
    assert err_msg == ''
    assert results == {}
    assert filename in action_module.included_files

def test_load_files_with_valid_extension_and_non_dict_data(action_module):
    action_module._is_valid_file_ext = MagicMock(return_value=True)
    action_module._loader._get_file_contents = MagicMock(return_value=(b'non-dict', False))
    action_module._loader.load = MagicMock(return_value='non-dict')
    filename = 'test.yml'
    
    failed, err_msg, results = action_module._load_files(filename, validate_extensions=True)
    
    assert failed is True
    assert err_msg == f'{to_native(filename)} must be stored as a dictionary/hash'
    assert results == {}

def test_load_files_with_valid_extension_and_dict_data(action_module):
    action_module._is_valid_file_ext = MagicMock(return_value=True)
    action_module._loader._get_file_contents = MagicMock(return_value=(b'dict_data', False))
    action_module._loader.load = MagicMock(return_value={'key': 'value'})
    filename = 'test.yml'
    
    failed, err_msg, results = action_module._load_files(filename, validate_extensions=True)
    
    assert failed is False
    assert err_msg == ''
    assert results == {'key': 'value'}
    assert filename in action_module.included_files
