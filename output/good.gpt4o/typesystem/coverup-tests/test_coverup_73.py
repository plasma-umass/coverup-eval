# file typesystem/tokenize/tokenize_json.py:158-162
# lines [160, 161, 162]
# branches []

import pytest
from typesystem.tokenize.tokenize_json import _TokenizingDecoder
from json import JSONDecodeError

def test_tokenizing_decoder_with_content():
    content = '{"key": "value"}'
    decoder = _TokenizingDecoder(content=content)
    
    assert decoder.scan_once is not None

    with pytest.raises(JSONDecodeError):
        decoder.decode('{"key": "value"')  # Invalid JSON to trigger scan_once

