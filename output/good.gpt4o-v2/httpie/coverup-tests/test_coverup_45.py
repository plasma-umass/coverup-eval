# file: httpie/cli/argparser.py:417-426
# asked: {"lines": [417, 418, 419, 420, 421, 422, 423, 426], "branches": [[418, 419], [418, 421], [421, 423], [421, 426]]}
# gained: {"lines": [417, 418, 419, 420, 421, 422, 423, 426], "branches": [[418, 419], [418, 421], [421, 423], [421, 426]]}

import pytest
from unittest import mock
from httpie.cli.argparser import HTTPieArgumentParser
from httpie.cli.constants import PRETTY_MAP, PRETTY_STDOUT_TTY_ONLY

@pytest.fixture
def parser():
    parser = HTTPieArgumentParser()
    parser.args = mock.Mock()
    parser.env = mock.Mock()
    return parser

def test_pretty_stdout_tty_only(parser):
    parser.args.prettify = PRETTY_STDOUT_TTY_ONLY
    parser.env.stdout_isatty = True
    parser._process_pretty_options()
    assert parser.args.prettify == PRETTY_MAP['all']

    parser.env.stdout_isatty = False
    parser.args.prettify = PRETTY_STDOUT_TTY_ONLY
    parser._process_pretty_options()
    assert parser.args.prettify == PRETTY_MAP['none']

def test_pretty_windows_output_file(parser):
    parser.args.prettify = True
    parser.env.is_windows = True
    parser.args.output_file = 'output.txt'
    with mock.patch.object(parser, 'error', side_effect=parser.error) as mock_error:
        with pytest.raises(SystemExit):
            parser._process_pretty_options()
        mock_error.assert_called_once_with('Only terminal output can be colorized on Windows.')

def test_pretty_map(parser):
    parser.args.prettify = 'all'
    parser.env.is_windows = False
    parser.args.output_file = None
    parser._process_pretty_options()
    assert parser.args.prettify == PRETTY_MAP['all']

    parser.args.prettify = 'none'
    parser._process_pretty_options()
    assert parser.args.prettify == PRETTY_MAP['none']
