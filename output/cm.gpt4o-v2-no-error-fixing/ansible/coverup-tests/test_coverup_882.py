# file: lib/ansible/parsing/mod_args.py:140-193
# asked: {"lines": [152, 153, 154, 155, 157, 159, 160, 162, 175, 176, 177, 178, 186], "branches": [[151, 152], [152, 153], [152, 159], [154, 155], [154, 157], [159, 160], [159, 162], [174, 175], [176, 177], [176, 178], [185, 186]]}
# gained: {"lines": [152, 153, 154, 155, 157, 159, 162, 175, 176, 177, 178, 186], "branches": [[151, 152], [152, 153], [152, 159], [154, 155], [154, 157], [159, 162], [174, 175], [176, 177], [185, 186]]}

import pytest
from ansible.errors import AnsibleParserError, AnsibleError
from ansible.module_utils.six import string_types
from ansible.parsing.mod_args import ModuleArgsParser
from ansible.template import Templar

@pytest.fixture
def parser():
    return ModuleArgsParser()

def test_normalize_parameters_with_string_additional_args(parser, mocker):
    mocker.patch.object(Templar, 'is_template', return_value=True)
    action, final_args = parser._normalize_parameters(thing={}, additional_args="{{ var_name }}")
    assert final_args['_variable_params'] == "{{ var_name }}"

def test_normalize_parameters_with_invalid_string_additional_args(parser, mocker):
    mocker.patch.object(Templar, 'is_template', return_value=False)
    with pytest.raises(AnsibleParserError, match="Complex args containing variables cannot use bare variables"):
        parser._normalize_parameters(thing={}, additional_args="var_name")

def test_normalize_parameters_with_invalid_additional_args_type(parser):
    with pytest.raises(AnsibleParserError, match='Complex args must be a dictionary or variable string'):
        parser._normalize_parameters(thing={}, additional_args=123)

def test_normalize_parameters_with_args_in_args(parser, mocker):
    mocker.patch('ansible.parsing.mod_args.ModuleArgsParser._normalize_old_style_args', return_value=('action', {'args': 'key=value'}))
    mocker.patch('ansible.parsing.splitter.parse_kv', return_value={'key': 'value'})
    action, final_args = parser._normalize_parameters(thing={})
    assert final_args['key'] == 'value'

def test_normalize_parameters_with_invalid_parameter(parser, mocker):
    mocker.patch('ansible.parsing.mod_args.ModuleArgsParser._normalize_old_style_args', return_value=('action', {'_ansible_invalid': 'value'}))
    with pytest.raises(AnsibleError, match="invalid parameter specified for action 'action'"):
        parser._normalize_parameters(thing={})
