# file: httpie/output/streams.py:139-141
# asked: {"lines": [139, 140, 141], "branches": []}
# gained: {"lines": [139, 140, 141], "branches": []}

import pytest
from unittest.mock import Mock
from httpie.output.streams import PrettyStream
from httpie.output.processing import Formatting

@pytest.fixture
def pretty_stream():
    mock_msg = Mock()
    mock_msg.headers = {'Content-Type': 'application/json'}
    mock_msg.content_type = 'application/json; charset=utf-8'
    mock_msg.encoding = 'utf-8'
    
    mock_env = Mock()
    mock_env.stdout_isatty = True
    mock_env.stdout_encoding = 'utf-8'
    
    formatting = Mock(spec=Formatting)
    formatting.format_headers.return_value = 'Formatted-Headers'
    
    stream = PrettyStream(env=mock_env, msg=mock_msg, formatting=formatting, conversion=Mock())
    return stream, formatting

def test_get_headers(pretty_stream):
    stream, formatting = pretty_stream
    headers = stream.get_headers()
    formatting.format_headers.assert_called_once_with({'Content-Type': 'application/json'})
    assert headers == b'Formatted-Headers'
