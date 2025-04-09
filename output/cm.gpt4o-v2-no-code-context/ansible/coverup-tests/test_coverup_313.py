# file: lib/ansible/playbook/task.py:148-157
# asked: {"lines": [148, 151, 152, 153, 154, 155, 156, 157], "branches": [[152, 153], [152, 154], [154, 155], [154, 156]]}
# gained: {"lines": [148, 151, 152, 153, 154, 155, 156, 157], "branches": [[152, 153], [152, 154], [154, 155], [154, 156]]}

import pytest
from ansible.playbook.task import Task
from ansible.errors import AnsibleError

class TestTask:
    def setup_method(self):
        self.task = Task()

    def test_preprocess_with_loop_duplicate_loop(self):
        ds = {}
        new_ds = {'loop': 'some_loop'}
        k = 'with_items'
        v = 'item1, item2'
        
        with pytest.raises(AnsibleError, match="duplicate loop in task: items"):
            self.task._preprocess_with_loop(ds, new_ds, k, v)

    def test_preprocess_with_loop_duplicate_loop_with(self):
        ds = {}
        new_ds = {'loop_with': 'some_loop'}
        k = 'with_items'
        v = 'item1, item2'
        
        with pytest.raises(AnsibleError, match="duplicate loop in task: items"):
            self.task._preprocess_with_loop(ds, new_ds, k, v)

    def test_preprocess_with_loop_no_value(self):
        ds = {}
        new_ds = {}
        k = 'with_items'
        v = None
        
        with pytest.raises(AnsibleError, match="you must specify a value when using with_items"):
            self.task._preprocess_with_loop(ds, new_ds, k, v)

    def test_preprocess_with_loop_success(self):
        ds = {}
        new_ds = {}
        k = 'with_items'
        v = 'item1, item2'
        
        self.task._preprocess_with_loop(ds, new_ds, k, v)
        
        assert new_ds['loop_with'] == 'items'
        assert new_ds['loop'] == v
