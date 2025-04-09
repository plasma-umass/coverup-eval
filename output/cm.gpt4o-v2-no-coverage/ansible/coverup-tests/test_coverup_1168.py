# file: lib/ansible/parsing/mod_args.py:222-258
# asked: {"lines": [248, 250, 251, 252, 256], "branches": [[238, 248], [241, 258], [248, 250], [248, 256]]}
# gained: {"lines": [248, 250, 251, 252, 256], "branches": [[238, 248], [241, 258], [248, 250], [248, 256]]}

import pytest
from ansible.errors import AnsibleParserError
from ansible.module_utils.six import string_types
from ansible.parsing.splitter import parse_kv
from ansible.parsing.mod_args import ModuleArgsParser

FREEFORM_ACTIONS = ['shell', 'command']

class MockTaskDS:
    pass

@pytest.fixture
def parser():
    parser = ModuleArgsParser()
    parser._task_ds = MockTaskDS()
    parser._split_module_string = lambda x: (x.split()[0], ' '.join(x.split()[1:]))
    return parser

def test_normalize_old_style_args_dict_with_module(parser):
    thing = {'module': 'copy src=a dest=b'}
    action, args = parser._normalize_old_style_args(thing)
    assert action == 'copy'
    assert args == {'src': 'a', 'dest': 'b'}

def test_normalize_old_style_args_dict_without_module(parser):
    thing = {'shell': 'echo hi'}
    action, args = parser._normalize_old_style_args(thing)
    assert action is None
    assert args is None

def test_normalize_old_style_args_string(parser):
    thing = 'shell echo hi'
    action, args = parser._normalize_old_style_args(thing)
    assert action == 'shell'
    assert args == {'_raw_params': 'echo hi'}

def test_normalize_old_style_args_unexpected_type(parser):
    thing = 12345
    with pytest.raises(AnsibleParserError, match="unexpected parameter type in action: <class 'int'>"):
        parser._normalize_old_style_args(thing)
