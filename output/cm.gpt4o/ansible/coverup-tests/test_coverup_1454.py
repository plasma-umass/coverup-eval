# file lib/ansible/playbook/task.py:356-368
# lines []
# branches ['363->365', '365->368']

import pytest
from unittest.mock import Mock

from ansible.playbook.task import Task

@pytest.fixture
def mock_parent():
    parent = Mock()
    parent.get_vars.return_value = {'tags': 'some_tag', 'when': 'some_condition', 'other_var': 'value'}
    return parent

def test_get_vars_with_tags_and_when(mock_parent):
    task = Task()
    task._parent = mock_parent
    task.vars = {'additional_var': 'additional_value'}
    
    result = task.get_vars()
    
    assert 'tags' not in result
    assert 'when' not in result
    assert 'other_var' in result
    assert 'additional_var' in result

def test_get_vars_without_tags_and_when(mock_parent):
    task = Task()
    task._parent = mock_parent
    task.vars = {'additional_var': 'additional_value'}
    
    # Modify the mock to not include 'tags' and 'when'
    mock_parent.get_vars.return_value = {'other_var': 'value'}
    
    result = task.get_vars()
    
    assert 'tags' not in result
    assert 'when' not in result
    assert 'other_var' in result
    assert 'additional_var' in result
