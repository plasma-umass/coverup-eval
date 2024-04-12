# file lib/ansible/plugins/callback/junit.py:314-337
# lines [314, 315, 319, 320, 321, 322, 323, 324, 325, 326, 327, 329, 330, 331, 333, 335, 337]
# branches ['330->331', '330->337', '331->333', '331->335']

import pytest
import time
from unittest.mock import Mock

# Assuming the TaskData class is in a module named `junit` under `ansible.plugins.callback`
from ansible.plugins.callback.junit import TaskData

class HostMock:
    def __init__(self, uuid, name, status, result):
        self.uuid = uuid
        self.name = name
        self.status = status
        self.result = result

@pytest.fixture
def task_data():
    return TaskData(uuid="1234", name="test_task", path="/path/to/task", play="test_play", action="test_action")

def test_task_data_add_host_duplicate_raises_exception(task_data):
    host1 = HostMock(uuid="host1", name="host_one", status="ok", result="result1")
    task_data.add_host(host1)
    
    host2 = HostMock(uuid="host1", name="host_one", status="failed", result="result2")
    with pytest.raises(Exception) as excinfo:
        task_data.add_host(host2)
    
    assert str(excinfo.value) == "/path/to/task: test_play: test_task: duplicate host callback: host_one"

def test_task_data_add_host_included_concatenates_results(task_data):
    host1 = HostMock(uuid="host1", name="host_one", status="included", result="result1")
    task_data.add_host(host1)
    
    host2 = HostMock(uuid="host1", name="host_one", status="included", result="result2")
    task_data.add_host(host2)
    
    assert task_data.host_data["host1"].result == "result1\nresult2"
