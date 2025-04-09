# file: httpie/output/writer.py:19-51
# asked: {"lines": [19, 23, 24, 26, 27, 28, 29, 30, 31, 32, 33, 34, 37, 38, 40, 41, 42, 44, 45, 46, 47, 49, 51], "branches": [[26, 27], [26, 28], [41, 42], [41, 44], [47, 49], [47, 51]]}
# gained: {"lines": [19, 23, 24, 26, 27, 28, 29, 30, 31, 32, 33, 34, 37, 38, 40, 41, 42, 44, 45, 46, 47, 49, 51], "branches": [[26, 27], [26, 28], [41, 42], [41, 44], [47, 49], [47, 51]]}

import pytest
import argparse
import requests
import errno
from unittest import mock
from httpie.output.writer import write_message
from httpie.context import Environment

@pytest.fixture
def env():
    return Environment()

@pytest.fixture
def args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--stream', action='store_true')
    parser.add_argument('--prettify', nargs='*', default=[])
    parser.add_argument('--debug', action='store_true')
    parser.add_argument('--traceback', action='store_true')
    return parser.parse_args([])

def test_write_message_no_body_no_headers(env, args):
    request = requests.Request('GET', 'http://example.com').prepare()
    write_message(request, env, args)
    # No assertions needed, just ensuring no exceptions and no output

def test_write_message_with_body(env, args, monkeypatch):
    request = requests.Request('GET', 'http://example.com').prepare()
    args.stream = True

    def mock_build_output_stream_for_message(*args, **kwargs):
        return mock.Mock()

    def mock_write_stream(*args, **kwargs):
        pass

    monkeypatch.setattr('httpie.output.writer.build_output_stream_for_message', mock_build_output_stream_for_message)
    monkeypatch.setattr('httpie.output.writer.write_stream', mock_write_stream)

    write_message(request, env, args, with_body=True)
    # No assertions needed, just ensuring no exceptions

def test_write_message_with_headers(env, args, monkeypatch):
    request = requests.Request('GET', 'http://example.com').prepare()
    args.stream = True

    def mock_build_output_stream_for_message(*args, **kwargs):
        return mock.Mock()

    def mock_write_stream(*args, **kwargs):
        pass

    monkeypatch.setattr('httpie.output.writer.build_output_stream_for_message', mock_build_output_stream_for_message)
    monkeypatch.setattr('httpie.output.writer.write_stream', mock_write_stream)

    write_message(request, env, args, with_headers=True)
    # No assertions needed, just ensuring no exceptions

def test_write_message_with_colors_win(env, args, monkeypatch):
    request = requests.Request('GET', 'http://example.com').prepare()
    args.prettify = ['colors']
    env.is_windows = True

    def mock_build_output_stream_for_message(*args, **kwargs):
        return mock.Mock()

    def mock_write_stream_with_colors_win_py3(*args, **kwargs):
        pass

    monkeypatch.setattr('httpie.output.writer.build_output_stream_for_message', mock_build_output_stream_for_message)
    monkeypatch.setattr('httpie.output.writer.write_stream_with_colors_win_py3', mock_write_stream_with_colors_win_py3)

    write_message(request, env, args, with_body=True)
    # No assertions needed, just ensuring no exceptions

def test_write_message_ioerror(env, args, monkeypatch):
    request = requests.Request('GET', 'http://example.com').prepare()
    args.stream = True

    def mock_build_output_stream_for_message(*args, **kwargs):
        return mock.Mock()

    def mock_write_stream(*args, **kwargs):
        raise IOError(errno.EPIPE, 'Broken pipe')

    monkeypatch.setattr('httpie.output.writer.build_output_stream_for_message', mock_build_output_stream_for_message)
    monkeypatch.setattr('httpie.output.writer.write_stream', mock_write_stream)

    with mock.patch.object(env.stderr, 'write') as mock_stderr_write:
        write_message(request, env, args, with_body=True)
        mock_stderr_write.assert_called_once_with('\n')

def test_write_message_ioerror_with_traceback(env, args, monkeypatch):
    request = requests.Request('GET', 'http://example.com').prepare()
    args.stream = True
    args.traceback = True

    def mock_build_output_stream_for_message(*args, **kwargs):
        return mock.Mock()

    def mock_write_stream(*args, **kwargs):
        raise IOError(errno.EPIPE, 'Broken pipe')

    monkeypatch.setattr('httpie.output.writer.build_output_stream_for_message', mock_build_output_stream_for_message)
    monkeypatch.setattr('httpie.output.writer.write_stream', mock_write_stream)

    with pytest.raises(IOError):
        write_message(request, env, args, with_body=True)
