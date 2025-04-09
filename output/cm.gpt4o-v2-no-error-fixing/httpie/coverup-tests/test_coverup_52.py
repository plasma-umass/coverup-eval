# file: httpie/output/streams.py:139-141
# asked: {"lines": [139, 140, 141], "branches": []}
# gained: {"lines": [139, 140, 141], "branches": []}

import pytest
from unittest.mock import Mock
from httpie.output.streams import PrettyStream
from httpie.output.processing import Formatting, Conversion

@pytest.fixture
def mock_msg():
    mock = Mock()
    mock.headers = {'Content-Type': 'application/json'}
    mock.content_type = 'application/json'
    mock.encoding = 'utf8'
    return mock

@pytest.fixture
def pretty_stream(mock_msg):
    formatting = Mock(spec=Formatting)
    conversion = Mock(spec=Conversion)
    stream = PrettyStream(conversion=conversion, formatting=formatting, msg=mock_msg)
    return stream

def test_get_headers(pretty_stream, mock_msg):
    pretty_stream.formatting.format_headers.return_value = 'Formatted-Headers'
    headers = pretty_stream.get_headers()
    assert headers == b'Formatted-Headers'
    pretty_stream.formatting.format_headers.assert_called_once_with(mock_msg.headers)
