# file lib/ansible/playbook/task_include.py:90-102
# lines [91, 93, 94, 96, 97, 98, 100, 102]
# branches ['94->96', '94->102', '96->94', '96->97', '97->98', '97->100']

import pytest
from ansible.playbook.task_include import TaskInclude
from ansible.errors import AnsibleParserError
from ansible.utils.display import Display
from ansible.utils.sentinel import Sentinel

@pytest.fixture
def mock_display(mocker):
    return mocker.patch('ansible.utils.display.Display.warning')

@pytest.fixture
def task_include():
    return TaskInclude()

def test_preprocess_data_invalid_attribute_error(task_include, mocker, mock_display):
    mocker.patch('ansible.constants._ACTION_ALL_INCLUDE_ROLE_TASKS', ['include'])
    mocker.patch('ansible.constants.INVALID_TASK_ATTRIBUTE_FAILED', True)
    
    ds = {
        'action': 'include',
        'invalid_key': 'some_value'
    }
    
    with pytest.raises(AnsibleParserError, match="'invalid_key' is not a valid attribute for a TaskInclude"):
        task_include.preprocess_data(ds)

def test_preprocess_data_invalid_attribute_warning(task_include, mocker, mock_display):
    mocker.patch('ansible.constants._ACTION_ALL_INCLUDE_ROLE_TASKS', ['include'])
    mocker.patch('ansible.constants.INVALID_TASK_ATTRIBUTE_FAILED', False)
    
    ds = {
        'action': 'include',
        'invalid_key': 'some_value'
    }
    
    result = task_include.preprocess_data(ds)
    
    mock_display.assert_called_once_with("Ignoring invalid attribute: invalid_key")
    assert 'invalid_key' not in result
    assert result['action'] == 'include'
    assert result['args'] == {}
    assert result['delegate_to'] == Sentinel
    assert result['vars'] == {}
