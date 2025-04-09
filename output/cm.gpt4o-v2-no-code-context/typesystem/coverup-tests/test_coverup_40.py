# file: typesystem/tokenize/tokenize_json.py:158-162
# asked: {"lines": [158, 159, 160, 161, 162], "branches": []}
# gained: {"lines": [158, 159, 160, 161, 162], "branches": []}

import pytest
from typesystem.tokenize.tokenize_json import _TokenizingDecoder
from json import JSONDecoder, JSONDecodeError

def test_tokenizing_decoder_initialization():
    content = '{"key": "value"}'
    decoder = _TokenizingDecoder(content=content)
    assert hasattr(decoder, 'scan_once')

def test_tokenizing_decoder_invalid_content():
    content = '{"key": "value"'
    decoder = _TokenizingDecoder(content=content)
    with pytest.raises(JSONDecodeError):
        decoder.decode(content)

def test_tokenizing_decoder_with_additional_args():
    content = '{"key": "value"}'
    decoder = _TokenizingDecoder(content=content, object_hook=dict)
    assert hasattr(decoder, 'scan_once')
    assert decoder.object_hook == dict
