# file: lib/ansible/plugins/action/include_vars.py:218-247
# asked: {"lines": [218, 226, 227, 228, 229, 230, 231, 233, 234, 236, 237, 238, 239, 240, 241, 242, 244, 245, 247], "branches": [[229, 230], [229, 233], [238, 239], [238, 240], [240, 241], [240, 244]]}
# gained: {"lines": [218, 226, 227, 228, 229, 230, 231, 233, 234, 236, 237, 238, 239, 240, 241, 242, 244, 245, 247], "branches": [[229, 230], [229, 233], [238, 239], [238, 240], [240, 241], [240, 244]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.action.include_vars import ActionModule
from ansible.module_utils._text import to_native

@pytest.fixture
def action_module():
    module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    module._loader = MagicMock()
    module.included_files = []
    module.valid_extensions = ['yaml', 'yml', 'json']
    return module

def test_load_files_valid_extension(action_module):
    action_module._loader._get_file_contents.return_value = (b'{"key": "value"}', False)
    action_module._loader.load.return_value = {"key": "value"}

    failed, err_msg, results = action_module._load_files('test.yml', validate_extensions=True)

    assert not failed
    assert err_msg == ''
    assert results == {"key": "value"}
    assert 'test.yml' in action_module.included_files

def test_load_files_invalid_extension(action_module):
    action_module._is_valid_file_ext = MagicMock(return_value=False)

    failed, err_msg, results = action_module._load_files('test.txt', validate_extensions=True)

    assert failed
    assert err_msg == 'test.txt does not have a valid extension: yaml, yml, json'
    assert results == {}

def test_load_files_not_dict(action_module):
    action_module._loader._get_file_contents.return_value = (b'["item1", "item2"]', False)
    action_module._loader.load.return_value = ["item1", "item2"]

    failed, err_msg, results = action_module._load_files('test.yml', validate_extensions=False)

    assert failed
    assert err_msg == 'test.yml must be stored as a dictionary/hash'
    assert results == {}

def test_load_files_empty_file(action_module):
    action_module._loader._get_file_contents.return_value = (b'', False)
    action_module._loader.load.return_value = None

    failed, err_msg, results = action_module._load_files('test.yml', validate_extensions=False)

    assert not failed
    assert err_msg == ''
    assert results == {}
    assert 'test.yml' in action_module.included_files
