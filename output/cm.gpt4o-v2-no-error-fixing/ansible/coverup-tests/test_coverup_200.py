# file: lib/ansible/parsing/mod_args.py:195-220
# asked: {"lines": [195, 208, 210, 211, 213, 214, 215, 217, 219, 220], "branches": [[208, 210], [208, 211], [211, 213], [211, 215], [215, 217], [215, 219]]}
# gained: {"lines": [195, 208, 210, 211, 213, 214, 215, 217, 219, 220], "branches": [[208, 210], [208, 211], [211, 213], [211, 215], [215, 217], [215, 219]]}

import pytest
from ansible.errors import AnsibleParserError
from ansible.module_utils.six import string_types
from ansible.parsing.splitter import parse_kv
from ansible.parsing.mod_args import ModuleArgsParser

FREEFORM_ACTIONS = frozenset(['shell', 'command', 'raw', 'script'])

@pytest.fixture
def parser():
    return ModuleArgsParser()

def test_normalize_new_style_args_dict(parser):
    thing = {'region': 'xyz'}
    action = 'ec2'
    result = parser._normalize_new_style_args(thing, action)
    assert result == {'region': 'xyz'}

def test_normalize_new_style_args_string(parser, mocker):
    thing = 'src=a dest=b'
    action = 'copy'
    mocker.patch('ansible.parsing.mod_args.FREEFORM_ACTIONS', new=FREEFORM_ACTIONS)
    result = parser._normalize_new_style_args(thing, action)
    expected_result = parse_kv(thing, check_raw=False)
    assert result == expected_result

def test_normalize_new_style_args_string_freeform(parser, mocker):
    thing = 'echo hi'
    action = 'shell'
    mocker.patch('ansible.parsing.mod_args.FREEFORM_ACTIONS', new=FREEFORM_ACTIONS)
    result = parser._normalize_new_style_args(thing, action)
    expected_result = parse_kv(thing, check_raw=True)
    assert result == expected_result

def test_normalize_new_style_args_none(parser):
    thing = None
    action = 'ping'
    result = parser._normalize_new_style_args(thing, action)
    assert result is None

def test_normalize_new_style_args_unexpected_type(parser):
    thing = 12345
    action = 'ping'
    with pytest.raises(AnsibleParserError, match="unexpected parameter type in action: <class 'int'>"):
        parser._normalize_new_style_args(thing, action)
