# file: lib/ansible/playbook/task.py:273-285
# asked: {"lines": [279, 280, 282, 283, 285], "branches": [[279, 280], [279, 282], [282, 283], [282, 285]]}
# gained: {"lines": [279, 280, 282, 283, 285], "branches": [[279, 280], [282, 283], [282, 285]]}

import pytest
from unittest.mock import Mock, patch

# Assuming the Task class and its dependencies are imported from ansible.playbook.task
from ansible.playbook.task import Task
from ansible.playbook.task import AnsibleCollectionConfig

class TestTask:
    @pytest.fixture
    def task(self):
        # Create a Task instance with a mock parent
        parent = Mock()
        task = Task()
        task._parent = parent
        return task

    def test_post_validate_with_parent(self, task):
        templar = Mock()
        task._valid_attrs = {}
        task.post_validate(templar)
        task._parent.post_validate.assert_called_once_with(templar)

    @patch('ansible.playbook.task.AnsibleCollectionConfig')
    def test_post_validate_with_default_collection(self, mock_config, task):
        templar = Mock()
        task._valid_attrs = {}
        mock_config.default_collection = True
        task.post_validate(templar)
        task._parent.post_validate.assert_called_once_with(templar)
        # Ensure the super method is called
        with patch.object(Task, 'post_validate', autospec=True) as mock_super:
            task.post_validate(templar)
            mock_super.assert_called_with(task, templar)

    def test_post_validate_without_parent(self):
        task = Task()
        task._parent = None
        task._valid_attrs = {}
        templar = Mock()
        with patch.object(Task, 'post_validate', autospec=True) as mock_super:
            task.post_validate(templar)
            mock_super.assert_called_with(task, templar)
