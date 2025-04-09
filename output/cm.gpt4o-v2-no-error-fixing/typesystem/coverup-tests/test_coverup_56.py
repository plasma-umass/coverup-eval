# file: typesystem/tokenize/tokenize_json.py:158-162
# asked: {"lines": [160, 161, 162], "branches": []}
# gained: {"lines": [160, 161, 162], "branches": []}

import pytest
from typesystem.tokenize.tokenize_json import _TokenizingDecoder

def test_tokenizing_decoder_initialization():
    content = "test content"
    decoder = _TokenizingDecoder(content=content)
    assert hasattr(decoder, 'scan_once')
    assert callable(decoder.scan_once)
