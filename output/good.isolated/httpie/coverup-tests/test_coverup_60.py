# file httpie/output/writer.py:93-118
# lines [93, 100, 101, 102, 104, 105, 106, 107, 108, 109, 110, 111, 112, 114, 115, 118]
# branches ['114->exit', '114->118']

import argparse
import pytest
from unittest.mock import Mock
from httpie.output.writer import build_output_stream_for_message
import requests

MESSAGE_SEPARATOR_BYTES = b'\n\n'

class DummyStream:
    def __init__(self, msg, with_headers, with_body, **kwargs):
        self.msg = msg
        self.with_headers = with_headers
        self.with_body = with_body

    def __iter__(self):
        if self.with_headers:
            yield b'headers'
        if self.with_body:
            yield b'body'

def get_stream_type_and_kwargs(env, args):
    return DummyStream, {}

@pytest.fixture
def mock_env(mocker):
    env = Mock(stdout_isatty=True)
    mocker.patch('httpie.output.writer.get_stream_type_and_kwargs', side_effect=get_stream_type_and_kwargs)
    return env

@pytest.fixture
def mock_args():
    return argparse.Namespace()

def test_build_output_stream_for_message_with_body(mock_env, mock_args):
    request = requests.PreparedRequest()
    request.prepare(method='GET', url='http://example.com')

    stream = build_output_stream_for_message(
        args=mock_args,
        env=mock_env,
        requests_message=request,
        with_headers=True,
        with_body=True
    )

    output = list(stream)
    assert output == [b'headers', b'body', MESSAGE_SEPARATOR_BYTES]

def test_build_output_stream_for_message_without_body(mock_env, mock_args):
    request = requests.PreparedRequest()
    request.prepare(method='GET', url='http://example.com')

    stream = build_output_stream_for_message(
        args=mock_args,
        env=mock_env,
        requests_message=request,
        with_headers=True,
        with_body=False
    )

    output = list(stream)
    assert output == [b'headers']

def test_build_output_stream_for_message_upload_chunk(mock_env, mock_args):
    response = requests.Response()
    response.is_body_upload_chunk = True

    stream = build_output_stream_for_message(
        args=mock_args,
        env=mock_env,
        requests_message=response,
        with_headers=True,
        with_body=True
    )

    output = list(stream)
    assert output == [b'headers', b'body']
    assert MESSAGE_SEPARATOR_BYTES not in output
