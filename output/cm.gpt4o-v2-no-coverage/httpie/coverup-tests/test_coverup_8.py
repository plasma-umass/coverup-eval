# file: httpie/cli/argparser.py:377-415
# asked: {"lines": [377, 384, 385, 386, 387, 388, 389, 392, 393, 395, 396, 397, 398, 399, 400, 401, 403, 405, 406, 408, 409, 411, 414, 415], "branches": [[386, 0], [386, 387], [392, 393], [392, 395], [395, 396], [395, 405], [396, 397], [396, 398], [398, 399], [398, 400], [400, 401], [400, 403], [405, 406], [405, 408], [411, 0], [411, 414]]}
# gained: {"lines": [377, 384, 385, 386, 392, 393, 395, 396, 397, 398, 399, 400, 401, 403, 405, 406, 408, 409, 411, 414, 415], "branches": [[386, 0], [392, 393], [392, 395], [395, 396], [395, 405], [396, 397], [396, 398], [398, 399], [398, 400], [400, 401], [400, 403], [405, 406], [411, 0], [411, 414]]}

import pytest
from unittest.mock import Mock
import argparse
from httpie.cli.argparser import HTTPieArgumentParser
from httpie.cli.constants import OUTPUT_OPTIONS, OUTPUT_OPTIONS_DEFAULT, OUTPUT_OPTIONS_DEFAULT_OFFLINE, OUTPUT_OPTIONS_DEFAULT_STDOUT_REDIRECTED, OUT_RESP_BODY

@pytest.fixture
def parser():
    parser = HTTPieArgumentParser()
    parser.args = Mock()
    parser.env = Mock()
    return parser

def test_process_output_options_verbose(parser):
    parser.args.verbose = True
    parser.args.output_options = None
    parser.args.output_options_history = None
    parser.args.offline = False
    parser.env.stdout_isatty = True
    parser.args.download = False

    parser._process_output_options()

    assert parser.args.all is True
    assert parser.args.output_options == ''.join(OUTPUT_OPTIONS)
    assert parser.args.output_options_history == ''.join(OUTPUT_OPTIONS)

def test_process_output_options_offline(parser):
    parser.args.verbose = False
    parser.args.output_options = None
    parser.args.output_options_history = None
    parser.args.offline = True
    parser.env.stdout_isatty = True
    parser.args.download = False

    parser._process_output_options()

    assert parser.args.output_options == OUTPUT_OPTIONS_DEFAULT_OFFLINE
    assert parser.args.output_options_history == OUTPUT_OPTIONS_DEFAULT_OFFLINE

def test_process_output_options_stdout_redirected(parser):
    parser.args.verbose = False
    parser.args.output_options = None
    parser.args.output_options_history = None
    parser.args.offline = False
    parser.env.stdout_isatty = False
    parser.args.download = False

    parser._process_output_options()

    assert parser.args.output_options == OUTPUT_OPTIONS_DEFAULT_STDOUT_REDIRECTED
    assert parser.args.output_options_history == OUTPUT_OPTIONS_DEFAULT_STDOUT_REDIRECTED

def test_process_output_options_default(parser):
    parser.args.verbose = False
    parser.args.output_options = None
    parser.args.output_options_history = None
    parser.args.offline = False
    parser.env.stdout_isatty = True
    parser.args.download = False

    parser._process_output_options()

    assert parser.args.output_options == OUTPUT_OPTIONS_DEFAULT
    assert parser.args.output_options_history == OUTPUT_OPTIONS_DEFAULT

def test_process_output_options_download(parser):
    parser.args.verbose = False
    parser.args.output_options = ''.join(OUTPUT_OPTIONS)
    parser.args.output_options_history = None
    parser.args.offline = False
    parser.env.stdout_isatty = True
    parser.args.download = True

    parser._process_output_options()

    assert OUT_RESP_BODY not in parser.args.output_options
    assert parser.args.output_options_history == ''.join(OUTPUT_OPTIONS)
