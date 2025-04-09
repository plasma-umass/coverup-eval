# file: lib/ansible/playbook/task.py:122-134
# asked: {"lines": [122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134], "branches": [[123, 124], [123, 125], [125, 126], [125, 127], [127, 0], [127, 128], [129, 130], [129, 133], [130, 131], [130, 132]]}
# gained: {"lines": [122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134], "branches": [[123, 124], [123, 125], [125, 126], [125, 127], [127, 128], [129, 130], [129, 133], [130, 131], [130, 132]]}

import pytest
from ansible.playbook.task import Task

class TestTask:
    @pytest.fixture
    def task_instance(self):
        return Task()

    def test_merge_kv_none(self, task_instance):
        result = task_instance._merge_kv(None)
        assert result == ""

    def test_merge_kv_string(self, task_instance):
        result = task_instance._merge_kv("test_string")
        assert result == "test_string"

    def test_merge_kv_dict(self, task_instance):
        test_dict = {'key1': 'value1', 'key2': 'value2'}
        result = task_instance._merge_kv(test_dict)
        assert result == "key1=value1 key2=value2"

    def test_merge_kv_dict_with_underscore(self, task_instance):
        test_dict = {'_key1': 'value1', 'key2': 'value2'}
        result = task_instance._merge_kv(test_dict)
        assert result == "key2=value2"
