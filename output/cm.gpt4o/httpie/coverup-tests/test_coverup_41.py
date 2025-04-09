# file httpie/output/streams.py:89-115
# lines [89, 90, 97, 99, 100, 101, 103, 106, 108, 110, 111, 112, 113, 114, 115]
# branches ['101->103', '101->106', '111->exit', '111->112', '112->113', '112->114']

import pytest
from httpie.output.streams import EncodedStream, BinarySuppressedError
from httpie.context import Environment
from unittest.mock import Mock

def test_encoded_stream_stdout_isatty(mocker):
    # Mock the environment
    mock_env = mocker.Mock(spec=Environment)
    mock_env.stdout_isatty = True
    mock_env.stdout_encoding = 'utf-8'
    
    # Mock the message
    mock_msg = mocker.Mock()
    mock_msg.encoding = 'utf-8'
    mock_msg.iter_lines.return_value = [(b'line1\n', b'\n'), (b'line2\n', b'\n')]
    
    # Create the EncodedStream instance
    stream = EncodedStream(env=mock_env, msg=mock_msg)
    
    # Verify the output encoding
    assert stream.output_encoding == 'utf-8'
    
    # Verify the body iteration
    body = list(stream.iter_body())
    assert body == [b'line1\n\n', b'line2\n\n']

def test_encoded_stream_stdout_not_isatty(mocker):
    # Mock the environment
    mock_env = mocker.Mock(spec=Environment)
    mock_env.stdout_isatty = False
    
    # Mock the message
    mock_msg = mocker.Mock()
    mock_msg.encoding = 'latin1'
    mock_msg.iter_lines.return_value = [(b'line1\n', b'\n'), (b'line2\n', b'\n')]
    
    # Create the EncodedStream instance
    stream = EncodedStream(env=mock_env, msg=mock_msg)
    
    # Verify the output encoding
    assert stream.output_encoding == 'latin1'
    
    # Verify the body iteration
    body = list(stream.iter_body())
    assert body == [b'line1\n\n', b'line2\n\n']

def test_encoded_stream_binary_suppressed_error(mocker):
    # Mock the environment
    mock_env = mocker.Mock(spec=Environment)
    mock_env.stdout_isatty = False
    
    # Mock the message
    mock_msg = mocker.Mock()
    mock_msg.encoding = 'utf-8'
    mock_msg.iter_lines.return_value = [(b'line1\0\n', b'\n')]
    
    # Create the EncodedStream instance
    stream = EncodedStream(env=mock_env, msg=mock_msg)
    
    # Verify that BinarySuppressedError is raised
    with pytest.raises(BinarySuppressedError):
        list(stream.iter_body())
