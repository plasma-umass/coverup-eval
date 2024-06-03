# file httpie/output/writer.py:93-118
# lines [100, 101, 102, 104, 105, 106, 107, 108, 109, 110, 111, 112, 114, 115, 118]
# branches ['114->exit', '114->118']

import pytest
import argparse
import requests
from httpie.output.writer import build_output_stream_for_message
from httpie.context import Environment
from httpie.models import HTTPRequest, HTTPResponse
from unittest.mock import MagicMock

def test_build_output_stream_for_message(mocker):
    # Mock the get_stream_type_and_kwargs function
    mock_stream_class = MagicMock()
    mocker.patch('httpie.output.writer.get_stream_type_and_kwargs', return_value=(mock_stream_class, {}))

    # Create a mock environment
    env = Environment()
    env.stdout_isatty = True

    # Create a mock requests.Response object
    response = requests.Response()
    response._content = b'Test content'
    response.status_code = 200
    response.headers['Content-Type'] = 'text/plain'

    # Create argparse.Namespace with necessary attributes
    args = argparse.Namespace()

    # Mock the stream_class to yield specific content
    mock_stream_instance = MagicMock()
    mock_stream_instance.__iter__.return_value = iter([b'Test content'])
    mock_stream_class.return_value = mock_stream_instance

    # Test with with_headers=True and with_body=True
    stream = build_output_stream_for_message(args, env, response, with_headers=True, with_body=True)
    output = b''.join(stream)
    assert b'Test content' in output

    # Test the MESSAGE_SEPARATOR_BYTES condition
    response.is_body_upload_chunk = False
    mock_stream_instance.__iter__.return_value = iter([b'Test content', b'\n\n'])
    stream = build_output_stream_for_message(args, env, response, with_headers=True, with_body=True)
    output = b''.join(stream)
    assert b'Test content' in output
    assert b'\n\n' in output  # Assuming MESSAGE_SEPARATOR_BYTES is b'\n\n'

    # Clean up
    del response
    del env
    del args
