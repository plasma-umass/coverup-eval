# file lib/ansible/parsing/mod_args.py:195-220
# lines [195, 208, 210, 211, 213, 214, 215, 217, 219, 220]
# branches ['208->210', '208->211', '211->213', '211->215', '215->217', '215->219']

import pytest
from ansible.parsing.mod_args import ModuleArgsParser
from ansible.errors import AnsibleParserError
from ansible.module_utils.six import string_types

# Mocking the necessary functions and constants
FREEFORM_ACTIONS = ['shell', 'command']
def parse_kv(thing, check_raw=False):
    if check_raw:
        return {'_raw_params': thing, '_uses_shell': True}
    return dict(item.split('=') for item in thing.split())

@pytest.fixture
def module_args_parser(mocker):
    parser = ModuleArgsParser()
    mocker.patch('ansible.parsing.mod_args.FREEFORM_ACTIONS', FREEFORM_ACTIONS)
    mocker.patch('ansible.parsing.mod_args.parse_kv', parse_kv)
    return parser

def test_normalize_new_style_args_dict(module_args_parser):
    thing = {'region': 'xyz'}
    action = 'ec2'
    result = module_args_parser._normalize_new_style_args(thing, action)
    assert result == {'region': 'xyz'}

def test_normalize_new_style_args_string(module_args_parser):
    thing = 'src=a dest=b'
    action = 'copy'
    result = module_args_parser._normalize_new_style_args(thing, action)
    assert result == {'src': 'a', 'dest': 'b'}

def test_normalize_new_style_args_string_freeform(module_args_parser):
    thing = 'echo hi'
    action = 'shell'
    result = module_args_parser._normalize_new_style_args(thing, action)
    assert result == {'_raw_params': 'echo hi', '_uses_shell': True}

def test_normalize_new_style_args_none(module_args_parser):
    thing = None
    action = 'ping'
    result = module_args_parser._normalize_new_style_args(thing, action)
    assert result is None

def test_normalize_new_style_args_unexpected_type(module_args_parser):
    thing = 12345
    action = 'copy'
    with pytest.raises(AnsibleParserError, match="unexpected parameter type in action: <class 'int'>"):
        module_args_parser._normalize_new_style_args(thing, action)
