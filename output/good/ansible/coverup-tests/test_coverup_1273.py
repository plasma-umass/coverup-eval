# file lib/ansible/module_utils/common/validation.py:173-210
# lines [189, 197, 210]
# branches ['188->189', '196->197', '199->198', '202->210', '203->210', '204->203', '206->208']

import pytest
from ansible.module_utils.common.validation import check_required_by
from ansible.module_utils._text import to_native

def test_check_required_by_missing_parameters(mocker):
    # Mocking string_types to be just a tuple with str for the test
    mocker.patch('ansible.module_utils.common.validation.string_types', (str,))

    # Test case to cover line 189
    assert check_required_by(None, {}) == {}

    # Test case to cover line 197
    requirements = {'key1': 'value1'}
    parameters = {'key1': None}
    assert check_required_by(requirements, parameters) == {}

    # Test case to cover line 210
    requirements = {'key1': []}
    parameters = {'key1': 'some_value', 'value2': None}
    assert check_required_by(requirements, parameters) == {'key1': []}

    # Test case to cover branch 199->198
    requirements = {'key1': ['value1']}
    parameters = {'key1': 'some_value', 'value1': None}
    with pytest.raises(TypeError) as excinfo:
        check_required_by(requirements, parameters)
    assert "missing parameter(s) required by 'key1': value1" in str(excinfo.value)

    # Test case to cover branch 204->203
    requirements = {'key1': ['value1']}
    parameters = {'key1': 'some_value'}
    with pytest.raises(TypeError) as excinfo:
        check_required_by(requirements, parameters)
    assert "missing parameter(s) required by 'key1': value1" in str(excinfo.value)

    # Test case to cover branch 206->208
    requirements = {'key1': ['value1']}
    parameters = {'key1': 'some_value'}
    options_context = ['parent1', 'parent2']
    with pytest.raises(TypeError) as excinfo:
        check_required_by(requirements, parameters, options_context=options_context)
    expected_message = "missing parameter(s) required by 'key1': value1 found in parent1 -> parent2"
    assert expected_message in to_native(str(excinfo.value))
