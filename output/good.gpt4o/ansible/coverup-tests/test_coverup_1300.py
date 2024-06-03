# file lib/ansible/playbook/task.py:349-354
# lines [354]
# branches []

import pytest
from ansible.playbook.task import Task
from ansible.template import Templar

@pytest.fixture
def mock_templar(mocker):
    return mocker.Mock(spec=Templar)

def test_post_validate_until(mock_templar):
    task = Task()
    attr = 'until'
    value = 'some_value'
    
    result = task._post_validate_until(attr, value, mock_templar)
    
    assert result == value
