# file lib/ansible/module_utils/common/validation.py:213-243
# lines [213, 228, 229, 230, 232, 233, 234, 235, 237, 238, 239, 240, 241, 243]
# branches ['229->230', '229->232', '232->233', '232->237', '234->232', '234->235', '237->238', '237->243', '239->240', '239->241']

import pytest
from ansible.module_utils.common.validation import check_required_arguments
from ansible.module_utils._text import to_native

def test_check_required_arguments_missing_with_context(mocker):
    mocker.patch('ansible.module_utils.common.validation.to_native', side_effect=lambda x: x)
    
    argument_spec = {
        'name': {'required': True},
        'state': {'required': True},
        'path': {'required': False}
    }
    parameters = {'path': '/some/path'}
    options_context = ['main', 'sub']

    with pytest.raises(TypeError) as excinfo:
        check_required_arguments(argument_spec, parameters, options_context)

    assert str(excinfo.value) == "missing required arguments: name, state found in main -> sub"

def test_check_required_arguments_missing_without_context(mocker):
    mocker.patch('ansible.module_utils.common.validation.to_native', side_effect=lambda x: x)
    
    argument_spec = {
        'name': {'required': True},
        'state': {'required': True},
        'path': {'required': False}
    }
    parameters = {'path': '/some/path'}

    with pytest.raises(TypeError) as excinfo:
        check_required_arguments(argument_spec, parameters)

    assert str(excinfo.value) == "missing required arguments: name, state"

def test_check_required_arguments_none_specified(mocker):
    mocker.patch('ansible.module_utils.common.validation.to_native', side_effect=lambda x: x)
    
    argument_spec = None
    parameters = {'path': '/some/path'}

    missing = check_required_arguments(argument_spec, parameters)

    assert missing == []

def test_check_required_arguments_no_missing(mocker):
    mocker.patch('ansible.module_utils.common.validation.to_native', side_effect=lambda x: x)
    
    argument_spec = {
        'name': {'required': True},
        'state': {'required': True},
        'path': {'required': False}
    }
    parameters = {'name': 'test', 'state': 'present', 'path': '/some/path'}

    missing = check_required_arguments(argument_spec, parameters)

    assert missing == []
