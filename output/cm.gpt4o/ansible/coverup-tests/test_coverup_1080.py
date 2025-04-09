# file lib/ansible/playbook/task_include.py:63-88
# lines [70, 73, 74, 75, 77, 78, 79, 80, 82, 83, 84, 85, 86, 88]
# branches ['74->75', '74->77', '77->78', '77->82', '79->80', '79->82', '83->84', '83->85', '85->86', '85->88']

import pytest
from ansible.playbook.task_include import TaskInclude
from ansible.errors import AnsibleParserError
from unittest.mock import Mock, patch

class MockTask:
    def __init__(self, action, args):
        self.action = action
        self.args = args

@pytest.fixture
def mock_task():
    return MockTask(action='include', args={'file': 'test_file.yml'})

@pytest.fixture
def mock_data():
    return {'some': 'data'}

def test_check_options_valid_args(mock_task, mock_data):
    task_include = TaskInclude()
    task_include.VALID_ARGS = frozenset(['file', '_raw_params', 'apply'])
    with patch('ansible.playbook.task_include.C', new=Mock(_ACTION_ALL_PROPER_INCLUDE_IMPORT_TASKS=['include'], _ACTION_INCLUDE_TASKS=['include'])):
        task_include.check_options(mock_task, mock_data)
    assert mock_task.args['_raw_params'] == 'test_file.yml'

def test_check_options_invalid_args(mock_task, mock_data):
    task_include = TaskInclude()
    task_include.VALID_ARGS = frozenset(['_raw_params', 'apply'])
    with patch('ansible.playbook.task_include.C', new=Mock(_ACTION_ALL_PROPER_INCLUDE_IMPORT_TASKS=['include'])):
        with pytest.raises(AnsibleParserError, match='Invalid options for include: file'):
            task_include.check_options(mock_task, mock_data)

def test_check_options_no_file_specified(mock_task, mock_data):
    task_include = TaskInclude()
    task_include.VALID_ARGS = frozenset(['_raw_params', 'apply'])
    with patch('ansible.playbook.task_include.C', new=Mock(_ACTION_ALL_PROPER_INCLUDE_IMPORT_TASKS=['include'])):
        mock_task.args = {}
        with pytest.raises(AnsibleParserError, match='No file specified for include'):
            task_include.check_options(mock_task, mock_data)

def test_check_options_invalid_apply(mock_task, mock_data):
    task_include = TaskInclude()
    task_include.VALID_ARGS = frozenset(['file', '_raw_params', 'apply'])
    with patch('ansible.playbook.task_include.C', new=Mock(_ACTION_INCLUDE_TASKS=[])):
        mock_task.args['apply'] = {'some': 'data'}
        with pytest.raises(AnsibleParserError, match='Invalid options for include: apply'):
            task_include.check_options(mock_task, mock_data)

def test_check_options_apply_not_dict(mock_task, mock_data):
    task_include = TaskInclude()
    task_include.VALID_ARGS = frozenset(['file', '_raw_params', 'apply'])
    with patch('ansible.playbook.task_include.C', new=Mock(_ACTION_INCLUDE_TASKS=['include'])):
        mock_task.args['apply'] = 'not_a_dict'
        with pytest.raises(AnsibleParserError, match='Expected a dict for apply but got <class \'str\'> instead'):
            task_include.check_options(mock_task, mock_data)
