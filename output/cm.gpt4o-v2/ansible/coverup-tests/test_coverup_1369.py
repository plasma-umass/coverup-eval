# file: lib/ansible/parsing/splitter.py:49-103
# asked: {"lines": [63, 64, 65, 66, 67, 69, 81, 84, 85], "branches": [[60, 103], [66, 67], [66, 69], [79, 77]]}
# gained: {"lines": [63, 64, 65, 66, 67, 69, 81, 84, 85], "branches": [[66, 67], [66, 69], [79, 77]]}

import pytest
from ansible.parsing.splitter import parse_kv
from ansible.errors import AnsibleParserError

def test_parse_kv_index_error(mocker):
    mocker.patch('ansible.parsing.splitter.split_args', side_effect=IndexError)
    with pytest.raises(AnsibleParserError, match="Unable to parse argument string"):
        parse_kv("some args")

def test_parse_kv_value_error_no_closing_quotation(mocker):
    mocker.patch('ansible.parsing.splitter.split_args', side_effect=ValueError("no closing quotation"))
    with pytest.raises(AnsibleParserError, match="error parsing argument string, try quoting the entire line."):
        parse_kv("some args")

def test_parse_kv_value_error_other(mocker):
    mocker.patch('ansible.parsing.splitter.split_args', side_effect=ValueError("some other error"))
    with pytest.raises(ValueError, match="some other error"):
        parse_kv("some args")

def test_parse_kv_escaped_equals(mocker):
    mocker.patch('ansible.parsing.splitter.split_args', return_value=["key\\=value"])
    result = parse_kv("key\\=value")
    assert result == {'_raw_params': 'key=value'}

def test_parse_kv_check_raw(mocker):
    mocker.patch('ansible.parsing.splitter.split_args', return_value=["key=value"])
    result = parse_kv("key=value", check_raw=True)
    assert result == {'_raw_params': 'key=value'}

def test_parse_kv_normal_case(mocker):
    mocker.patch('ansible.parsing.splitter.split_args', return_value=["key=value"])
    result = parse_kv("key=value")
    assert result == {'key': 'value'}
