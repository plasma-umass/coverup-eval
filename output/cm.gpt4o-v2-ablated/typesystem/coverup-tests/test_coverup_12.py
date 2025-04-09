# file: typesystem/tokenize/tokenize_json.py:158-162
# asked: {"lines": [158, 159, 160, 161, 162], "branches": []}
# gained: {"lines": [158, 159, 160, 161, 162], "branches": []}

import pytest
import typing
from json import JSONDecoder
from typesystem.tokenize.tokenize_json import _TokenizingDecoder, _make_scanner

def test_tokenizing_decoder_initialization(mocker):
    # Mock the _make_scanner function to avoid actual scanning logic
    mock_make_scanner = mocker.patch('typesystem.tokenize.tokenize_json._make_scanner', return_value='mocked_scanner')

    # Initialize the _TokenizingDecoder with required arguments
    content = 'test_content'
    decoder = _TokenizingDecoder(content=content)

    # Assertions to verify the correct initialization
    assert decoder.scan_once == 'mocked_scanner'
    mock_make_scanner.assert_called_once_with(decoder, content)
