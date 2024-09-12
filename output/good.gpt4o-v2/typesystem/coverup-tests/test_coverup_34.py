# file: typesystem/tokenize/tokenize_json.py:158-162
# asked: {"lines": [158, 159, 160, 161, 162], "branches": []}
# gained: {"lines": [158, 159, 160, 161, 162], "branches": []}

import pytest
from typesystem.tokenize.tokenize_json import _TokenizingDecoder

def test_tokenizing_decoder_initialization():
    content = "test content"
    decoder = _TokenizingDecoder(content=content)
    assert decoder.scan_once is not None

def test_tokenizing_decoder_scan_once():
    content = "test content"
    decoder = _TokenizingDecoder(content=content)
    result = decoder.scan_once('"key": "value"', 0)
    assert result is not None
