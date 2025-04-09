# file: lib/ansible/plugins/action/include_vars.py:175-189
# asked: {"lines": [175, 180, 181, 182, 183, 184, 185, 186, 187, 189], "branches": [[183, 0], [183, 184], [185, 186], [185, 189]]}
# gained: {"lines": [175, 180, 181, 182, 183, 184, 185, 186, 187, 189], "branches": [[183, 0], [183, 184], [185, 186], [185, 189]]}

import os
import pytest
from unittest.mock import patch, MagicMock

# Assuming the ActionModule class is imported from ansible/plugins/action/include_vars.py
from ansible.plugins.action.include_vars import ActionModule
from ansible.playbook.task import Task
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.playbook.play_context import PlayContext
from ansible.plugins.loader import PluginLoader
from ansible.template import Templar

@pytest.fixture
def action_module():
    task = MagicMock(spec=Task)
    connection = MagicMock()
    play_context = MagicMock(spec=PlayContext)
    loader = MagicMock(spec=PluginLoader)
    templar = MagicMock(spec=Templar)
    shared_loader_obj = MagicMock()
    module = ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)
    module.source_dir = "test_dir"
    module.depth = 2
    return module

@pytest.fixture
def setup_test_dir(tmp_path):
    test_dir = tmp_path / "test_dir"
    test_dir.mkdir()
    sub_dir = test_dir / "sub_dir"
    sub_dir.mkdir()
    file1 = test_dir / "file1.txt"
    file1.write_text("content1")
    file2 = sub_dir / "file2.txt"
    file2.write_text("content2")
    return test_dir

def test_traverse_dir_depth(action_module, setup_test_dir, monkeypatch):
    action_module.source_dir = str(setup_test_dir)
    action_module.depth = 1

    with patch("ansible.plugins.action.include_vars.walk") as mock_walk:
        mock_walk.return_value = [
            (str(setup_test_dir), ["sub_dir"], ["file1.txt"]),
            (str(setup_test_dir / "sub_dir"), [], ["file2.txt"]),
        ]

        result = list(action_module._traverse_dir_depth())

        assert len(result) == 1
        assert result[0][0] == str(setup_test_dir)
        assert result[0][1] == ["file1.txt"]

def test_traverse_dir_depth_unlimited_depth(action_module, setup_test_dir, monkeypatch):
    action_module.source_dir = str(setup_test_dir)
    action_module.depth = 0

    with patch("ansible.plugins.action.include_vars.walk") as mock_walk:
        mock_walk.return_value = [
            (str(setup_test_dir), ["sub_dir"], ["file1.txt"]),
            (str(setup_test_dir / "sub_dir"), [], ["file2.txt"]),
        ]

        result = list(action_module._traverse_dir_depth())

        assert len(result) == 2
        assert result[0][0] == str(setup_test_dir)
        assert result[0][1] == ["file1.txt"]
        assert result[1][0] == str(setup_test_dir / "sub_dir")
        assert result[1][1] == ["file2.txt"]
