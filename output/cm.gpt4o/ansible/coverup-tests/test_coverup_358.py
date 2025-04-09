# file lib/ansible/playbook/task.py:148-157
# lines [148, 151, 152, 153, 154, 155, 156, 157]
# branches ['152->153', '152->154', '154->155', '154->156']

import pytest
from ansible.errors import AnsibleError
from ansible.playbook.task import Task

@pytest.fixture
def task_instance():
    return Task()

def test_preprocess_with_loop_duplicate_loop(task_instance):
    ds = {}
    new_ds = {'loop': 'existing_loop'}
    k = 'with_items'
    v = 'some_value'
    
    with pytest.raises(AnsibleError, match="duplicate loop in task: items"):
        task_instance._preprocess_with_loop(ds, new_ds, k, v)

def test_preprocess_with_loop_no_value(task_instance):
    ds = {}
    new_ds = {}
    k = 'with_items'
    v = None
    
    with pytest.raises(AnsibleError, match="you must specify a value when using with_items"):
        task_instance._preprocess_with_loop(ds, new_ds, k, v)

def test_preprocess_with_loop_success(task_instance):
    ds = {}
    new_ds = {}
    k = 'with_items'
    v = 'some_value'
    
    task_instance._preprocess_with_loop(ds, new_ds, k, v)
    
    assert new_ds['loop_with'] == 'items'
    assert new_ds['loop'] == v
