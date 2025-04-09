# file: lib/ansible/playbook/task.py:294-333
# asked: {"lines": [], "branches": [[300, 333]]}
# gained: {"lines": [], "branches": [[300, 333]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.playbook.task import Task
from ansible.template import Templar
from ansible.errors import AnsibleUndefinedVariable
from ansible.utils.display import Display

@pytest.fixture
def templar():
    return MagicMock(spec=Templar)

@pytest.fixture
def task():
    return Task()

def test_post_validate_environment_with_none_value(task, templar):
    result = task._post_validate_environment('attr', None, templar)
    assert result == {}

def test_post_validate_environment_with_list_of_dicts(task, templar):
    templar.template.side_effect = lambda x, convert_bare: x
    value = [{'key1': 'value1'}, {'key2': 'value2'}]
    result = task._post_validate_environment('attr', value, templar)
    assert result == {'key1': 'value1', 'key2': 'value2'}

def test_post_validate_environment_with_list_of_non_dicts(task, templar):
    templar.template.side_effect = lambda x, convert_bare: {'key': 'value'} if x == 'env_item' else x
    value = ['env_item']
    result = task._post_validate_environment('attr', value, templar)
    assert result == {'key': 'value'}

def test_post_validate_environment_with_dict(task, templar):
    templar.template.side_effect = lambda x, convert_bare: x
    value = {'key1': 'value1', 'key2': 'value2'}
    result = task._post_validate_environment('attr', value, templar)
    assert result == {'key1': 'value1', 'key2': 'value2'}

def test_post_validate_environment_with_string(task, templar):
    templar.template.side_effect = lambda x, convert_bare: 'templated_value'
    value = 'some_string'
    result = task._post_validate_environment('attr', value, templar)
    assert result == 'templated_value'

def test_post_validate_environment_with_undefined_variable(task, templar):
    templar.template.side_effect = AnsibleUndefinedVariable("undefined variable")
    value = {'key1': 'value1'}
    with pytest.raises(AnsibleUndefinedVariable):
        task._post_validate_environment('attr', value, templar)

def test_post_validate_environment_with_fact_gathering(task, templar):
    templar.template.side_effect = AnsibleUndefinedVariable("ansible_facts.env")
    task.action = 'gather_facts'
    value = {'key1': 'value1'}
    result = task._post_validate_environment('attr', value, templar)
    assert result == {}

def test_post_validate_environment_with_warning(task, templar, mocker):
    mock_display = mocker.patch('ansible.playbook.task.display', autospec=True)
    templar.template.side_effect = lambda x, convert_bare: x
    value = ['non_dict_item']
    result = task._post_validate_environment('attr', value, templar)
    mock_display.warning.assert_called_once_with("could not parse environment value, skipping: %s" % value)
    assert result == {}
