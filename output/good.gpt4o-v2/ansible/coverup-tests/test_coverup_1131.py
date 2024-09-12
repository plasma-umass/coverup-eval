# file: lib/ansible/plugins/action/include_vars.py:218-247
# asked: {"lines": [226, 227, 228, 229, 230, 231, 233, 234, 236, 237, 238, 239, 240, 241, 242, 244, 245, 247], "branches": [[229, 230], [229, 233], [238, 239], [238, 240], [240, 241], [240, 244]]}
# gained: {"lines": [226, 227, 228, 229, 230, 231, 233, 234, 236, 237, 238, 239, 240, 241, 242, 244, 245, 247], "branches": [[229, 230], [229, 233], [238, 239], [238, 240], [240, 241], [240, 244]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.action.include_vars import ActionModule

@pytest.fixture
def action_module():
    module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    module._loader = MagicMock()
    module.included_files = []
    module.valid_extensions = ['yml', 'yaml', 'json']
    return module

def test_load_files_with_invalid_extension(action_module):
    action_module._is_valid_file_ext = MagicMock(return_value=False)
    failed, err_msg, results = action_module._load_files('invalid.txt', validate_extensions=True)
    assert failed is True
    assert 'invalid.txt does not have a valid extension' in err_msg
    assert results == {}

def test_load_files_with_valid_extension(action_module):
    action_module._is_valid_file_ext = MagicMock(return_value=True)
    action_module._loader._get_file_contents = MagicMock(return_value=(b'{"key": "value"}', False))
    action_module._loader.load = MagicMock(return_value={"key": "value"})
    
    failed, err_msg, results = action_module._load_files('valid.json', validate_extensions=True)
    
    assert failed is False
    assert err_msg == ''
    assert results == {"key": "value"}
    assert 'valid.json' in action_module.included_files

def test_load_files_with_empty_data(action_module):
    action_module._loader._get_file_contents = MagicMock(return_value=(b'', False))
    action_module._loader.load = MagicMock(return_value=None)
    
    failed, err_msg, results = action_module._load_files('empty.json')
    
    assert failed is False
    assert err_msg == ''
    assert results == {}
    assert 'empty.json' in action_module.included_files

def test_load_files_with_invalid_data(action_module):
    action_module._loader._get_file_contents = MagicMock(return_value=(b'not a dict', False))
    action_module._loader.load = MagicMock(return_value="not a dict")
    
    failed, err_msg, results = action_module._load_files('invalid.json')
    
    assert failed is True
    assert 'invalid.json must be stored as a dictionary/hash' in err_msg
    assert results == {}
