# file: typesystem/tokenize/tokenize_json.py:98-155
# asked: {"lines": [113, 114, 119, 120, 121, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 137, 138, 139, 140, 141, 143, 144, 145, 147], "branches": [[116, 119], [119, 120], [119, 124], [124, 125], [124, 127], [127, 128], [127, 130], [130, 131], [130, 133], [133, 134], [133, 137], [138, 139], [138, 147], [140, 141], [140, 143]]}
# gained: {"lines": [113, 114, 119, 120, 121, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 137, 138, 139, 140, 141, 143, 144, 145, 147], "branches": [[116, 119], [119, 120], [119, 124], [124, 125], [124, 127], [127, 128], [127, 130], [130, 131], [130, 133], [133, 134], [133, 137], [138, 139], [138, 147], [140, 141], [140, 143]]}

import pytest
from typesystem.tokenize.tokenize_json import _make_scanner
from typesystem.tokenize.tokens import DictToken, ListToken, ScalarToken, Token
import re
from json.decoder import JSONDecodeError

class MockContext:
    def __init__(self):
        self.parse_array = self.mock_parse_array
        self.parse_string = self.mock_parse_string
        self.strict = True
        self.parse_float = float
        self.parse_int = int
        self.memo = {}
    
    def mock_parse_array(self, args, scan_once):
        return ([], args[1] + 1)
    
    def mock_parse_string(self, string, idx, strict):
        return ("mock_string", idx + 1)

NUMBER_RE = re.compile(r'(-?\d+)(\.\d*)?([eE][+-]?\d+)?')

def test_scan_once_index_error():
    context = MockContext()
    scanner = _make_scanner(context, "")
    with pytest.raises(StopIteration) as excinfo:
        scanner("", 1)
    assert excinfo.value.args[0] == 1

def test_scan_once_dict_token():
    context = MockContext()
    scanner = _make_scanner(context, "")
    with pytest.raises(JSONDecodeError):
        scanner("{", 0)

def test_scan_once_list_token():
    context = MockContext()
    scanner = _make_scanner(context, "")
    token, end = scanner("[", 0)
    assert isinstance(token, ListToken)
    assert token._value == []
    assert end == 2

def test_scan_once_null_token():
    context = MockContext()
    scanner = _make_scanner(context, "")
    token, end = scanner("null", 0)
    assert isinstance(token, ScalarToken)
    assert token._value is None
    assert end == 4

def test_scan_once_true_token():
    context = MockContext()
    scanner = _make_scanner(context, "")
    token, end = scanner("true", 0)
    assert isinstance(token, ScalarToken)
    assert token._value is True
    assert end == 4

def test_scan_once_false_token():
    context = MockContext()
    scanner = _make_scanner(context, "")
    token, end = scanner("false", 0)
    assert isinstance(token, ScalarToken)
    assert token._value is False
    assert end == 5

def test_scan_once_number_token():
    context = MockContext()
    scanner = _make_scanner(context, "")
    token, end = scanner("123", 0)
    assert isinstance(token, ScalarToken)
    assert token._value == 123
    assert end == 3

def test_scan_once_number_float_token():
    context = MockContext()
    scanner = _make_scanner(context, "")
    token, end = scanner("123.45", 0)
    assert isinstance(token, ScalarToken)
    assert token._value == 123.45
    assert end == 6

def test_scan_once_stop_iteration():
    context = MockContext()
    scanner = _make_scanner(context, "")
    with pytest.raises(StopIteration) as excinfo:
        scanner("x", 0)
    assert excinfo.value.args[0] == 0
