# file lib/ansible/module_utils/common/validation.py:173-210
# lines [197]
# branches ['196->197', '199->198']

import pytest
from ansible.module_utils.common.validation import check_required_by
from ansible.module_utils._text import to_native

def test_check_required_by_missing_branches(mocker):
    # Mock string_types to be just str for simplicity
    mocker.patch('ansible.module_utils.common.validation.string_types', new=(str,))

    # Define requirements and parameters that will trigger the missing lines/branches
    requirements = {'key1': 'required1'}
    parameters = {'key1': 'value1', 'required1': None}

    # Call the function with the mocked requirements and parameters
    with pytest.raises(TypeError) as excinfo:
        check_required_by(requirements, parameters)

    # Verify the exception message
    assert "missing parameter(s) required by 'key1': required1" in str(excinfo.value)

    # Clean up after the test
    mocker.stopall()
