# file: lib/ansible/playbook/task.py:148-157
# asked: {"lines": [148, 151, 152, 153, 154, 155, 156, 157], "branches": [[152, 153], [152, 154], [154, 155], [154, 156]]}
# gained: {"lines": [148, 151, 152, 153, 154, 155, 156, 157], "branches": [[152, 153], [152, 154], [154, 155], [154, 156]]}

import pytest
from ansible.errors import AnsibleError
from ansible.playbook.task import Task

class MockBase:
    pass

class MockConditional:
    pass

class MockTaggable:
    pass

class MockCollectionSearch:
    pass

class MockTask(MockBase, MockConditional, MockTaggable, MockCollectionSearch, Task):
    pass

@pytest.fixture
def task():
    return MockTask()

def test_preprocess_with_loop_no_duplicate(task):
    ds = {}
    new_ds = {}
    k = "with_items"
    v = [1, 2, 3]
    
    task._preprocess_with_loop(ds, new_ds, k, v)
    
    assert new_ds['loop_with'] == "items"
    assert new_ds['loop'] == v

def test_preprocess_with_loop_duplicate_loop(task):
    ds = {}
    new_ds = {'loop': [1, 2, 3]}
    k = "with_items"
    v = [4, 5, 6]
    
    with pytest.raises(AnsibleError, match="duplicate loop in task: items"):
        task._preprocess_with_loop(ds, new_ds, k, v)

def test_preprocess_with_loop_duplicate_loop_with(task):
    ds = {}
    new_ds = {'loop_with': "items"}
    k = "with_items"
    v = [4, 5, 6]
    
    with pytest.raises(AnsibleError, match="duplicate loop in task: items"):
        task._preprocess_with_loop(ds, new_ds, k, v)

def test_preprocess_with_loop_value_none(task):
    ds = {}
    new_ds = {}
    k = "with_items"
    v = None
    
    with pytest.raises(AnsibleError, match="you must specify a value when using with_items"):
        task._preprocess_with_loop(ds, new_ds, k, v)
