# file lib/ansible/parsing/mod_args.py:140-193
# lines [140, 145, 150, 151, 152, 153, 154, 155, 157, 159, 160, 162, 168, 169, 171, 174, 175, 176, 177, 178, 182, 183, 184, 185, 186, 190, 191, 193]
# branches ['151->152', '151->168', '152->153', '152->159', '154->155', '154->157', '159->160', '159->162', '168->169', '168->171', '174->175', '174->182', '176->177', '176->178', '182->183', '182->190', '183->184', '183->190', '185->183', '185->186', '190->191', '190->193']

import pytest
from ansible.parsing.mod_args import ModuleArgsParser
from ansible.errors import AnsibleParserError, AnsibleError
from ansible.template import Templar
from ansible.module_utils.six import string_types

@pytest.fixture
def mock_templar(mocker):
    mocker.patch('ansible.template.Templar.is_template', return_value=False)
    return Templar(loader=None)

def test_normalize_parameters_additional_args_string(mock_templar):
    parser = ModuleArgsParser()
    with pytest.raises(AnsibleParserError, match="Complex args containing variables cannot use bare variables"):
        parser._normalize_parameters(thing={}, additional_args="bare_variable")

def test_normalize_parameters_additional_args_invalid_type():
    parser = ModuleArgsParser()
    with pytest.raises(AnsibleParserError, match="Complex args must be a dictionary or variable string"):
        parser._normalize_parameters(thing={}, additional_args=123)

def test_normalize_parameters_action_none_with_args():
    parser = ModuleArgsParser()
    parser._normalize_old_style_args = lambda x: ('some_action', {'args': 'key1=value1 key2=value2'})
    action, final_args = parser._normalize_parameters(thing={})
    assert action == 'some_action'
    assert final_args == {'key1': 'value1', 'key2': 'value2'}

def test_normalize_parameters_invalid_parameter():
    parser = ModuleArgsParser()
    parser._normalize_old_style_args = lambda x: ('some_action', {'_ansible_invalid': 'value'})
    with pytest.raises(AnsibleError, match="invalid parameter specified for action 'some_action'"):
        parser._normalize_parameters(thing={})

def test_normalize_parameters_action_not_none():
    parser = ModuleArgsParser()
    parser._normalize_new_style_args = lambda x, y: {'key': 'value'}
    action, final_args = parser._normalize_parameters(thing={}, action='some_action')
    assert action == 'some_action'
    assert final_args == {'key': 'value'}

def test_normalize_parameters_additional_args_dict():
    parser = ModuleArgsParser()
    action, final_args = parser._normalize_parameters(thing={}, additional_args={'key': 'value'})
    assert final_args == {'key': 'value'}
