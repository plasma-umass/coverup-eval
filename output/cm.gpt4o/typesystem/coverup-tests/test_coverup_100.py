# file typesystem/tokenize/tokenize_json.py:98-155
# lines [113, 114]
# branches []

import pytest
from typesystem.tokenize.tokenize_json import _make_scanner, Token, ScalarToken, DictToken, ListToken
from unittest.mock import Mock

def test_make_scanner_index_error():
    context = Mock()
    context.parse_array = Mock()
    context.parse_string = Mock()
    context.strict = Mock()
    context.parse_float = Mock()
    context.parse_int = Mock()
    context.memo = Mock()

    scanner = _make_scanner(context, "test_content")

    with pytest.raises(StopIteration) as excinfo:
        scanner("", 0)
    
    assert excinfo.value.args[0] == 0
