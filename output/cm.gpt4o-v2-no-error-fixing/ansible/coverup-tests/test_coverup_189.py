# file: lib/ansible/parsing/mod_args.py:107-124
# asked: {"lines": [107, 108, 110, 111, 112, 113, 115, 116, 118, 119, 121, 122, 124], "branches": [[110, 111], [110, 112]]}
# gained: {"lines": [107, 108, 110, 111, 112, 113, 115, 116, 118, 119, 121, 122, 124], "branches": [[110, 111], [110, 112]]}

import pytest
from ansible.errors import AnsibleAssertionError
from ansible.parsing.mod_args import ModuleArgsParser

def test_module_args_parser_init_with_none():
    parser = ModuleArgsParser()
    assert parser._task_ds == {}
    assert parser._collection_list is None
    assert parser.resolved_action is None

def test_module_args_parser_init_with_dict():
    task_ds = {'key': 'value'}
    parser = ModuleArgsParser(task_ds=task_ds)
    assert parser._task_ds == task_ds
    assert parser._collection_list is None
    assert parser.resolved_action is None

def test_module_args_parser_init_with_invalid_type():
    with pytest.raises(AnsibleAssertionError, match="the type of 'task_ds' should be a dict, but is a <class 'list'>"):
        ModuleArgsParser(task_ds=[])

def test_module_args_parser_task_attrs(monkeypatch):
    class MockTask:
        _valid_attrs = {'attr1': None}

    class MockHandler:
        _valid_attrs = {'attr2': None}

    monkeypatch.setattr('ansible.playbook.task.Task', MockTask)
    monkeypatch.setattr('ansible.playbook.handler.Handler', MockHandler)

    parser = ModuleArgsParser()
    expected_attrs = frozenset(['attr1', 'attr2', 'local_action', 'static'])
    assert parser._task_attrs == expected_attrs
