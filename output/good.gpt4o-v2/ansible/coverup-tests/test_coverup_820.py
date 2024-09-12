# file: lib/ansible/playbook/task.py:349-354
# asked: {"lines": [349, 354], "branches": []}
# gained: {"lines": [349, 354], "branches": []}

import pytest
from ansible.playbook.task import Task
from ansible.template import Templar

@pytest.fixture
def task_instance():
    return Task()

def test_post_validate_until(task_instance, mocker):
    attr = "until"
    value = "some_value"
    templar = mocker.Mock(spec=Templar)

    result = task_instance._post_validate_until(attr, value, templar)

    assert result == value
