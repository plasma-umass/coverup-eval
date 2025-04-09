# file: lib/ansible/playbook/task.py:294-333
# asked: {"lines": [294, 299, 300, 302, 303, 304, 305, 306, 307, 309, 310, 312, 313, 314, 315, 316, 318, 319, 320, 322, 324, 326, 327, 328, 331, 333], "branches": [[300, 302], [300, 333], [307, 309], [307, 310], [312, 313], [312, 324], [313, 314], [313, 333], [314, 315], [314, 318], [315, 313], [315, 316], [319, 320], [319, 322], [324, 326], [324, 331], [327, 328], [327, 333]]}
# gained: {"lines": [294, 299, 300, 302, 303, 304, 305, 306, 307, 309, 310, 312, 313, 314, 315, 316, 318, 319, 320, 324, 326, 327, 328, 331, 333], "branches": [[300, 302], [307, 309], [307, 310], [312, 313], [312, 324], [313, 314], [313, 333], [314, 315], [314, 318], [315, 313], [315, 316], [319, 320], [324, 326], [324, 331], [327, 328], [327, 333]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.playbook.task import Task
from ansible.errors import AnsibleUndefinedVariable
from ansible.module_utils._text import to_native

@pytest.fixture
def templar():
    return MagicMock()

@pytest.fixture
def task():
    return Task()

def test_post_validate_environment_with_list_of_dicts(task, templar):
    value = [{'key1': 'value1'}, {'key2': 'value2'}]
    templar.template.side_effect = lambda x, convert_bare: x
    result = task._post_validate_environment('attr', value, templar)
    assert result == {'key1': 'value1', 'key2': 'value2'}

def test_post_validate_environment_with_list_of_non_dicts(task, templar):
    value = ['key1=value1', 'key2=value2']
    templar.template.side_effect = lambda x, convert_bare: {'key1': 'value1'} if x == 'key1=value1' else {'key2': 'value2'}
    result = task._post_validate_environment('attr', value, templar)
    assert result == {'key1': 'value1', 'key2': 'value2'}

def test_post_validate_environment_with_dict(task, templar):
    value = {'key1': 'value1', 'key2': 'value2'}
    templar.template.side_effect = lambda x, convert_bare: x
    result = task._post_validate_environment('attr', value, templar)
    assert result == {'key1': 'value1', 'key2': 'value2'}

def test_post_validate_environment_with_string(task, templar):
    value = 'key1=value1'
    templar.template.side_effect = lambda x, convert_bare: {'key1': 'value1'}
    result = task._post_validate_environment('attr', value, templar)
    assert result == {'key1': 'value1'}

def test_post_validate_environment_with_undefined_variable(task, templar):
    value = {'key1': 'value1'}
    templar.template.side_effect = AnsibleUndefinedVariable('undefined variable')
    with pytest.raises(AnsibleUndefinedVariable):
        task._post_validate_environment('attr', value, templar)

def test_post_validate_environment_with_fact_gathering(task, templar):
    value = {'key1': 'value1'}
    task.action = 'gather_facts'
    templar.template.side_effect = AnsibleUndefinedVariable('ansible_facts.env')
    result = task._post_validate_environment('attr', value, templar)
    assert result == {}
