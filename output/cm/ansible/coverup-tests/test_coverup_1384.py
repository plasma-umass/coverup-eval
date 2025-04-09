# file lib/ansible/module_utils/common/validation.py:246-335
# lines [296]
# branches ['295->296', '328->335']

import pytest
from ansible.module_utils.common.validation import check_required_if

def test_check_required_if_with_none_requirements(mocker):
    # Mock the to_native function to simply return the message
    mocker.patch('ansible.module_utils.common.validation.to_native', side_effect=lambda x: x)

    # Test with requirements set to None
    parameters = {'state': 'present', 'path': '/some/path'}
    assert check_required_if(None, parameters) == []

def test_check_required_if_with_missing_requirements(mocker):
    # Mock the to_native function to simply return the message
    mocker.patch('ansible.module_utils.common.validation.to_native', side_effect=lambda x: x)

    # Define requirements that will trigger the missing branch
    requirements = [
        ['state', 'present', ('path', 'mode'), True]
    ]
    parameters = {'state': 'present'}

    # Test with requirements that will raise TypeError
    with pytest.raises(TypeError) as exc_info:
        check_required_if(requirements, parameters)

    # Verify the exception message
    assert "state is present but any of the following are missing: path, mode" in str(exc_info.value)

    # Verify that the options_context is included in the message if provided
    options_context = ['context1', 'context2']
    with pytest.raises(TypeError) as exc_info:
        check_required_if(requirements, parameters, options_context=options_context)

    # Verify the exception message with options_context
    assert "state is present but any of the following are missing: path, mode found in context1 -> context2" in str(exc_info.value)
