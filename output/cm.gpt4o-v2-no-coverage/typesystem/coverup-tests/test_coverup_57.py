# file: typesystem/tokenize/tokenize_json.py:165-180
# asked: {"lines": [165, 166, 167, 169, 171, 172, 174, 175, 176, 177, 179, 180], "branches": [[166, 167], [166, 169], [169, 171], [169, 174]]}
# gained: {"lines": [165, 166, 167, 169, 171, 172, 174, 175, 176, 177, 179, 180], "branches": [[166, 167], [166, 169], [169, 171], [169, 174]]}

import pytest
from typesystem.tokenize.tokenize_json import tokenize_json
from typesystem.base import ParseError, Position
from typesystem.tokenize.tokens import Token
from json.decoder import JSONDecodeError

class MockTokenizingDecoder:
    def __init__(self, content):
        self.content = content

    def decode(self, content):
        if content == "invalid":
            raise JSONDecodeError("Invalid JSON", content, 0)
        return Token(value="mock", start_index=0, end_index=len(content))

def test_tokenize_json_with_bytes(monkeypatch):
    def mock_decoder_init(self, content):
        self.content = content

    def mock_decoder_decode(self, content):
        return Token(value="mock", start_index=0, end_index=len(content))

    monkeypatch.setattr("typesystem.tokenize.tokenize_json._TokenizingDecoder.__init__", mock_decoder_init)
    monkeypatch.setattr("typesystem.tokenize.tokenize_json._TokenizingDecoder.decode", mock_decoder_decode)

    result = tokenize_json(b'{"key": "value"}')
    assert isinstance(result, Token)
    assert result._value == "mock"

def test_tokenize_json_with_empty_string():
    with pytest.raises(ParseError) as exc_info:
        tokenize_json("")
    assert str(exc_info.value) == "No content."

def test_tokenize_json_with_invalid_json(monkeypatch):
    def mock_decoder_init(self, content):
        self.content = content

    def mock_decoder_decode(self, content):
        raise JSONDecodeError("Invalid JSON", content, 0)

    monkeypatch.setattr("typesystem.tokenize.tokenize_json._TokenizingDecoder.__init__", mock_decoder_init)
    monkeypatch.setattr("typesystem.tokenize.tokenize_json._TokenizingDecoder.decode", mock_decoder_decode)

    with pytest.raises(ParseError) as exc_info:
        tokenize_json("invalid")
    assert str(exc_info.value) == "Invalid JSON."

def test_tokenize_json_with_valid_string(monkeypatch):
    def mock_decoder_init(self, content):
        self.content = content

    def mock_decoder_decode(self, content):
        return Token(value="mock", start_index=0, end_index=len(content))

    monkeypatch.setattr("typesystem.tokenize.tokenize_json._TokenizingDecoder.__init__", mock_decoder_init)
    monkeypatch.setattr("typesystem.tokenize.tokenize_json._TokenizingDecoder.decode", mock_decoder_decode)

    result = tokenize_json('{"key": "value"}')
    assert isinstance(result, Token)
    assert result._value == "mock"
