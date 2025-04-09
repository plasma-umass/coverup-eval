# file lib/ansible/playbook/task.py:294-333
# lines []
# branches ['300->333']

import pytest
from unittest.mock import MagicMock
from ansible.playbook.task import Task
from ansible.template import Templar
from ansible.errors import AnsibleUndefinedVariable

@pytest.fixture
def templar():
    return MagicMock(spec=Templar)

@pytest.fixture
def task():
    return Task()

def test_post_validate_environment_with_none(task, templar):
    value = None

    result = task._post_validate_environment('attr', value, templar)

    assert result == {}

def test_post_validate_environment_with_list_of_dicts(task, templar):
    value = [{'key1': 'value1'}, {'key2': 'value2'}]
    templar.template.side_effect = lambda v, convert_bare: v

    result = task._post_validate_environment('attr', value, templar)

    assert result == {'key1': 'value1', 'key2': 'value2'}

def test_post_validate_environment_with_list_of_non_dicts(task, templar):
    value = ['key1=value1', 'key2=value2']
    templar.template.side_effect = lambda v, convert_bare: {'key1': 'value1'} if v == 'key1=value1' else {'key2': 'value2'}

    result = task._post_validate_environment('attr', value, templar)

    assert result == {'key1': 'value1', 'key2': 'value2'}

def test_post_validate_environment_with_dict(task, templar):
    value = {'key1': 'value1', 'key2': 'value2'}
    templar.template.side_effect = lambda v, convert_bare: v

    result = task._post_validate_environment('attr', value, templar)

    assert result == {'key1': 'value1', 'key2': 'value2'}

def test_post_validate_environment_with_string(task, templar):
    value = 'key1=value1'
    templar.template.side_effect = lambda v, convert_bare: {'key1': 'value1'}

    result = task._post_validate_environment('attr', value, templar)

    assert result == {'key1': 'value1'}

def test_post_validate_environment_with_undefined_variable(task, templar):
    value = {'key1': 'value1'}
    templar.template.side_effect = AnsibleUndefinedVariable("undefined variable error")

    with pytest.raises(AnsibleUndefinedVariable):
        task._post_validate_environment('attr', value, templar)
