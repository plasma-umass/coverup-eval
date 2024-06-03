# file lib/ansible/module_utils/common/arg_spec.py:257-278
# lines [257, 258, 264, 265, 267, 268, 270, 271, 272, 273, 275, 276, 278]
# branches ['270->271', '270->275', '275->276', '275->278']

import pytest
from unittest.mock import MagicMock, patch
from ansible.module_utils.common.arg_spec import ArgumentSpecValidator, ModuleArgumentSpecValidator

@pytest.fixture
def mock_deprecate_warn():
    with patch('ansible.module_utils.common.arg_spec.deprecate') as mock_deprecate, \
         patch('ansible.module_utils.common.arg_spec.warn') as mock_warn:
        yield mock_deprecate, mock_warn

def test_module_argument_spec_validator(mock_deprecate_warn):
    mock_deprecate, mock_warn = mock_deprecate_warn

    # Create a mock result object with _deprecations and _warnings
    mock_result = MagicMock()
    mock_result._deprecations = [{'name': 'old_option', 'version': '2.0', 'date': '2023-01-01', 'collection_name': 'test_collection'}]
    mock_result._warnings = [{'option': 'new_option', 'alias': 'old_option'}]

    # Mock the validate method of the parent class to return the mock result
    with patch.object(ArgumentSpecValidator, 'validate', return_value=mock_result):
        argument_spec = {'some_option': {'type': 'str'}}
        validator = ModuleArgumentSpecValidator(argument_spec)
        parameters = {}  # Add any necessary parameters for validation
        result = validator.validate(parameters)

        # Assertions to verify that deprecate and warn were called with the expected arguments
        mock_deprecate.assert_called_once_with(
            "Alias 'old_option' is deprecated. See the module docs for more information",
            version='2.0', date='2023-01-01', collection_name='test_collection'
        )
        mock_warn.assert_called_once_with('Both option new_option and its alias old_option are set.')

        # Verify that the result is the mock result
        assert result == mock_result
