# file: lib/ansible/playbook/task.py:294-333
# asked: {"lines": [294, 299, 300, 302, 303, 304, 305, 306, 307, 309, 310, 312, 313, 314, 315, 316, 318, 319, 320, 322, 324, 326, 327, 328, 331, 333], "branches": [[300, 302], [300, 333], [307, 309], [307, 310], [312, 313], [312, 324], [313, 314], [313, 333], [314, 315], [314, 318], [315, 313], [315, 316], [319, 320], [319, 322], [324, 326], [324, 331], [327, 328], [327, 333]]}
# gained: {"lines": [294, 299, 300, 302, 303, 304, 305, 306, 307, 309, 310, 312, 313, 314, 315, 316, 318, 319, 320, 322, 324, 326, 327, 328, 331, 333], "branches": [[300, 302], [307, 309], [307, 310], [312, 313], [312, 324], [313, 314], [313, 333], [314, 315], [314, 318], [315, 313], [315, 316], [319, 320], [319, 322], [324, 326], [324, 331], [327, 328], [327, 333]]}

import pytest
from unittest.mock import Mock, patch
from ansible.playbook.task import Task
from ansible.template import Templar
from ansible.errors import AnsibleUndefinedVariable
from ansible.utils.display import Display

@pytest.fixture
def templar():
    loader = Mock()
    loader.get_basedir = Mock(return_value='/tmp')
    variables = {}
    return Templar(loader=loader, variables=variables)

@pytest.fixture
def task():
    return Task()

def test_post_validate_environment_with_list_of_dicts(task, templar):
    value = [{'key1': 'value1'}, {'key2': 'value2'}]
    templar.template = Mock(side_effect=lambda x, convert_bare: x)
    result = task._post_validate_environment('attr', value, templar)
    assert result == {'key1': 'value1', 'key2': 'value2'}

def test_post_validate_environment_with_list_of_non_dicts(task, templar):
    value = ['key1=value1', 'key2=value2']
    templar.template = Mock(side_effect=lambda x, convert_bare: {'key1': 'value1'} if x == 'key1=value1' else {'key2': 'value2'})
    result = task._post_validate_environment('attr', value, templar)
    assert result == {'key1': 'value1', 'key2': 'value2'}

def test_post_validate_environment_with_list_of_non_parsable_items(task, templar, mocker):
    value = ['non_parsable']
    templar.template = Mock(return_value='non_parsable')
    mocker.patch.object(Display, 'warning')
    result = task._post_validate_environment('attr', value, templar)
    Display.warning.assert_called_once_with("could not parse environment value, skipping: %s" % value)
    assert result == {}

def test_post_validate_environment_with_dict(task, templar):
    value = {'key1': 'value1', 'key2': 'value2'}
    templar.template = Mock(side_effect=lambda x, convert_bare: x)
    result = task._post_validate_environment('attr', value, templar)
    assert result == {'key1': 'value1', 'key2': 'value2'}

def test_post_validate_environment_with_string(task, templar):
    value = 'simple_string'
    templar.template = Mock(return_value='templated_string')
    result = task._post_validate_environment('attr', value, templar)
    assert result == 'templated_string'

def test_post_validate_environment_with_undefined_variable(task, templar):
    value = {'key1': 'value1'}
    templar.template = Mock(side_effect=AnsibleUndefinedVariable('undefined variable'))
    task.action = 'gather_facts'
    with pytest.raises(AnsibleUndefinedVariable):
        task._post_validate_environment('attr', value, templar)

def test_post_validate_environment_with_undefined_variable_ignored(task, templar):
    value = {'key1': 'value1'}
    templar.template = Mock(side_effect=AnsibleUndefinedVariable('ansible_facts.env'))
    task.action = 'gather_facts'
    result = task._post_validate_environment('attr', value, templar)
    assert result == {}
