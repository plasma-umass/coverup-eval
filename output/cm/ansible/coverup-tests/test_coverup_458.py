# file lib/ansible/module_utils/common/validation.py:567-578
# lines [567, 574, 575, 576, 577, 578]
# branches ['574->575', '574->576', '576->577', '576->578']

import pytest
from ansible.module_utils.common.validation import check_type_jsonarg
from ansible.module_utils._text import to_text, to_bytes

# Define the test function
def test_check_type_jsonarg(mocker):
    # Mock the jsonify function to return a simple string representation of the input
    mocker.patch('ansible.module_utils.common.validation.jsonify', side_effect=lambda x: str(x))

    # Test with a text type
    text_value = to_text('{"key": "value"}')
    assert check_type_jsonarg(text_value) == text_value.strip()

    # Test with a binary type
    binary_value = to_bytes('{"key": "value"}')
    assert check_type_jsonarg(binary_value) == binary_value.strip()

    # Test with a list
    list_value = ['one', 'two', 'three']
    assert check_type_jsonarg(list_value) == str(list_value)

    # Test with a tuple
    tuple_value = ('one', 'two', 'three')
    assert check_type_jsonarg(tuple_value) == str(tuple_value)

    # Test with a dict
    dict_value = {'key': 'value'}
    assert check_type_jsonarg(dict_value) == str(dict_value)

    # Test with an unsupported type
    with pytest.raises(TypeError):
        check_type_jsonarg(42)

# Run the test function with the pytest fixture
def test_check_type_jsonarg_coverage(mocker):
    test_check_type_jsonarg(mocker)
