# file: lib/ansible/playbook/task.py:294-333
# asked: {"lines": [322], "branches": [[300, 333], [319, 322]]}
# gained: {"lines": [322], "branches": [[300, 333], [319, 322]]}

import pytest
from unittest.mock import Mock, patch
from ansible.errors import AnsibleUndefinedVariable
from ansible.playbook.task import Task

@pytest.fixture
def templar():
    return Mock()

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
    templar.template.side_effect = lambda x, convert_bare: {'key': 'value'} if x == 'item' else x
    value = ['item', 'non_dict_item']
    with patch('ansible.playbook.task.display.warning') as mock_warning:
        result = task._post_validate_environment('attr', value, templar)
        assert result == {'key': 'value'}
        mock_warning.assert_called_once_with("could not parse environment value, skipping: %s" % value)

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
    task.action = 'gather_facts'
    templar.template.side_effect = AnsibleUndefinedVariable("ansible_facts.env")
    value = {'key1': 'value1'}
    result = task._post_validate_environment('attr', value, templar)
    assert result == {}
