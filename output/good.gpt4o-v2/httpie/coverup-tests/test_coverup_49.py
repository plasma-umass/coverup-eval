# file: httpie/output/streams.py:164-170
# asked: {"lines": [164, 165, 168, 169, 170], "branches": [[165, 168], [165, 169]]}
# gained: {"lines": [164, 165, 168, 169, 170], "branches": [[165, 168], [165, 169]]}

import pytest
from unittest.mock import Mock
from httpie.output.streams import PrettyStream
from httpie.output.processing import Formatting, Conversion

@pytest.fixture
def pretty_stream():
    mock_msg = Mock()
    mock_msg.encoding = 'utf-8'
    mock_msg.content_type = 'text/plain'
    conversion = Mock(spec=Conversion)
    formatting = Mock(spec=Formatting)
    return PrettyStream(conversion=conversion, formatting=formatting, msg=mock_msg)

def test_process_body_with_bytes(pretty_stream):
    chunk = b'test bytes'
    pretty_stream.formatting.format_body = Mock(return_value='formatted body')
    
    result = pretty_stream.process_body(chunk)
    
    pretty_stream.formatting.format_body.assert_called_once_with(content='test bytes', mime='text/plain')
    assert result == b'formatted body'

def test_process_body_with_str(pretty_stream):
    chunk = 'test string'
    pretty_stream.formatting.format_body = Mock(return_value='formatted body')
    
    result = pretty_stream.process_body(chunk)
    
    pretty_stream.formatting.format_body.assert_called_once_with(content='test string', mime='text/plain')
    assert result == b'formatted body'
