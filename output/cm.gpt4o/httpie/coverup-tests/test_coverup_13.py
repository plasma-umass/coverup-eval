# file httpie/cli/argparser.py:69-106
# lines [69, 72, 73, 75, 76, 77, 78, 79, 80, 81, 82, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 99, 101, 102, 103, 104, 106]
# branches ['77->78', '77->79', '94->95', '94->96', '99->101', '99->106', '101->102', '101->103', '103->104', '103->106']

import pytest
import argparse
from unittest import mock
from httpie.cli.argparser import HTTPieArgumentParser
from httpie.context import Environment

@pytest.fixture
def mock_env():
    env = mock.Mock(spec=Environment)
    env.stdin = mock.Mock()
    env.stdin_isatty = False
    return env

def test_parse_args_with_debug(mock_env):
    parser = HTTPieArgumentParser()
    args = ['--debug']
    namespace = argparse.Namespace()
    namespace.debug = True
    namespace.ignore_stdin = False
    namespace.compress = False
    namespace.chunked = False
    namespace.multipart = False

    with mock.patch.object(parser, '_apply_no_options') as mock_apply_no_options, \
         mock.patch.object(parser, '_process_request_type') as mock_process_request_type, \
         mock.patch.object(parser, '_process_download_options') as mock_process_download_options, \
         mock.patch.object(parser, '_setup_standard_streams') as mock_setup_standard_streams, \
         mock.patch.object(parser, '_process_output_options') as mock_process_output_options, \
         mock.patch.object(parser, '_process_pretty_options') as mock_process_pretty_options, \
         mock.patch.object(parser, '_process_format_options') as mock_process_format_options, \
         mock.patch.object(parser, '_guess_method') as mock_guess_method, \
         mock.patch.object(parser, '_parse_items') as mock_parse_items, \
         mock.patch.object(parser, '_body_from_file') as mock_body_from_file, \
         mock.patch.object(parser, '_process_url') as mock_process_url, \
         mock.patch.object(parser, '_process_auth') as mock_process_auth:
        
        parsed_args = parser.parse_args(mock_env, args, namespace)
        
        assert parsed_args.debug is True
        assert parsed_args.traceback is True
        assert parser.has_stdin_data is True

        mock_apply_no_options.assert_called_once()
        mock_process_request_type.assert_called_once()
        mock_process_download_options.assert_called_once()
        mock_setup_standard_streams.assert_called_once()
        mock_process_output_options.assert_called_once()
        mock_process_pretty_options.assert_called_once()
        mock_process_format_options.assert_called_once()
        mock_guess_method.assert_called_once()
        mock_parse_items.assert_called_once()
        mock_body_from_file.assert_called_once_with(mock_env.stdin)
        mock_process_url.assert_called_once()
        mock_process_auth.assert_called_once()

def test_parse_args_with_compress_and_chunked(mock_env):
    parser = HTTPieArgumentParser()
    args = ['--compress', '--chunked']
    namespace = argparse.Namespace()
    namespace.debug = False
    namespace.ignore_stdin = False
    namespace.compress = True
    namespace.chunked = True
    namespace.multipart = False

    with pytest.raises(SystemExit):
        parser.parse_args(mock_env, args, namespace)

def test_parse_args_with_compress_and_multipart(mock_env):
    parser = HTTPieArgumentParser()
    args = ['--compress', '--multipart']
    namespace = argparse.Namespace()
    namespace.debug = False
    namespace.ignore_stdin = False
    namespace.compress = True
    namespace.chunked = False
    namespace.multipart = True

    with pytest.raises(SystemExit):
        parser.parse_args(mock_env, args, namespace)
