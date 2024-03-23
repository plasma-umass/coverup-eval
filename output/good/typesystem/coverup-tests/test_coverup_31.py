# file typesystem/tokenize/tokenize_json.py:158-162
# lines [158, 159, 160, 161, 162]
# branches []

import pytest
from typesystem.tokenize.tokenize_json import _TokenizingDecoder
from json.scanner import py_make_scanner

@pytest.fixture
def mock_make_scanner(mocker):
    return mocker.patch('typesystem.tokenize.tokenize_json._make_scanner', return_value=py_make_scanner)

def test_tokenizing_decoder_init(mock_make_scanner):
    content = '{"key": "value"}'
    decoder = _TokenizingDecoder(content=content)
    mock_make_scanner.assert_called_once_with(decoder, content)
    assert decoder.scan_once is py_make_scanner
