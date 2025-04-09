# file: lib/ansible/parsing/mod_args.py:107-124
# asked: {"lines": [107, 108, 110, 111, 112, 113, 115, 116, 118, 119, 121, 122, 124], "branches": [[110, 111], [110, 112]]}
# gained: {"lines": [107, 108, 110, 111, 112, 113, 115, 116, 118, 119, 121, 122, 124], "branches": [[110, 111], [110, 112]]}

import pytest
from ansible.errors import AnsibleAssertionError
from ansible.parsing.mod_args import ModuleArgsParser
from ansible.playbook.task import Task
from ansible.playbook.handler import Handler

@pytest.fixture
def mock_task_attrs(monkeypatch):
    monkeypatch.setattr(Task, '_valid_attrs', {'attr1': 'value1'})
    monkeypatch.setattr(Handler, '_valid_attrs', {'attr2': 'value2'})

def test_module_args_parser_init_with_none(mock_task_attrs):
    parser = ModuleArgsParser()
    assert parser._task_ds == {}
    assert parser._collection_list is None
    assert parser.resolved_action is None
    assert 'local_action' in parser._task_attrs
    assert 'static' in parser._task_attrs

def test_module_args_parser_init_with_dict(mock_task_attrs):
    task_ds = {'key': 'value'}
    parser = ModuleArgsParser(task_ds=task_ds)
    assert parser._task_ds == task_ds
    assert parser._collection_list is None
    assert parser.resolved_action is None
    assert 'local_action' in parser._task_attrs
    assert 'static' in parser._task_attrs

def test_module_args_parser_init_with_invalid_type():
    with pytest.raises(AnsibleAssertionError, match="the type of 'task_ds' should be a dict, but is a <class 'list'>"):
        ModuleArgsParser(task_ds=[])

