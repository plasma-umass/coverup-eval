# file: httpie/output/streams.py:139-141
# asked: {"lines": [139, 140, 141], "branches": []}
# gained: {"lines": [139, 140, 141], "branches": []}

import pytest
from unittest.mock import Mock, MagicMock
from httpie.output.processing import Formatting, Conversion
from httpie.models import HTTPMessage

class TestPrettyStream:
    @pytest.fixture
    def mock_encoded_stream(self, monkeypatch):
        from httpie.output.streams import EncodedStream
        mock_stream = Mock(spec=EncodedStream)
        mock_stream.output_encoding = 'utf8'
        mock_stream.msg = MagicMock(spec=HTTPMessage)
        mock_stream.msg.headers = {'Content-Type': 'application/json'}
        monkeypatch.setattr('httpie.output.streams.EncodedStream', mock_stream)
        return mock_stream

    @pytest.fixture
    def pretty_stream(self, mock_encoded_stream):
        from httpie.output.streams import PrettyStream
        formatting = Mock(spec=Formatting)
        formatting.format_headers.return_value = 'Formatted-Headers'
        conversion = Mock(spec=Conversion)
        stream = PrettyStream(conversion=conversion, formatting=formatting, msg=mock_encoded_stream.msg)
        stream.output_encoding = mock_encoded_stream.output_encoding
        return stream

    def test_get_headers(self, pretty_stream):
        headers = pretty_stream.get_headers()
        assert headers == b'Formatted-Headers'
        pretty_stream.formatting.format_headers.assert_called_once_with(pretty_stream.msg.headers)
