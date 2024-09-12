# file: httpie/cli/argparser.py:148-186
# asked: {"lines": [154, 155, 157, 159, 164, 165, 167, 171, 172, 173, 174, 175, 177, 179, 180, 181, 183, 184, 185, 186], "branches": [[155, 157], [155, 167], [157, 159], [157, 164], [167, 171], [167, 183], [175, 177], [175, 179], [183, 0], [183, 184], [185, 0], [185, 186]]}
# gained: {"lines": [154, 155, 157, 159, 164, 165, 167, 171, 172, 173, 174, 175, 177, 179, 180, 181, 183, 184, 185, 186], "branches": [[155, 157], [155, 167], [157, 159], [157, 164], [167, 171], [167, 183], [175, 177], [175, 179], [183, 0], [183, 184], [185, 0], [185, 186]]}

import pytest
import argparse
import io
import errno
from unittest import mock
from httpie.cli.argparser import HTTPieArgumentParser, HTTPieHelpFormatter
from httpie.context import Environment

@pytest.fixture
def parser():
    parser = HTTPieArgumentParser(formatter_class=HTTPieHelpFormatter)
    parser.env = mock.Mock()
    parser.args = mock.Mock()
    return parser

def test_setup_standard_streams_output_file_specified(parser):
    parser.args.output_file = io.StringIO()
    parser.args.download = False
    parser.args.quiet = False
    parser.env.stdout_isatty = True
    parser._setup_standard_streams()
    assert parser.args.output_file_specified is True

def test_setup_standard_streams_download_no_output_file(parser):
    parser.args.output_file = None
    parser.args.download = True
    parser.args.quiet = False
    parser.env.stdout_isatty = False
    stdout = io.StringIO()
    stderr = io.StringIO()
    parser.env.stdout = stdout
    parser.env.stderr = stderr
    parser.env.stderr_isatty = False
    parser._setup_standard_streams()
    assert parser.args.output_file == stdout
    assert parser.env.stdout == stderr
    assert parser.env.stdout_isatty == parser.env.stderr_isatty

def test_setup_standard_streams_download_with_output_file(parser):
    parser.args.output_file = io.StringIO()
    parser.args.download = True
    parser.args.quiet = False
    parser.env.stdout_isatty = True
    stderr = io.StringIO()
    parser.env.stderr = stderr
    parser.env.stderr_isatty = False
    parser._setup_standard_streams()
    assert parser.env.stdout == stderr
    assert parser.env.stdout_isatty == parser.env.stderr_isatty

def test_setup_standard_streams_output_file_truncate(parser):
    parser.args.output_file = io.StringIO("test")
    parser.args.download = False
    parser.args.quiet = False
    parser.env.stdout_isatty = True
    parser._setup_standard_streams()
    assert parser.args.output_file.getvalue() == ""
    assert parser.env.stdout == parser.args.output_file
    assert parser.env.stdout_isatty is False

def test_setup_standard_streams_output_file_truncate_ioerror(parser):
    parser.args.output_file = mock.Mock()
    parser.args.output_file.seek = mock.Mock()
    parser.args.output_file.truncate = mock.Mock(side_effect=IOError(errno.EINVAL, "Invalid argument"))
    parser.args.download = False
    parser.args.quiet = False
    parser.env.stdout_isatty = True
    parser._setup_standard_streams()
    parser.args.output_file.truncate.assert_called_once()
    assert parser.env.stdout == parser.args.output_file
    assert parser.env.stdout_isatty is False

def test_setup_standard_streams_output_file_truncate_ioerror_raise(parser):
    parser.args.output_file = mock.Mock()
    parser.args.output_file.seek = mock.Mock()
    parser.args.output_file.truncate = mock.Mock(side_effect=IOError(errno.EPERM, "Operation not permitted"))
    parser.args.download = False
    parser.args.quiet = False
    parser.env.stdout_isatty = True
    with pytest.raises(IOError):
        parser._setup_standard_streams()

def test_setup_standard_streams_quiet(parser):
    parser.args.output_file = None
    parser.args.download = False
    parser.args.quiet = True
    devnull = io.StringIO()
    parser.env.devnull = devnull
    parser._setup_standard_streams()
    assert parser.env.stderr == devnull
    assert parser.env.stdout == devnull

def test_setup_standard_streams_quiet_with_output_file(parser):
    parser.args.output_file = io.StringIO()
    parser.args.download = False
    parser.args.quiet = True
    devnull = io.StringIO()
    parser.env.devnull = devnull
    parser._setup_standard_streams()
    assert parser.env.stderr == devnull
    assert parser.env.stdout == parser.args.output_file
