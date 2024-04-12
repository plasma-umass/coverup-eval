# file httpie/cli/argparser.py:117-134
# lines [117, 118, 119, 120, 122, 125, 126, 127, 128, 129, 130, 131, 132, 134]
# branches ['118->exit', '118->119', '119->120', '119->122', '126->127', '126->134', '130->131', '130->132']

import os
import re
import pytest
from unittest.mock import Mock
from httpie.cli.argparser import HTTPieArgumentParser

# Constants used in tests
URL_SCHEME_RE = re.compile(r'^https?://')
HTTPS_COMMAND = 'https'
DEFAULT_SCHEME = 'http'


@pytest.fixture
def mock_env(mocker):
    env = mocker.Mock()
    env.program_name = 'http'
    env.default_scheme = DEFAULT_SCHEME
    return env


@pytest.fixture
def parser(mock_env):
    # The 'env' argument is not expected by the HTTPieArgumentParser constructor.
    # We need to remove it and handle the environment within the test functions.
    # Instead, we pass the mock_env as a property of the parser instance.
    parser_instance = HTTPieArgumentParser()
    parser_instance.env = mock_env
    return parser_instance


def test_process_url_with_https_program_name(mocker, parser):
    # Mock os.path.basename to return 'https' to simulate the https command
    mocker.patch('os.path.basename', return_value=HTTPS_COMMAND)

    # Set the URL to a value that does not match the URL_SCHEME_RE
    parser.args = Mock(url='example.com', default_scheme=DEFAULT_SCHEME)

    # Call the method under test
    parser._process_url()

    # Assert the URL has been modified to include 'https://'
    assert parser.args.url == 'https://example.com'


def test_process_url_with_curl_style_shorthand_for_localhost(mocker, parser):
    # Mock os.path.basename to return the default program name
    mocker.patch('os.path.basename', return_value='http')

    # Set the URL to a curl style shorthand for localhost
    parser.args = Mock(url=':3000/foo', default_scheme=DEFAULT_SCHEME)

    # Call the method under test
    parser._process_url()

    # Assert the URL has been modified to include 'http://localhost:3000/foo'
    assert parser.args.url == 'http://localhost:3000/foo'


def test_process_url_without_curl_style_shorthand(mocker, parser):
    # Mock os.path.basename to return the default program name
    mocker.patch('os.path.basename', return_value='http')

    # Set the URL to a value that does not match the URL_SCHEME_RE and is not a shorthand
    parser.args = Mock(url='example.com', default_scheme=DEFAULT_SCHEME)

    # Call the method under test
    parser._process_url()

    # Assert the URL has been modified to include 'http://'
    assert parser.args.url == 'http://example.com'
