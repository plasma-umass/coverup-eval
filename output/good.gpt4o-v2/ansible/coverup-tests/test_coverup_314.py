# file: lib/ansible/playbook/task_include.py:90-102
# asked: {"lines": [90, 91, 93, 94, 96, 97, 98, 100, 102], "branches": [[94, 96], [94, 102], [96, 94], [96, 97], [97, 98], [97, 100]]}
# gained: {"lines": [90, 91, 93, 94, 96, 97, 98, 102], "branches": [[94, 96], [94, 102], [96, 94], [96, 97], [97, 98]]}

import pytest
from ansible.playbook.task_include import TaskInclude
from ansible.errors import AnsibleParserError
from ansible.utils.sentinel import Sentinel
import ansible.constants as C
from ansible.utils.display import Display

@pytest.fixture
def task_include():
    return TaskInclude()

def test_preprocess_data_invalid_attribute_error(task_include, mocker):
    ds = {
        'action': 'include_tasks',
        'invalid_attr': 'value'
    }
    mocker.patch('ansible.constants._ACTION_ALL_INCLUDE_ROLE_TASKS', ['include_tasks'])
    mocker.patch('ansible.constants.INVALID_TASK_ATTRIBUTE_FAILED', True)
    
    with pytest.raises(AnsibleParserError, match="'invalid_attr' is not a valid attribute for a TaskInclude"):
        task_include.preprocess_data(ds)

def test_preprocess_data_invalid_attribute_warning(task_include, mocker):
    ds = {
        'action': 'include_tasks',
        'invalid_attr': 'value'
    }
    mocker.patch('ansible.constants._ACTION_ALL_INCLUDE_ROLE_TASKS', ['include_tasks'])
    mocker.patch('ansible.constants.INVALID_TASK_ATTRIBUTE_FAILED', False)
    mock_display_warning = mocker.patch.object(Display, 'warning')
    
    result = task_include.preprocess_data(ds)
    
    mock_display_warning.assert_called_once_with('Ignoring invalid attribute: invalid_attr')
    assert 'invalid_attr' not in result
