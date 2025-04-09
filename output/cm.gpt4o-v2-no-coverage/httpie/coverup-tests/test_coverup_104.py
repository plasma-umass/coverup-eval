# file: httpie/output/streams.py:173-199
# asked: {"lines": [186, 187, 189, 190, 191, 192, 193, 194, 196, 197, 199], "branches": [[189, 190], [189, 196], [190, 191], [190, 194], [192, 193], [192, 194], [196, 197], [196, 199]]}
# gained: {"lines": [186, 187, 189, 190, 191, 192, 193, 194, 196, 199], "branches": [[189, 190], [189, 196], [190, 191], [190, 194], [192, 193], [196, 199]]}

import pytest
from unittest.mock import Mock, MagicMock
from httpie.output.streams import BufferedPrettyStream, BinarySuppressedError
from httpie.context import Environment

class MockMessage:
    def __init__(self, body_chunks, encoding='utf-8'):
        self.body_chunks = body_chunks
        self.content_type = 'text/plain'
        self.encoding = encoding

    def iter_body(self, chunk_size):
        for chunk in self.body_chunks:
            yield chunk

class MockConverter:
    def convert(self, body):
        return 'text/plain', body.upper()

@pytest.fixture
def mock_msg():
    return MockMessage([b'hello', b'world'])

@pytest.fixture
def mock_conversion():
    conversion = Mock()
    conversion.get_converter = Mock(return_value=MockConverter())
    return conversion

@pytest.fixture
def mock_formatting():
    formatting = Mock()
    formatting.format_body = Mock(side_effect=lambda content, mime: content)
    return formatting

@pytest.fixture
def mock_env():
    env = Mock(Environment)
    env.stdout_isatty = False
    env.stdout_encoding = 'utf-8'
    return env

def test_iter_body_text(mock_msg, mock_conversion, mock_formatting, mock_env):
    stream = BufferedPrettyStream(
        msg=mock_msg,
        conversion=mock_conversion,
        formatting=mock_formatting,
        env=mock_env
    )
    body = b''.join(stream.iter_body())
    assert body == b'helloworld'

def test_iter_body_binary(mock_msg, mock_conversion, mock_formatting, mock_env):
    mock_msg.body_chunks = [b'hello', b'\x00world']
    mock_conversion.get_converter = Mock(return_value=None)
    
    stream = BufferedPrettyStream(
        msg=mock_msg,
        conversion=mock_conversion,
        formatting=mock_formatting,
        env=mock_env
    )
    
    with pytest.raises(BinarySuppressedError):
        list(stream.iter_body())
