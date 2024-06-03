# file lib/ansible/parsing/mod_args.py:222-258
# lines [222, 235, 236, 238, 240, 241, 242, 243, 244, 245, 246, 248, 250, 251, 252, 256, 258]
# branches ['238->240', '238->248', '241->242', '241->258', '248->250', '248->256']

import pytest
from ansible.parsing.mod_args import ModuleArgsParser
from ansible.errors import AnsibleParserError
from ansible.module_utils.common.text.converters import to_text
from ansible.module_utils.common.collections import ImmutableDict

# Mocking necessary functions and constants
FREEFORM_ACTIONS = ['shell', 'command']

def parse_kv(args, check_raw=False):
    # Dummy implementation for testing purposes
    if check_raw:
        return {'_raw_params': args}
    return dict(arg.split('=') for arg in args.split() if '=' in arg)

@pytest.fixture
def module_args_parser():
    return ModuleArgsParser()

def test_normalize_old_style_args_dict(module_args_parser, mocker):
    mocker.patch('ansible.parsing.mod_args.FREEFORM_ACTIONS', FREEFORM_ACTIONS)
    mocker.patch('ansible.parsing.mod_args.parse_kv', parse_kv)
    
    thing = {'module': 'shell echo hi'}
    action, args = module_args_parser._normalize_old_style_args(thing)
    
    assert action == 'shell'
    assert args == {'_raw_params': 'echo hi'}

def test_normalize_old_style_args_string(module_args_parser, mocker):
    mocker.patch('ansible.parsing.mod_args.FREEFORM_ACTIONS', FREEFORM_ACTIONS)
    mocker.patch('ansible.parsing.mod_args.parse_kv', parse_kv)
    
    thing = 'shell echo hi'
    action, args = module_args_parser._normalize_old_style_args(thing)
    
    assert action == 'shell'
    assert args == {'_raw_params': 'echo hi'}

def test_normalize_old_style_args_invalid_type(module_args_parser):
    with pytest.raises(AnsibleParserError):
        module_args_parser._normalize_old_style_args(123)
