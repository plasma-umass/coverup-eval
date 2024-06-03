# file httpie/cli/argparser.py:417-426
# lines [418, 419, 420, 421, 422, 423, 426]
# branches ['418->419', '418->421', '421->423', '421->426']

import pytest
from unittest import mock
from httpie.cli.argparser import HTTPieArgumentParser, PRETTY_STDOUT_TTY_ONLY, PRETTY_MAP

class MockArgs:
    def __init__(self, prettify, output_file=None):
        self.prettify = prettify
        self.output_file = output_file

class MockEnv:
    def __init__(self, stdout_isatty, is_windows):
        self.stdout_isatty = stdout_isatty
        self.is_windows = is_windows
        self.stdout = mock.Mock()
        self.stderr = mock.Mock()

@pytest.fixture
def parser():
    return HTTPieArgumentParser()

def test_pretty_stdout_tty_only(parser, mocker):
    args = MockArgs(prettify=PRETTY_STDOUT_TTY_ONLY)
    env = MockEnv(stdout_isatty=True, is_windows=False)
    parser.args = args
    parser.env = env

    parser._process_pretty_options()
    assert parser.args.prettify == PRETTY_MAP['all']

def test_pretty_stdout_not_tty(parser, mocker):
    args = MockArgs(prettify=PRETTY_STDOUT_TTY_ONLY)
    env = MockEnv(stdout_isatty=False, is_windows=False)
    parser.args = args
    parser.env = env

    parser._process_pretty_options()
    assert parser.args.prettify == PRETTY_MAP['none']

def test_pretty_windows_output_file(parser, mocker):
    args = MockArgs(prettify=True, output_file='output.txt')
    env = MockEnv(stdout_isatty=True, is_windows=True)
    parser.args = args
    parser.env = env

    with pytest.raises(SystemExit):
        parser._process_pretty_options()

def test_pretty_map(parser, mocker):
    args = MockArgs(prettify='all')
    env = MockEnv(stdout_isatty=True, is_windows=False)
    parser.args = args
    parser.env = env

    parser._process_pretty_options()
    assert parser.args.prettify == PRETTY_MAP['all']
