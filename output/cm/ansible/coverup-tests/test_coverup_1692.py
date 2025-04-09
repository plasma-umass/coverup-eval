# file lib/ansible/module_utils/common/validation.py:414-465
# lines [434]
# branches ['432->434', '459->461']

import pytest
from ansible.module_utils.common.validation import check_type_dict
from ansible.module_utils._text import to_bytes

@pytest.fixture
def safe_eval_mock(mocker):
    return mocker.patch('ansible.module_utils.common.validation.safe_eval')

def test_check_type_dict_with_valid_string():
    input_value = "key1=value1, key2=value2"
    expected_result = {'key1': 'value1', 'key2': 'value2'}
    assert check_type_dict(input_value) == expected_result

def test_check_type_dict_with_valid_json_string():
    input_value = '{"key1": "value1", "key2": "value2"}'
    expected_result = {'key1': 'value1', 'key2': 'value2'}
    assert check_type_dict(input_value) == expected_result

def test_check_type_dict_with_invalid_json_string(safe_eval_mock):
    input_value = '{"invalid_json": "without end"'
    safe_eval_mock.return_value = ({}, ValueError())
    with pytest.raises(TypeError):
        check_type_dict(input_value)

def test_check_type_dict_with_non_string():
    input_value = 12345
    with pytest.raises(TypeError):
        check_type_dict(input_value)

def test_check_type_dict_with_dict():
    input_value = {'key1': 'value1', 'key2': 'value2'}
    assert check_type_dict(input_value) == input_value

def test_check_type_dict_with_valid_string_eval(safe_eval_mock):
    input_value = "{'key1': 'value1', 'key2': 'value2'}"
    expected_result = {'key1': 'value1', 'key2': 'value2'}
    safe_eval_mock.return_value = (expected_result, None)
    assert check_type_dict(input_value) == expected_result

def test_check_type_dict_with_invalid_string_eval(safe_eval_mock):
    input_value = "{'key1': 'value1', 'key2':"
    safe_eval_mock.return_value = ({}, Exception())
    with pytest.raises(TypeError):
        check_type_dict(input_value)

def test_check_type_dict_with_valid_string_single_field():
    input_value = "key1=value1"
    expected_result = {'key1': 'value1'}
    assert check_type_dict(input_value) == expected_result

def test_check_type_dict_with_valid_string_escaped_characters():
    input_value = r'key1=value1\,key2\=value2'
    expected_result = {'key1': 'value1,key2=value2'}
    assert check_type_dict(input_value) == expected_result
