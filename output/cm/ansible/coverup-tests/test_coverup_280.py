# file lib/ansible/parsing/mod_args.py:107-124
# lines [107, 108, 110, 111, 112, 113, 115, 116, 118, 119, 121, 122, 124]
# branches ['110->111', '110->112']

import pytest
from ansible.errors import AnsibleAssertionError
from ansible.parsing.mod_args import ModuleArgsParser

def test_module_args_parser_with_invalid_task_ds_type(mocker):
    with pytest.raises(AnsibleAssertionError) as excinfo:
        ModuleArgsParser(task_ds='not_a_dict')
    assert "the type of 'task_ds' should be a dict" in str(excinfo.value)

def test_module_args_parser_with_none_task_ds(mocker):
    parser = ModuleArgsParser(task_ds=None)
    assert parser._task_ds == {}

def test_module_args_parser_with_valid_task_ds(mocker):
    task_ds = {'key': 'value'}
    parser = ModuleArgsParser(task_ds=task_ds)
    assert parser._task_ds == task_ds

def test_module_args_parser_with_collection_list(mocker):
    collection_list = ['collection1', 'collection2']
    parser = ModuleArgsParser(collection_list=collection_list)
    assert parser._collection_list == collection_list
