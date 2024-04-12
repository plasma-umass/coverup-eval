# file lib/ansible/plugins/callback/tree.py:39-86
# lines [39, 40, 44, 45, 46, 47, 49, 52, 54, 56, 58, 60, 63, 64, 65, 66, 67, 69, 70, 71, 72, 73, 74, 76, 77, 79, 80, 82, 83, 85, 86]
# branches ['54->56', '54->58']

import os
import pytest
from ansible.plugins.callback.tree import CallbackModule
from ansible.executor.task_result import TaskResult
from ansible.inventory.host import Host
from ansible.vars.manager import VariableManager
from unittest.mock import MagicMock, patch

# Define a fixture for the callback module
@pytest.fixture
def tree_callback(tmp_path, mocker):
    mocker.patch('ansible.plugins.callback.tree.TREE_DIR', str(tmp_path))
    callback = CallbackModule()
    # Mock the required attributes and methods for set_options
    callback._load_name = 'tree'
    callback._plugin_options = {}
    mocker.patch('ansible.plugins.callback.tree.CallbackBase.set_options')
    callback.set_options()
    return callback

# Define a fixture for the task result
@pytest.fixture
def task_result():
    fake_host = Host(name='fake-host')
    result = TaskResult(
        task=MagicMock(),
        host=fake_host,
        return_data={
            'changed': False,
            'failed': False,
            'msg': 'All good!'
        }
    )
    return result

# Test function to improve coverage
def test_write_tree_file(tree_callback, task_result, tmp_path):
    # Mock the _dump_results method to return a simple JSON string
    tree_callback._dump_results = MagicMock(return_value='{"msg": "All good!"}')
    
    # Call the method that should trigger write_tree_file
    tree_callback.v2_runner_on_ok(task_result)
    
    # Check if the file was created and contains the expected content
    host_file = tmp_path / 'fake-host'
    assert host_file.exists()
    with host_file.open('r') as f:
        content = f.read()
        assert content == '{"msg": "All good!"}'

    # Cleanup after the test
    os.remove(str(host_file))
