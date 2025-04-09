# file: httpie/output/streams.py:164-170
# asked: {"lines": [164, 165, 168, 169, 170], "branches": [[165, 168], [165, 169]]}
# gained: {"lines": [164, 165, 168, 169, 170], "branches": [[165, 168], [165, 169]]}

import pytest
from unittest.mock import Mock
from httpie.output.streams import PrettyStream
from httpie.output.processing import Formatting, Conversion

@pytest.fixture
def mock_environment():
    env = Mock()
    env.stdout_isatty = True
    env.stdout_encoding = 'utf-8'
    return env

@pytest.fixture
def pretty_stream(mock_environment):
    formatting = Mock(spec=Formatting)
    conversion = Mock(spec=Conversion)
    msg = Mock()
    msg.encoding = 'utf-8'
    msg.content_type = 'text/plain; charset=utf-8'
    stream = PrettyStream(conversion=conversion, formatting=formatting, env=mock_environment, msg=msg)
    return stream

def test_process_body_with_bytes(pretty_stream):
    chunk = b'hello'
    pretty_stream.formatting.format_body.return_value = 'formatted_hello'
    result = pretty_stream.process_body(chunk)
    assert result == b'formatted_hello'
    pretty_stream.formatting.format_body.assert_called_once_with(content='hello', mime='text/plain')

def test_process_body_with_str(pretty_stream):
    chunk = 'hello'
    pretty_stream.formatting.format_body.return_value = 'formatted_hello'
    result = pretty_stream.process_body(chunk)
    assert result == b'formatted_hello'
    pretty_stream.formatting.format_body.assert_called_once_with(content='hello', mime='text/plain')
