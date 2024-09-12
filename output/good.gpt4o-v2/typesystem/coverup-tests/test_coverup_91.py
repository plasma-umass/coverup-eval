# file: typesystem/tokenize/tokenize_yaml.py:25-109
# asked: {"lines": [26, 28, 29, 31, 33, 35, 36, 38, 39, 41, 42, 43, 44, 45, 47, 48, 49, 50, 51, 53, 54, 55, 56, 57, 59, 60, 61, 62, 63, 65, 66, 67, 68, 69, 71, 72, 73, 74, 75, 77, 78, 79, 80, 81, 83, 84, 87, 88, 91, 92, 95, 97, 99, 101, 103, 104, 105, 107, 108, 109], "branches": [[28, 29], [28, 31], [33, 35], [33, 38]]}
# gained: {"lines": [26, 28, 31, 33, 35, 36, 38, 39, 41, 42, 43, 44, 45, 47, 48, 49, 50, 51, 53, 54, 55, 56, 57, 59, 60, 61, 62, 63, 65, 66, 67, 68, 69, 71, 72, 73, 74, 75, 77, 78, 79, 80, 81, 83, 84, 87, 88, 91, 92, 95, 97, 99, 101, 103, 104, 105, 107, 108, 109], "branches": [[28, 31], [33, 35], [33, 38]]}

import pytest
from typesystem.tokenize.tokenize_yaml import tokenize_yaml
from typesystem.base import ParseError, Position
from typesystem.tokenize.tokens import DictToken, ListToken, ScalarToken, Token

def test_tokenize_yaml_empty_string():
    with pytest.raises(ParseError) as exc_info:
        tokenize_yaml("")
    error = exc_info.value
    assert error.messages()[0].text == "No content."
    assert error.messages()[0].code == "no_content"
    assert error.messages()[0].start_position == Position(column_no=1, line_no=1, char_index=0)

def test_tokenize_yaml_invalid_yaml():
    invalid_yaml = "key: [unclosed list"
    with pytest.raises(ParseError) as exc_info:
        tokenize_yaml(invalid_yaml)
    error = exc_info.value
    assert error.messages()[0].code == "parse_error"

def test_tokenize_yaml_valid_dict():
    yaml_content = "key: value"
    token = tokenize_yaml(yaml_content)
    assert isinstance(token, DictToken)
    assert token.value == {"key": "value"}

def test_tokenize_yaml_valid_list():
    yaml_content = "- item1\n- item2"
    token = tokenize_yaml(yaml_content)
    assert isinstance(token, ListToken)
    assert token.value == ["item1", "item2"]

def test_tokenize_yaml_valid_scalar():
    yaml_content = "scalar value"
    token = tokenize_yaml(yaml_content)
    assert isinstance(token, ScalarToken)
    assert token.value == "scalar value"

def test_tokenize_yaml_valid_int():
    yaml_content = "42"
    token = tokenize_yaml(yaml_content)
    assert isinstance(token, ScalarToken)
    assert token.value == 42

def test_tokenize_yaml_valid_float():
    yaml_content = "3.14"
    token = tokenize_yaml(yaml_content)
    assert isinstance(token, ScalarToken)
    assert token.value == 3.14

def test_tokenize_yaml_valid_bool():
    yaml_content = "true"
    token = tokenize_yaml(yaml_content)
    assert isinstance(token, ScalarToken)
    assert token.value is True

def test_tokenize_yaml_valid_null():
    yaml_content = "null"
    token = tokenize_yaml(yaml_content)
    assert isinstance(token, ScalarToken)
    assert token.value is None
