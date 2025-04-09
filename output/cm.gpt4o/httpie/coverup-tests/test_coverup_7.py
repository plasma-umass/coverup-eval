# file httpie/cli/argparser.py:117-134
# lines [117, 118, 119, 120, 122, 125, 126, 127, 128, 129, 130, 131, 132, 134]
# branches ['118->exit', '118->119', '119->120', '119->122', '126->127', '126->134', '130->131', '130->132']

import pytest
import re
import os
from unittest import mock
from httpie.cli.argparser import HTTPieArgumentParser

URL_SCHEME_RE = re.compile(r'^[a-zA-Z][a-zA-Z0-9+.-]*://')

@pytest.fixture
def mock_env():
    with mock.patch('httpie.cli.argparser.os.path.basename') as mock_basename:
        with mock.patch('httpie.cli.argparser.os.environ') as mock_environ:
            yield mock_basename, mock_environ

def test_process_url_with_https(mock_env):
    mock_basename, mock_environ = mock_env
    mock_basename.return_value = 'https'
    mock_environ.program_name = 'https'

    parser = HTTPieArgumentParser()
    parser.args = mock.Mock()
    parser.args.url = 'example.com'
    parser.args.default_scheme = 'http'
    parser.env = mock_environ

    parser._process_url()

    assert parser.args.url == 'https://example.com'

def test_process_url_with_default_scheme(mock_env):
    mock_basename, mock_environ = mock_env
    mock_basename.return_value = 'http'
    mock_environ.program_name = 'http'

    parser = HTTPieArgumentParser()
    parser.args = mock.Mock()
    parser.args.url = 'example.com'
    parser.args.default_scheme = 'http'
    parser.env = mock_environ

    parser._process_url()

    assert parser.args.url == 'http://example.com'

def test_process_url_with_shorthand(mock_env):
    mock_basename, mock_environ = mock_env
    mock_basename.return_value = 'http'
    mock_environ.program_name = 'http'

    parser = HTTPieArgumentParser()
    parser.args = mock.Mock()
    parser.args.url = ':3000/foo'
    parser.args.default_scheme = 'http'
    parser.env = mock_environ

    parser._process_url()

    assert parser.args.url == 'http://localhost:3000/foo'
