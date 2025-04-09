# file: httpie/cli/argparser.py:417-426
# asked: {"lines": [417, 418, 419, 420, 421, 422, 423, 426], "branches": [[418, 419], [418, 421], [421, 423], [421, 426]]}
# gained: {"lines": [417, 418, 419, 420, 421, 422, 423, 426], "branches": [[418, 419], [418, 421], [421, 423], [421, 426]]}

import pytest
import argparse
from unittest.mock import Mock, patch
from httpie.cli.argparser import HTTPieArgumentParser
from httpie.cli.constants import PRETTY_MAP, PRETTY_STDOUT_TTY_ONLY

@pytest.fixture
def parser():
    parser = HTTPieArgumentParser()
    parser.args = Mock()
    parser.env = Mock()
    return parser

def test_prettify_stdout_tty_only(parser):
    parser.args.prettify = PRETTY_STDOUT_TTY_ONLY
    parser.env.stdout_isatty = True
    parser._process_pretty_options()
    assert parser.args.prettify == PRETTY_MAP['all']

    parser.args.prettify = PRETTY_STDOUT_TTY_ONLY
    parser.env.stdout_isatty = False
    parser._process_pretty_options()
    assert parser.args.prettify == PRETTY_MAP['none']

def test_prettify_windows_output_file(parser):
    parser.args.prettify = 'colors'
    parser.env.is_windows = True
    parser.args.output_file = 'output.txt'
    with pytest.raises(SystemExit):
        parser._process_pretty_options()

def test_prettify_map(parser):
    parser.args.prettify = 'colors'
    parser.env.is_windows = False
    parser.args.output_file = None
    parser._process_pretty_options()
    assert parser.args.prettify == PRETTY_MAP['colors']

    parser.args.prettify = 'none'
    parser._process_pretty_options()
    assert parser.args.prettify == PRETTY_MAP['none']
