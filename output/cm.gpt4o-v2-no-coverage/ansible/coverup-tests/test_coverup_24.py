# file: lib/ansible/executor/task_result.py:108-154
# asked: {"lines": [108, 113, 116, 118, 120, 122, 124, 125, 126, 127, 128, 129, 131, 132, 135, 136, 137, 139, 140, 141, 144, 145, 146, 149, 152, 154], "branches": [[116, 118], [116, 120], [124, 125], [124, 131], [125, 124], [125, 126], [127, 124], [127, 128], [128, 127], [128, 129], [131, 132], [131, 140], [135, 136], [135, 139], [136, 135], [136, 137], [140, 141], [140, 152], [144, 145], [144, 149], [145, 144], [145, 146]]}
# gained: {"lines": [108, 113, 116, 118, 122, 124, 125, 126, 127, 128, 129, 131, 132, 135, 136, 139, 140, 141, 144, 145, 146, 149, 152, 154], "branches": [[116, 118], [124, 125], [124, 131], [125, 124], [125, 126], [127, 124], [127, 128], [128, 129], [131, 132], [131, 140], [135, 136], [135, 139], [136, 135], [140, 141], [140, 152], [144, 145], [144, 149], [145, 144], [145, 146]]}

import pytest
from unittest.mock import Mock, patch
from ansible.executor.task_result import TaskResult
from ansible import constants as C
from ansible.vars.clean import module_response_deepcopy, strip_internal_keys

# Mock constants and functions
_IGNORE = ('key1', 'key2')
_SUB_PRESERVE = {'sub1': ['key1', 'key2'], 'sub2': ['key3']}
_PRESERVE = ['preserve_key1', 'preserve_key2']
CLEAN_EXCEPTIONS = ['exception_key']

@pytest.fixture
def mock_task():
    task = Mock()
    task.action = 'debug'
    task.no_log = False
    return task

@pytest.fixture
def mock_host():
    return Mock()

@pytest.fixture
def mock_result():
    return {
        'key1': 'value1',
        'key2': 'value2',
        'sub1': {'key1': 'subvalue1', 'key2': 'subvalue2'},
        'sub2': {'key3': 'subvalue3'},
        '_ansible_no_log': False
    }

def test_clean_copy_no_log(mock_host, mock_task, mock_result):
    mock_task.no_log = True
    task_result = TaskResult(mock_host, mock_task, mock_result)
    
    with patch('ansible.executor.task_result._IGNORE', _IGNORE), \
         patch('ansible.executor.task_result._SUB_PRESERVE', _SUB_PRESERVE), \
         patch('ansible.executor.task_result._PRESERVE', _PRESERVE), \
         patch('ansible.executor.task_result.CLEAN_EXCEPTIONS', CLEAN_EXCEPTIONS):
        
        clean_result = task_result.clean_copy()
        
        assert clean_result._result['censored'] == "the output has been hidden due to the fact that 'no_log: true' was specified for this result"
        for key in _PRESERVE:
            if key in mock_result:
                assert clean_result._result[key] == mock_result[key]

def test_clean_copy_with_result(mock_host, mock_task, mock_result):
    task_result = TaskResult(mock_host, mock_task, mock_result)
    
    with patch('ansible.executor.task_result._IGNORE', _IGNORE), \
         patch('ansible.executor.task_result._SUB_PRESERVE', _SUB_PRESERVE), \
         patch('ansible.executor.task_result._PRESERVE', _PRESERVE), \
         patch('ansible.executor.task_result.CLEAN_EXCEPTIONS', CLEAN_EXCEPTIONS), \
         patch('ansible.vars.clean.module_response_deepcopy', side_effect=lambda x: x), \
         patch('ansible.vars.clean.strip_internal_keys', side_effect=lambda x, exceptions: x):
        
        clean_result = task_result.clean_copy()
        
        for key in _IGNORE:
            assert key not in clean_result._result
        for sub in _SUB_PRESERVE:
            for key in _SUB_PRESERVE[sub]:
                assert clean_result._result[sub][key] == mock_result[sub][key]

def test_clean_copy_no_result(mock_host, mock_task):
    task_result = TaskResult(mock_host, mock_task, {})
    
    with patch('ansible.executor.task_result._IGNORE', _IGNORE), \
         patch('ansible.executor.task_result._SUB_PRESERVE', _SUB_PRESERVE), \
         patch('ansible.executor.task_result._PRESERVE', _PRESERVE), \
         patch('ansible.executor.task_result.CLEAN_EXCEPTIONS', CLEAN_EXCEPTIONS):
        
        clean_result = task_result.clean_copy()
        
        assert clean_result._result == {}
