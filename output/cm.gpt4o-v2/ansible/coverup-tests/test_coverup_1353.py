# file: lib/ansible/plugins/action/include_vars.py:27-46
# asked: {"lines": [28, 29, 31, 32, 34, 36, 37, 39, 40, 42, 43, 44, 45], "branches": [[28, 29], [28, 31], [31, 32], [31, 34], [36, 37], [36, 39], [39, 40], [39, 42], [42, 0], [42, 43]]}
# gained: {"lines": [28, 29, 31, 32, 34, 36, 37, 39, 40, 42, 43, 44, 45], "branches": [[28, 29], [28, 31], [31, 32], [31, 34], [36, 37], [36, 39], [39, 40], [39, 42], [42, 0], [42, 43]]}

import pytest
from ansible.plugins.action.include_vars import ActionModule
from ansible.module_utils.six import string_types

class MockTask:
    pass

class MockConnection:
    pass

class MockPlayContext:
    pass

class MockLoader:
    pass

class MockTemplar:
    pass

class MockSharedLoaderObj:
    pass

@pytest.fixture
def action_module():
    task = MockTask()
    connection = MockConnection()
    play_context = MockPlayContext()
    loader = MockLoader()
    templar = MockTemplar()
    shared_loader_obj = MockSharedLoaderObj()
    return ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)

def test_set_dir_defaults_no_depth(action_module):
    action_module.depth = None
    action_module.files_matching = None
    action_module.ignore_files = None
    action_module._set_dir_defaults()
    assert action_module.depth == 0
    assert action_module.matcher is None
    assert action_module.ignore_files == []

def test_set_dir_defaults_with_files_matching(action_module):
    action_module.depth = 1
    action_module.files_matching = '.*\.yml'
    action_module.ignore_files = None
    action_module._set_dir_defaults()
    assert action_module.matcher is not None
    assert action_module.matcher.pattern == '.*\.yml'

def test_set_dir_defaults_ignore_files_string(action_module):
    action_module.depth = 1
    action_module.files_matching = None
    action_module.ignore_files = 'file1 file2'
    action_module._set_dir_defaults()
    assert action_module.ignore_files == ['file1', 'file2']

def test_set_dir_defaults_ignore_files_dict(action_module):
    action_module.depth = 1
    action_module.files_matching = None
    action_module.ignore_files = {'key': 'value'}
    result = action_module._set_dir_defaults()
    assert result == {'failed': True, 'message': "{'key': 'value'} must be a list"}
