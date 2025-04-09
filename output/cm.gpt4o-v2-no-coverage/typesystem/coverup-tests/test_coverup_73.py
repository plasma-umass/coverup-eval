# file: typesystem/tokenize/tokenize_json.py:158-162
# asked: {"lines": [158, 159, 160, 161, 162], "branches": []}
# gained: {"lines": [158, 159, 160, 161, 162], "branches": []}

import pytest
from typesystem.tokenize.tokenize_json import _TokenizingDecoder
from typesystem.tokenize.tokens import DictToken, ListToken, ScalarToken

def test_tokenizing_decoder_init():
    content = "test content"
    decoder = _TokenizingDecoder(content=content)
    assert decoder.scan_once is not None

def test_tokenizing_decoder_scan_once():
    content = "test content"
    decoder = _TokenizingDecoder(content=content)
    result = decoder.scan_once('"key"', 0)
    assert result[0].value == "key"
    assert result[1] == 5

    result = decoder.scan_once('{"key": "value"}', 0)
    assert isinstance(result[0], DictToken)
    assert result[1] == 16

    result = decoder.scan_once('[1, 2, 3]', 0)
    assert isinstance(result[0], ListToken)
    assert result[1] == 9

    result = decoder.scan_once('null', 0)
    assert result[0].value is None
    assert result[1] == 4

    result = decoder.scan_once('true', 0)
    assert result[0].value is True
    assert result[1] == 4

    result = decoder.scan_once('false', 0)
    assert result[0].value is False
    assert result[1] == 5

    result = decoder.scan_once('123', 0)
    assert result[0].value == 123
    assert result[1] == 3

    with pytest.raises(StopIteration):
        decoder.scan_once('invalid', 0)
