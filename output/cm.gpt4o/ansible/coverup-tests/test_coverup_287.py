# file lib/ansible/parsing/mod_args.py:107-124
# lines [107, 108, 110, 111, 112, 113, 115, 116, 118, 119, 121, 122, 124]
# branches ['110->111', '110->112']

import pytest
from ansible.parsing.mod_args import ModuleArgsParser
from ansible.errors import AnsibleAssertionError

def test_module_args_parser_with_invalid_task_ds():
    with pytest.raises(AnsibleAssertionError, match="the type of 'task_ds' should be a dict, but is a <class 'list'>"):
        ModuleArgsParser(task_ds=[])

def test_module_args_parser_with_valid_task_ds(mocker):
    mock_task = mocker.patch('ansible.playbook.task.Task')
    mock_handler = mocker.patch('ansible.playbook.handler.Handler')
    mock_task._valid_attrs = {'attr1': None}
    mock_handler._valid_attrs = {'attr2': None}

    parser = ModuleArgsParser(task_ds={'key': 'value'}, collection_list=['collection1'])
    
    assert parser._task_ds == {'key': 'value'}
    assert parser._collection_list == ['collection1']
    assert 'attr1' in parser._task_attrs
    assert 'attr2' in parser._task_attrs
    assert 'local_action' in parser._task_attrs
    assert 'static' in parser._task_attrs
    assert parser.resolved_action is None
