# file: lib/ansible/playbook/task.py:294-333
# asked: {"lines": [322], "branches": [[300, 333], [319, 322]]}
# gained: {"lines": [322], "branches": [[300, 333], [319, 322]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.errors import AnsibleUndefinedVariable
from ansible.playbook.task import Task

@pytest.fixture
def templar():
    return MagicMock()

@pytest.fixture
def task():
    return Task()

def test_post_validate_environment_list_with_non_dict(task, templar):
    value = ["non-dict-item"]
    templar.template.return_value = "non-dict-item"
    
    with patch('ansible.playbook.task.display') as mock_display:
        result = task._post_validate_environment('attr', value, templar)
        mock_display.warning.assert_called_once_with("could not parse environment value, skipping: %s" % value)
        assert result == {}

def test_post_validate_environment_none(task, templar):
    result = task._post_validate_environment('attr', None, templar)
    assert result == {}

def test_post_validate_environment_dict(task, templar):
    value = {"key": "value"}
    templar.template.return_value = "templated-value"
    
    result = task._post_validate_environment('attr', value, templar)
    assert result == {"key": "templated-value"}

def test_post_validate_environment_string(task, templar):
    value = "simple-string"
    templar.template.return_value = "templated-string"
    
    result = task._post_validate_environment('attr', value, templar)
    assert result == "templated-string"
