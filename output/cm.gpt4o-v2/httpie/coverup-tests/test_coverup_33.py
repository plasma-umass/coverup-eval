# file: httpie/output/streams.py:173-199
# asked: {"lines": [173, 174, 181, 183, 186, 187, 189, 190, 191, 192, 193, 194, 196, 197, 199], "branches": [[189, 190], [189, 196], [190, 191], [190, 194], [192, 193], [192, 194], [196, 197], [196, 199]]}
# gained: {"lines": [173, 174, 181, 183, 186, 187, 189, 190, 191, 192, 193, 194, 196, 197, 199], "branches": [[189, 190], [189, 196], [190, 191], [190, 194], [192, 193], [192, 194], [196, 197], [196, 199]]}

import pytest
from httpie.output.streams import BufferedPrettyStream, PrettyStream, BinarySuppressedError
from httpie.output.processing import Conversion, Formatting
from httpie.context import Environment
from unittest.mock import Mock

class MockMessage:
    def __init__(self, body_chunks):
        self.body_chunks = body_chunks
        self.content_type = 'text/plain'
        self.encoding = 'utf-8'

    def iter_body(self, chunk_size):
        for chunk in self.body_chunks:
            yield chunk

@pytest.fixture
def mock_conversion():
    conversion = Mock(spec=Conversion)
    conversion.get_converter.return_value = None
    return conversion

@pytest.fixture
def mock_formatting():
    formatting = Mock(spec=Formatting)
    formatting.format_body.side_effect = lambda content, mime: content
    return formatting

@pytest.fixture
def mock_env():
    env = Mock(spec=Environment)
    env.stdout_isatty = False
    env.stdout_encoding = 'utf-8'
    return env

def test_iter_body_with_text_body(mock_conversion, mock_formatting, mock_env):
    body_chunks = [b'Hello, ', b'world!']
    msg = MockMessage(body_chunks)
    stream = BufferedPrettyStream(env=mock_env, conversion=mock_conversion, formatting=mock_formatting, msg=msg)

    result = b''.join(stream.iter_body())
    assert result == b'Hello, world!'

def test_iter_body_with_binary_body(mock_conversion, mock_formatting, mock_env):
    body_chunks = [b'Hello, ', b'world!\0']
    msg = MockMessage(body_chunks)
    mock_conversion.get_converter.return_value = None
    stream = BufferedPrettyStream(env=mock_env, conversion=mock_conversion, formatting=mock_formatting, msg=msg)

    with pytest.raises(BinarySuppressedError):
        list(stream.iter_body())

def test_iter_body_with_conversion(mock_conversion, mock_formatting, mock_env):
    body_chunks = [b'Hello, ', b'world!\0']
    msg = MockMessage(body_chunks)
    mock_converter = Mock()
    mock_converter.convert.return_value = ('text/plain', b'Converted body')
    mock_conversion.get_converter.return_value = mock_converter
    stream = BufferedPrettyStream(env=mock_env, conversion=mock_conversion, formatting=mock_formatting, msg=msg)

    result = b''.join(stream.iter_body())
    assert result == b'Converted body'
    mock_converter.convert.assert_called_once_with(b'Hello, world!\0')
