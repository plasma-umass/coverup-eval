# file: lib/ansible/plugins/callback/junit.py:314-337
# asked: {"lines": [330, 331, 333, 335, 337], "branches": [[330, 331], [330, 337], [331, 333], [331, 335]]}
# gained: {"lines": [330, 331, 333, 335, 337], "branches": [[330, 331], [330, 337], [331, 333], [331, 335]]}

import pytest
from unittest.mock import Mock

class Host:
    def __init__(self, uuid, status, result, name):
        self.uuid = uuid
        self.status = status
        self.result = result
        self.name = name

@pytest.fixture
def task_data():
    from ansible.plugins.callback.junit import TaskData
    return TaskData(uuid="1234", name="test_task", path="/path/to/task", play="test_play", action="test_action")

def test_add_host_included_status(task_data):
    host1 = Host(uuid="host1", status="included", result="result1", name="host1_name")
    host2 = Host(uuid="host1", status="included", result="result2", name="host1_name")
    
    task_data.add_host(host1)
    task_data.add_host(host2)
    
    assert task_data.host_data["host1"].result == "result1\nresult2"

def test_add_host_duplicate_callback(task_data):
    host1 = Host(uuid="host1", status="included", result="result1", name="host1_name")
    host2 = Host(uuid="host1", status="failed", result="result2", name="host1_name")
    
    task_data.add_host(host1)
    
    with pytest.raises(Exception) as excinfo:
        task_data.add_host(host2)
    
    assert "duplicate host callback" in str(excinfo.value)

def test_add_host_new_entry(task_data):
    host = Host(uuid="host1", status="included", result="result1", name="host1_name")
    
    task_data.add_host(host)
    
    assert task_data.host_data["host1"] == host
