# file lib/ansible/parsing/splitter.py:49-103
# lines [49, 57, 59, 60, 61, 62, 63, 64, 65, 66, 67, 69, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 84, 85, 87, 88, 91, 92, 94, 96, 100, 101, 103]
# branches ['60->61', '60->103', '66->67', '66->69', '72->73', '72->100', '74->75', '74->96', '77->78', '79->77', '79->80', '91->92', '91->94', '100->101', '100->103']

import pytest
from ansible.errors import AnsibleParserError
from ansible.parsing.splitter import parse_kv, split_args
from ansible.module_utils._text import to_text

def test_parse_kv_with_escaped_equals(mocker):
    # Mock the split_args function to return a list with an escaped equals
    mocker.patch('ansible.parsing.splitter.split_args', return_value=['key\\=value'])

    # Call parse_kv with the mocked split_args
    result = parse_kv('key\\=value')

    # Assert that the escaped equals is correctly handled and added to _raw_params
    assert result == {'_raw_params': 'key=value'}

def test_parse_kv_with_unescaped_equals(mocker):
    # Mock the split_args function to return a list with an unescaped equals
    mocker.patch('ansible.parsing.splitter.split_args', return_value=['key=value'])

    # Call parse_kv with the mocked split_args
    result = parse_kv('key=value')

    # Assert that the unescaped equals is correctly parsed into a key-value pair
    assert result == {'key': 'value'}

def test_parse_kv_with_no_closing_quotation(mocker):
    # Mock the split_args function to raise a ValueError indicating no closing quotation
    mocker.patch('ansible.parsing.splitter.split_args', side_effect=ValueError("no closing quotation"))

    # Assert that AnsibleParserError is raised with the expected message
    with pytest.raises(AnsibleParserError) as excinfo:
        parse_kv('key="value')

    assert "error parsing argument string, try quoting the entire line." in str(excinfo.value)

def test_parse_kv_with_index_error(mocker):
    # Mock the split_args function to raise an IndexError
    mocker.patch('ansible.parsing.splitter.split_args', side_effect=IndexError("list index out of range"))

    # Assert that AnsibleParserError is raised with the expected message
    with pytest.raises(AnsibleParserError) as excinfo:
        parse_kv('key=value')

    assert "Unable to parse argument string" in str(excinfo.value)

def test_parse_kv_with_check_raw_enabled(mocker):
    # Mock the split_args function to return a list with a key that should be treated as raw
    mocker.patch('ansible.parsing.splitter.split_args', return_value=['unexpected_key=value'])

    # Call parse_kv with the mocked split_args and check_raw enabled
    result = parse_kv('unexpected_key=value', check_raw=True)

    # Assert that the unexpected key is added to _raw_params
    assert result == {'_raw_params': 'unexpected_key=value'}

def test_parse_kv_with_check_raw_disabled(mocker):
    # Mock the split_args function to return a list with a key that should not be treated as raw
    mocker.patch('ansible.parsing.splitter.split_args', return_value=['creates=value'])

    # Call parse_kv with the mocked split_args and check_raw disabled
    result = parse_kv('creates=value', check_raw=False)

    # Assert that the key is not added to _raw_params
    assert result == {'creates': 'value'}
