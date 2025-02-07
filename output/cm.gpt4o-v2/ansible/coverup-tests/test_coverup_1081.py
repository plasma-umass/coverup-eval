# file: lib/ansible/executor/task_result.py:108-154
# asked: {"lines": [113, 116, 118, 120, 122, 124, 125, 126, 127, 128, 129, 131, 132, 135, 136, 137, 139, 140, 141, 144, 145, 146, 149, 152, 154], "branches": [[116, 118], [116, 120], [124, 125], [124, 131], [125, 124], [125, 126], [127, 124], [127, 128], [128, 127], [128, 129], [131, 132], [131, 140], [135, 136], [135, 139], [136, 135], [136, 137], [140, 141], [140, 152], [144, 145], [144, 149], [145, 144], [145, 146]]}
# gained: {"lines": [113, 116, 118, 122, 124, 125, 126, 127, 128, 129, 131, 132, 135, 136, 137, 139, 140, 141, 144, 145, 146, 149, 152, 154], "branches": [[116, 118], [124, 125], [124, 131], [125, 126], [127, 124], [127, 128], [128, 129], [131, 132], [131, 140], [135, 136], [135, 139], [136, 137], [140, 141], [144, 145], [144, 149], [145, 144], [145, 146]]}

import pytest
from ansible.executor.task_result import TaskResult
from ansible import constants as C
from unittest.mock import Mock

@pytest.fixture
def task_result():
    task = Mock()
    task.action = 'debug'
    task.no_log = False
    host = Mock()
    result = {
        '_ansible_no_log': False,
        '_ansible_delegated_vars': {
            'ansible_host': 'localhost',
            'ansible_port': 22,
            'ansible_user': 'user',
            'ansible_connection': 'ssh'
        },
        'failed': True,
        'skipped': True,
        'attempts': 1,
        'changed': True,
        'retries': 3
    }
    task_fields = {}
    return TaskResult(host, task, result, task_fields)

def test_clean_copy_no_log_true(task_result):
    task_result._task.no_log = True
    clean_result = task_result.clean_copy()
    assert clean_result._result['censored'] == "the output has been hidden due to the fact that 'no_log: true' was specified for this result"
    assert clean_result._result['attempts'] == 1
    assert clean_result._result['changed'] == True
    assert clean_result._result['retries'] == 3

def test_clean_copy_no_log_false(task_result):
    task_result._task.no_log = False
    clean_result = task_result.clean_copy()
    assert 'censored' not in clean_result._result
    assert 'failed' not in clean_result._result
    assert 'skipped' not in clean_result._result
    assert clean_result._result['attempts'] == 1
    assert clean_result._result['changed'] == True
    assert clean_result._result['retries'] == 3

def test_clean_copy_ansible_no_log(task_result):
    task_result._result['_ansible_no_log'] = True
    clean_result = task_result.clean_copy()
    assert clean_result._result['censored'] == "the output has been hidden due to the fact that 'no_log: true' was specified for this result"
    assert clean_result._result['attempts'] == 1
    assert clean_result._result['changed'] == True
    assert clean_result._result['retries'] == 3

def test_clean_copy_preserve_subset(task_result):
    clean_result = task_result.clean_copy()
    assert clean_result._result['_ansible_delegated_vars']['ansible_host'] == 'localhost'
    assert clean_result._result['_ansible_delegated_vars']['ansible_port'] == 22
    assert clean_result._result['_ansible_delegated_vars']['ansible_user'] == 'user'
    assert clean_result._result['_ansible_delegated_vars']['ansible_connection'] == 'ssh'
