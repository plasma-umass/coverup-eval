# file string_utils/validation.py:345-365
# lines [345, 359, 360, 361, 362, 363, 365]
# branches ['359->360', '359->365']

import pytest
import json
from string_utils.validation import is_json

@pytest.fixture(autouse=True)
def mock_json_loads(mocker):
    mocker.patch('string_utils.validation.json.loads', side_effect=json.loads)

def test_is_json():
    # Test with valid JSON string
    valid_json_string = '{"name": "Peter"}'
    assert is_json(valid_json_string) == True

    # Test with valid JSON array
    valid_json_array = '[1, 2, 3]'
    assert is_json(valid_json_array) == True

    # Test with invalid JSON string
    invalid_json_string = '{nope}'
    assert is_json(invalid_json_string) == False

    # Test with non-string input
    non_string_input = 123
    assert is_json(non_string_input) == False

    # Test with string that causes json.loads to raise ValueError
    invalid_json_value = '{"name": Peter}'
    assert is_json(invalid_json_value) == False

def test_is_json_overflow_error(mocker):
    # Mock json.loads to raise OverflowError for testing purposes
    mocker.patch('string_utils.validation.json.loads', side_effect=OverflowError)
    
    # Test with string that causes json.loads to raise OverflowError
    overflow_json_string = '999E9999'
    assert is_json(overflow_json_string) == False
