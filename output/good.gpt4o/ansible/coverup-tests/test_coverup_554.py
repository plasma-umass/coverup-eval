# file lib/ansible/playbook/task_include.py:35-48
# lines [35, 37, 42, 43, 44, 45]
# branches []

import pytest
from ansible.playbook.task_include import TaskInclude

def test_task_include_valid_args():
    # Check if the VALID_ARGS set is correctly formed
    expected_valid_args = frozenset(('file', '_raw_params', 'apply'))
    assert TaskInclude.VALID_ARGS == expected_valid_args

def test_task_include_valid_include_keywords():
    # Check if the VALID_INCLUDE_KEYWORDS set is correctly formed
    expected_valid_include_keywords = frozenset(('action', 'args', 'collections', 'debugger', 'ignore_errors', 'loop', 'loop_control',
                                                 'loop_with', 'name', 'no_log', 'register', 'run_once', 'tags', 'timeout', 'vars',
                                                 'when'))
    assert TaskInclude.VALID_INCLUDE_KEYWORDS == expected_valid_include_keywords

@pytest.fixture
def mock_task_include(mocker):
    # Mocking TaskInclude to ensure no side effects
    mocker.patch('ansible.playbook.task_include.TaskInclude', autospec=True)

def test_task_include_base(mock_task_include):
    # Check if the BASE set is correctly formed
    expected_base = frozenset(('file', '_raw_params'))
    assert TaskInclude.BASE == expected_base

def test_task_include_other_args(mock_task_include):
    # Check if the OTHER_ARGS set is correctly formed
    expected_other_args = frozenset(('apply',))
    assert TaskInclude.OTHER_ARGS == expected_other_args
