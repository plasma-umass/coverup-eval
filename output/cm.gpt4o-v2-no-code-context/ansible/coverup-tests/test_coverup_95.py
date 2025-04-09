# file: lib/ansible/playbook/task_include.py:63-88
# asked: {"lines": [63, 70, 73, 74, 75, 77, 78, 79, 80, 82, 83, 84, 85, 86, 88], "branches": [[74, 75], [74, 77], [77, 78], [77, 82], [79, 80], [79, 82], [83, 84], [83, 85], [85, 86], [85, 88]]}
# gained: {"lines": [63, 70, 73, 74, 75, 77, 78, 79, 80, 82, 83, 84, 85, 88], "branches": [[74, 75], [74, 77], [77, 78], [77, 82], [79, 80], [83, 84], [83, 85], [85, 88]]}

import pytest
from ansible.playbook.task_include import TaskInclude
from ansible.errors import AnsibleParserError
from unittest.mock import Mock, patch

class TestTaskInclude:

    @pytest.fixture
    def task_include(self):
        task_include = TaskInclude()
        task_include.VALID_ARGS = frozenset(['_raw_params', 'apply', 'file'])
        return task_include

    @patch('ansible.constants._ACTION_ALL_PROPER_INCLUDE_IMPORT_TASKS', new=['include'])
    def test_check_options_invalid_options(self, task_include):
        task = Mock()
        task.args = {'invalid_option': 'value'}
        task.action = 'include'
        data = {}

        with pytest.raises(AnsibleParserError, match='Invalid options for include: invalid_option'):
            task_include.check_options(task, data)

    def test_check_options_no_raw_params(self, task_include):
        task = Mock()
        task.args = {}
        task.action = 'include'
        data = {}

        with pytest.raises(AnsibleParserError, match='No file specified for include'):
            task_include.check_options(task, data)

    @patch('ansible.constants._ACTION_INCLUDE_TASKS', new=[])
    def test_check_options_apply_not_dict(self, task_include):
        task = Mock()
        task.args = {'_raw_params': 'some_file', 'apply': 'not_a_dict'}
        task.action = 'include'
        data = {}

        with pytest.raises(AnsibleParserError, match='Invalid options for include: apply'):
            task_include.check_options(task, data)

    @patch('ansible.constants._ACTION_INCLUDE_TASKS', new=[])
    def test_check_options_apply_invalid_action(self, task_include):
        task = Mock()
        task.args = {'_raw_params': 'some_file', 'apply': {'some_key': 'some_value'}}
        task.action = 'invalid_action'
        data = {}

        with pytest.raises(AnsibleParserError, match='Invalid options for invalid_action: apply'):
            task_include.check_options(task, data)

    def test_check_options_valid(self, task_include):
        task = Mock()
        task.args = {'_raw_params': 'some_file'}
        task.action = 'include'
        data = {}

        result = task_include.check_options(task, data)
        assert result == task
