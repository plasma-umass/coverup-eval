# file: lib/ansible/executor/task_result.py:108-154
# asked: {"lines": [108, 113, 116, 118, 120, 122, 124, 125, 126, 127, 128, 129, 131, 132, 135, 136, 137, 139, 140, 141, 144, 145, 146, 149, 152, 154], "branches": [[116, 118], [116, 120], [124, 125], [124, 131], [125, 124], [125, 126], [127, 124], [127, 128], [128, 127], [128, 129], [131, 132], [131, 140], [135, 136], [135, 139], [136, 135], [136, 137], [140, 141], [140, 152], [144, 145], [144, 149], [145, 144], [145, 146]]}
# gained: {"lines": [108, 113, 116, 118, 120, 122, 124, 125, 126, 127, 128, 129, 131, 132, 135, 136, 137, 139, 140, 141, 144, 145, 146, 149, 152, 154], "branches": [[116, 118], [116, 120], [124, 125], [124, 131], [125, 126], [127, 124], [127, 128], [128, 129], [131, 132], [131, 140], [135, 136], [135, 139], [136, 137], [140, 141], [144, 145], [144, 149], [145, 144], [145, 146]]}

import pytest
from unittest.mock import Mock, patch
from ansible.executor.task_result import TaskResult

# Mock constants and functions used in TaskResult
C = Mock()
C._ACTION_DEBUG = ['debug']
_IGNORE = ('ignore_this',)
_SUB_PRESERVE = {'sub_key': ['key1', 'key2']}
_PRESERVE = ['preserve_this']
CLEAN_EXCEPTIONS = ['exception_key']

def module_response_deepcopy(result):
    return result.copy()

def strip_internal_keys(result, exceptions):
    for key in list(result.keys()):
        if key not in exceptions:
            del result[key]

@pytest.fixture
def task_result():
    task = Mock()
    task.action = 'debug'
    task.no_log = False
    host = Mock()
    result = {
        'key1': 'value1',
        'key2': 'value2',
        'sub_key': {
            'key1': 'sub_value1',
            'key2': 'sub_value2'
        },
        'ignore_this': 'ignore_value',
        '_ansible_no_log': False
    }
    task_fields = {}
    return TaskResult(host, task, result, task_fields)

def test_clean_copy_debug_action(task_result, monkeypatch):
    monkeypatch.setattr('ansible.executor.task_result._IGNORE', _IGNORE)
    monkeypatch.setattr('ansible.executor.task_result._SUB_PRESERVE', _SUB_PRESERVE)
    monkeypatch.setattr('ansible.executor.task_result._PRESERVE', _PRESERVE)
    monkeypatch.setattr('ansible.executor.task_result.CLEAN_EXCEPTIONS', CLEAN_EXCEPTIONS)
    monkeypatch.setattr('ansible.executor.task_result.module_response_deepcopy', module_response_deepcopy)
    monkeypatch.setattr('ansible.executor.task_result.strip_internal_keys', strip_internal_keys)
    
    task_result._task.action = 'debug'
    clean_result = task_result.clean_copy()
    
    assert 'ignore_this' not in clean_result._result
    assert clean_result._result['sub_key']['key1'] == 'sub_value1'
    assert clean_result._result['sub_key']['key2'] == 'sub_value2'

def test_clean_copy_no_log(task_result, monkeypatch):
    monkeypatch.setattr('ansible.executor.task_result._IGNORE', _IGNORE)
    monkeypatch.setattr('ansible.executor.task_result._SUB_PRESERVE', _SUB_PRESERVE)
    monkeypatch.setattr('ansible.executor.task_result._PRESERVE', _PRESERVE)
    monkeypatch.setattr('ansible.executor.task_result.CLEAN_EXCEPTIONS', CLEAN_EXCEPTIONS)
    monkeypatch.setattr('ansible.executor.task_result.module_response_deepcopy', module_response_deepcopy)
    monkeypatch.setattr('ansible.executor.task_result.strip_internal_keys', strip_internal_keys)
    
    task_result._task.no_log = True
    task_result._result['preserve_this'] = 'preserved_value'
    clean_result = task_result.clean_copy()
    
    assert clean_result._result['censored'] == "the output has been hidden due to the fact that 'no_log: true' was specified for this result"
    assert clean_result._result['preserve_this'] == 'preserved_value'

def test_clean_copy_ansible_no_log(task_result, monkeypatch):
    monkeypatch.setattr('ansible.executor.task_result._IGNORE', _IGNORE)
    monkeypatch.setattr('ansible.executor.task_result._SUB_PRESERVE', _SUB_PRESERVE)
    monkeypatch.setattr('ansible.executor.task_result._PRESERVE', _PRESERVE)
    monkeypatch.setattr('ansible.executor.task_result.CLEAN_EXCEPTIONS', CLEAN_EXCEPTIONS)
    monkeypatch.setattr('ansible.executor.task_result.module_response_deepcopy', module_response_deepcopy)
    monkeypatch.setattr('ansible.executor.task_result.strip_internal_keys', strip_internal_keys)
    
    task_result._result['_ansible_no_log'] = True
    task_result._result['preserve_this'] = 'preserved_value'
    clean_result = task_result.clean_copy()
    
    assert clean_result._result['censored'] == "the output has been hidden due to the fact that 'no_log: true' was specified for this result"
    assert clean_result._result['preserve_this'] == 'preserved_value'

def test_clean_copy_normal_action(task_result, monkeypatch):
    monkeypatch.setattr('ansible.executor.task_result._IGNORE', _IGNORE)
    monkeypatch.setattr('ansible.executor.task_result._SUB_PRESERVE', _SUB_PRESERVE)
    monkeypatch.setattr('ansible.executor.task_result._PRESERVE', _PRESERVE)
    monkeypatch.setattr('ansible.executor.task_result.CLEAN_EXCEPTIONS', CLEAN_EXCEPTIONS)
    monkeypatch.setattr('ansible.executor.task_result.module_response_deepcopy', module_response_deepcopy)
    monkeypatch.setattr('ansible.executor.task_result.strip_internal_keys', strip_internal_keys)
    
    task_result._task.action = 'normal'
    clean_result = task_result.clean_copy()
    
    assert 'ignore_this' not in clean_result._result
    assert clean_result._result['sub_key']['key1'] == 'sub_value1'
    assert clean_result._result['sub_key']['key2'] == 'sub_value2'
