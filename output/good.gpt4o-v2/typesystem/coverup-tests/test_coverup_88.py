# file: typesystem/tokenize/tokenize_json.py:20-95
# asked: {"lines": [29, 30, 31, 32, 35, 37, 38, 39, 40, 42, 43, 44, 45, 46, 48, 49, 50, 51, 52, 53, 56, 57, 58, 59, 60, 62, 63, 64, 65, 66, 67, 68, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 95], "branches": [[37, 38], [37, 48], [38, 39], [38, 42], [42, 43], [42, 44], [44, 45], [44, 48], [49, 50], [56, 57], [56, 60], [58, 59], [58, 60], [63, 64], [63, 70], [65, 66], [65, 70], [77, 78], [77, 82], [84, 85], [84, 86], [86, 87], [86, 88], [91, 49], [91, 92]]}
# gained: {"lines": [29, 30, 31, 32, 35, 37, 38, 39, 40, 42, 43, 44, 45, 46, 48, 49, 50, 51, 52, 53, 56, 57, 58, 59, 60, 62, 63, 64, 65, 70, 71, 74, 75, 76, 77, 78, 79, 82, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 95], "branches": [[37, 38], [38, 39], [38, 42], [42, 43], [42, 44], [44, 45], [44, 48], [49, 50], [56, 57], [56, 60], [58, 59], [63, 64], [65, 70], [77, 78], [77, 82], [84, 85], [84, 86], [86, 87], [86, 88], [91, 92]]}

import pytest
from json.decoder import JSONDecodeError
from typesystem.tokenize.tokenize_json import _TokenizingJSONObject
from typesystem.tokenize.tokens import ScalarToken, Token

def test_tokenizing_json_object_empty_object():
    s_and_end = ("{}", 1)
    strict = True
    scan_once = lambda s, end: (Token(), end)
    memo = {}
    content = ""
    result, end = _TokenizingJSONObject(s_and_end, strict, scan_once, memo, content)
    assert result == {}
    assert end == 2

def test_tokenizing_json_object_with_whitespace():
    s_and_end = ('{ "key": "value" }', 1)
    strict = True
    scan_once = lambda s, end: (ScalarToken("value", end, end + 5, ""), end + 7)
    memo = {}
    content = ""
    result, end = _TokenizingJSONObject(s_and_end, strict, scan_once, memo, content)
    assert any(token.value == "key" for token in result.keys())
    assert any(token.value == "value" for token in result.values())
    assert end == 18

def test_tokenizing_json_object_missing_colon():
    s_and_end = ('{ "key" "value" }', 1)
    strict = True
    scan_once = lambda s, end: (ScalarToken("value", end, end + 5, ""), end + 7)
    memo = {}
    content = ""
    with pytest.raises(JSONDecodeError, match="Expecting ':' delimiter"):
        _TokenizingJSONObject(s_and_end, strict, scan_once, memo, content)

def test_tokenizing_json_object_missing_comma():
    s_and_end = ('{ "key": "value" "key2": "value2" }', 1)
    strict = True
    scan_once = lambda s, end: (ScalarToken("value", end, end + 5, ""), end + 7)
    memo = {}
    content = ""
    with pytest.raises(JSONDecodeError, match="Expecting ',' delimiter"):
        _TokenizingJSONObject(s_and_end, strict, scan_once, memo, content)

def test_tokenizing_json_object_missing_quotes():
    s_and_end = ('{ key: "value" }', 1)
    strict = True
    scan_once = lambda s, end: (ScalarToken("value", end, end + 5, ""), end + 7)
    memo = {}
    content = ""
    with pytest.raises(JSONDecodeError, match="Expecting property name enclosed in double quotes"):
        _TokenizingJSONObject(s_and_end, strict, scan_once, memo, content)

def test_tokenizing_json_object_trailing_comma():
    s_and_end = ('{ "key": "value", }', 1)
    strict = True
    scan_once = lambda s, end: (ScalarToken("value", end, end + 5, ""), end + 7)
    memo = {}
    content = ""
    with pytest.raises(JSONDecodeError, match="Expecting property name enclosed in double quotes"):
        _TokenizingJSONObject(s_and_end, strict, scan_once, memo, content)
