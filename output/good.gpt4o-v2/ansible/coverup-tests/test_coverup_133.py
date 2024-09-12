# file: lib/ansible/parsing/mod_args.py:222-258
# asked: {"lines": [222, 235, 236, 238, 240, 241, 242, 243, 244, 245, 246, 248, 250, 251, 252, 256, 258], "branches": [[238, 240], [238, 248], [241, 242], [241, 258], [248, 250], [248, 256]]}
# gained: {"lines": [222, 235, 236, 238, 240, 241, 242, 243, 244, 245, 246, 248, 250, 251, 252, 256, 258], "branches": [[238, 240], [238, 248], [241, 242], [241, 258], [248, 250], [248, 256]]}

import pytest
from ansible.errors import AnsibleParserError
from ansible.module_utils.six import string_types
from ansible.parsing.mod_args import ModuleArgsParser
from ansible.parsing.splitter import parse_kv

FREEFORM_ACTIONS = ['shell', 'command']

class MockTaskDS:
    pass

@pytest.fixture
def parser():
    parser = ModuleArgsParser()
    parser._task_ds = MockTaskDS()
    return parser

def test_normalize_old_style_args_dict_with_module(parser):
    thing = {'module': 'shell', 'src': 'a', 'dest': 'b'}
    action, args = parser._normalize_old_style_args(thing)
    assert action == 'shell'
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
