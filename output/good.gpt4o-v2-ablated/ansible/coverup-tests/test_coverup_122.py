# file: lib/ansible/parsing/mod_args.py:107-124
# asked: {"lines": [107, 108, 110, 111, 112, 113, 115, 116, 118, 119, 121, 122, 124], "branches": [[110, 111], [110, 112]]}
# gained: {"lines": [107, 108, 110, 111, 112, 113, 115, 116, 118, 119, 121, 122, 124], "branches": [[110, 111], [110, 112]]}

import pytest
from ansible.parsing.mod_args import ModuleArgsParser
from ansible.errors import AnsibleAssertionError
from unittest.mock import patch

@pytest.fixture
def mock_task_handler():
    with patch('ansible.playbook.task.Task') as MockTask, \
         patch('ansible.playbook.handler.Handler') as MockHandler:
        MockTask._valid_attrs = {'attr1': 'value1'}
        MockHandler._valid_attrs = {'attr2': 'value2'}
        yield MockTask, MockHandler

def test_module_args_parser_default(mock_task_handler):
    parser = ModuleArgsParser()
    assert parser._task_ds == {}
    assert parser._collection_list is None
    assert parser.resolved_action is None
    assert 'local_action' in parser._task_attrs
    assert 'static' in parser._task_attrs

def test_module_args_parser_with_task_ds(mock_task_handler):
    task_ds = {'key': 'value'}
    parser = ModuleArgsParser(task_ds=task_ds)
    assert parser._task_ds == task_ds
    assert parser._collection_list is None
    assert parser.resolved_action is None

def test_module_args_parser_invalid_task_ds(mock_task_handler):
    with pytest.raises(AnsibleAssertionError, match="the type of 'task_ds' should be a dict, but is a <class 'list'>"):
        ModuleArgsParser(task_ds=[])
