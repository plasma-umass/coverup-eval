# file: lib/ansible/playbook/task.py:491-497
# asked: {"lines": [491, 492, 493, 494, 495, 496, 497], "branches": [[493, 494], [493, 497], [494, 495], [494, 496]]}
# gained: {"lines": [491, 492, 493, 494, 495, 496, 497], "branches": [[493, 494], [493, 497], [494, 495], [494, 496]]}

import pytest
from ansible.playbook.task import Task
from ansible.playbook.task_include import TaskInclude

def test_get_first_parent_include_with_task_include():
    parent_include = TaskInclude()
    task = Task(task_include=parent_include)
    
    result = task.get_first_parent_include()
    
    assert result is parent_include

def test_get_first_parent_include_with_nested_task_include():
    grandparent_include = TaskInclude()
    parent_task = Task(task_include=grandparent_include)
    child_task = Task(task_include=parent_task)
    
    result = child_task.get_first_parent_include()
    
    assert result is grandparent_include

def test_get_first_parent_include_with_no_parent():
    task = Task()
    
    result = task.get_first_parent_include()
    
    assert result is None
