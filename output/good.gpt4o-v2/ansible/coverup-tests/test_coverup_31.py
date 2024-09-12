# file: lib/ansible/playbook/task.py:294-333
# asked: {"lines": [294, 299, 300, 302, 303, 304, 305, 306, 307, 309, 310, 312, 313, 314, 315, 316, 318, 319, 320, 322, 324, 326, 327, 328, 331, 333], "branches": [[300, 302], [300, 333], [307, 309], [307, 310], [312, 313], [312, 324], [313, 314], [313, 333], [314, 315], [314, 318], [315, 313], [315, 316], [319, 320], [319, 322], [324, 326], [324, 331], [327, 328], [327, 333]]}
# gained: {"lines": [294, 299, 300, 302, 303, 304, 305, 306, 307, 309, 310, 312, 313, 314, 315, 316, 318, 319, 320, 324, 326, 327, 328, 331, 333], "branches": [[300, 302], [307, 309], [307, 310], [312, 313], [312, 324], [313, 314], [313, 333], [314, 315], [314, 318], [315, 313], [315, 316], [319, 320], [324, 326], [324, 331], [327, 328], [327, 333]]}

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
    value = {'key': 'value'}
    result = task._post_validate_environment('attr', value, templar)
    assert result == {'key': 'value'}

def test_post_validate_environment_with_string(task, templar):
    templar.template.side_effect = lambda x, convert_bare: 'templated_value'
    value = 'some_string'
    result = task._post_validate_environment('attr', value, templar)
    assert result == 'templated_value'

def test_post_validate_environment_with_undefined_variable(task, templar):
    def template_side_effect(value, convert_bare):
        if value == 'undefined_var':
            raise AnsibleUndefinedVariable('ansible_facts.env')
        return value

    templar.template.side_effect = template_side_effect
    value = {'key': 'undefined_var'}
    task.action = 'gather_facts'
    result = task._post_validate_environment('attr', value, templar)
    assert result == {}

def test_post_validate_environment_with_undefined_variable_raises(task, templar):
    def template_side_effect(value, convert_bare):
        if value == 'undefined_var':
            raise AnsibleUndefinedVariable('some_error')
        return value

    templar.template.side_effect = template_side_effect
    value = {'key': 'undefined_var'}
    task.action = 'some_action'
    with pytest.raises(AnsibleUndefinedVariable):
        task._post_validate_environment('attr', value, templar)
