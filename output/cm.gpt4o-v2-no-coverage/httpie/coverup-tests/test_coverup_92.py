# file: httpie/cli/argparser.py:285-296
# asked: {"lines": [291, 292, 296], "branches": [[291, 292], [291, 296]]}
# gained: {"lines": [291, 292, 296], "branches": [[291, 292], [291, 296]]}

import pytest
from unittest.mock import Mock, patch
from httpie.cli.argparser import HTTPieArgumentParser

@pytest.fixture
def parser():
    parser = HTTPieArgumentParser()
    parser.args = Mock()
    return parser

def test_body_from_file_with_data(parser):
    parser.args.data = True
    parser.args.files = False
    fd = Mock()

    with patch.object(parser, 'error') as mock_error:
        parser._body_from_file(fd)
        mock_error.assert_called_once_with(
            'Request body (from stdin or a file) and request '
            'data (key=value) cannot be mixed. Pass '
            '--ignore-stdin to let key/value take priority. '
            'See https://httpie.org/doc#scripting for details.'
        )

def test_body_from_file_with_files(parser):
    parser.args.data = False
    parser.args.files = True
    fd = Mock()

    with patch.object(parser, 'error') as mock_error:
        parser._body_from_file(fd)
        mock_error.assert_called_once_with(
            'Request body (from stdin or a file) and request '
            'data (key=value) cannot be mixed. Pass '
            '--ignore-stdin to let key/value take priority. '
            'See https://httpie.org/doc#scripting for details.'
        )

def test_body_from_file_no_data_or_files(parser):
    parser.args.data = False
    parser.args.files = False
    fd = Mock()
    fd.buffer = b'test data'

    parser._body_from_file(fd)
    assert parser.args.data == fd.buffer

def test_body_from_file_no_buffer(parser):
    parser.args.data = False
    parser.args.files = False
    fd = Mock()
    del fd.buffer

    parser._body_from_file(fd)
    assert parser.args.data == fd
