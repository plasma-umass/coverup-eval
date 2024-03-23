# file lib/ansible/parsing/mod_args.py:222-258
# lines [222, 235, 236, 238, 240, 241, 242, 243, 244, 245, 246, 248, 250, 251, 252, 256, 258]
# branches ['238->240', '238->248', '241->242', '241->258', '248->250', '248->256']

import pytest
from ansible.errors import AnsibleParserError
from ansible.parsing.mod_args import ModuleArgsParser
from ansible.module_utils.six import string_types

# Assuming FREEFORM_ACTIONS and parse_kv are defined somewhere in the module
# If not, they should be mocked or defined for testing purposes

FREEFORM_ACTIONS = ['shell', 'cmd', 'raw']

def parse_kv(module_args, check_raw=False):
    # Mock implementation of parse_kv function
    return {'parsed_args': module_args}

@pytest.fixture
def module_args_parser():
    return ModuleArgsParser()

def test_normalize_old_style_args_with_dict(module_args_parser):
    input_dict = {'module': 'shell echo hi'}
    expected_action = 'shell'
    expected_args = {'parsed_args': 'echo hi'}
    action, args = module_args_parser._normalize_old_style_args(input_dict)
    assert action == expected_action
    assert args == expected_args

def test_normalize_old_style_args_with_string(module_args_parser):
    input_string = 'shell echo hi'
    expected_action = 'shell'
    expected_args = {'parsed_args': 'echo hi'}
    action, args = module_args_parser._normalize_old_style_args(input_string)
    assert action == expected_action
    assert args == expected_args

def test_normalize_old_style_args_with_unexpected_type(module_args_parser):
    with pytest.raises(AnsibleParserError):
        module_args_parser._normalize_old_style_args(12345)  # Not a dict or string

# Mocking the FREEFORM_ACTIONS and parse_kv if they are not available
@pytest.fixture(autouse=True)
def mock_freeform_actions(mocker):
    mocker.patch('ansible.parsing.mod_args.FREEFORM_ACTIONS', new=['shell', 'cmd', 'raw'])

@pytest.fixture(autouse=True)
def mock_parse_kv(mocker):
    mocker.patch('ansible.parsing.mod_args.parse_kv', side_effect=parse_kv)
