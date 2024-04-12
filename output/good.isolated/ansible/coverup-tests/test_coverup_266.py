# file lib/ansible/parsing/mod_args.py:195-220
# lines [195, 208, 210, 211, 213, 214, 215, 217, 219, 220]
# branches ['208->210', '208->211', '211->213', '211->215', '215->217', '215->219']

import pytest
from ansible.errors import AnsibleParserError
from ansible.parsing.mod_args import ModuleArgsParser
from ansible.module_utils.six import string_types

# Mocking the global FREEFORM_ACTIONS and parse_kv for testing purposes
FREEFORM_ACTIONS = ['shell', 'command']
def parse_kv(_string, check_raw=False):
    return {'_raw_params': _string, '_uses_shell': check_raw}

@pytest.fixture
def module_args_parser(mocker):
    mocker.patch('ansible.parsing.mod_args.FREEFORM_ACTIONS', FREEFORM_ACTIONS)
    mocker.patch('ansible.parsing.mod_args.parse_kv', side_effect=parse_kv)
    return ModuleArgsParser()

def test_normalize_new_style_args_with_dict(module_args_parser):
    input_dict = {'region': 'xyz'}
    action = 'ec2'
    expected = input_dict
    result = module_args_parser._normalize_new_style_args(input_dict, action)
    assert result == expected

def test_normalize_new_style_args_with_string(module_args_parser):
    input_string = 'echo hi'
    action = 'shell'
    expected = {'_raw_params': input_string, '_uses_shell': True}
    result = module_args_parser._normalize_new_style_args(input_string, action)
    assert result == expected

def test_normalize_new_style_args_with_none(module_args_parser):
    action = 'ping'
    result = module_args_parser._normalize_new_style_args(None, action)
    assert result is None

def test_normalize_new_style_args_with_unexpected_type(module_args_parser):
    with pytest.raises(AnsibleParserError):
        module_args_parser._normalize_new_style_args(123, 'invalid_action')
