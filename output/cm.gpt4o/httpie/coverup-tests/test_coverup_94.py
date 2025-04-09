# file httpie/cli/argparser.py:428-438
# lines [429, 430, 431, 432, 433, 434, 435, 436, 437, 438]
# branches ['429->430', '429->433', '433->434', '433->436', '434->435', '434->436', '436->exit', '436->438']

import pytest
from unittest import mock
import argparse
from httpie.cli.argparser import HTTPieArgumentParser

def test_process_download_options_offline():
    parser = HTTPieArgumentParser()
    parser.args = mock.Mock()
    parser.args.offline = True
    parser.args.download = True
    parser.args.download_resume = True

    parser._process_download_options()

    assert parser.args.download is False
    assert parser.args.download_resume is False

def test_process_download_options_download_resume_without_download(mocker):
    parser = HTTPieArgumentParser()
    parser.args = mock.Mock()
    parser.args.offline = False
    parser.args.download = False
    parser.args.download_resume = True

    mocker.patch.object(parser, 'error', side_effect=SystemExit)

    with pytest.raises(SystemExit):
        parser._process_download_options()

def test_process_download_options_download_resume_without_output_file(mocker):
    parser = HTTPieArgumentParser()
    parser.args = mock.Mock()
    parser.args.offline = False
    parser.args.download = True
    parser.args.download_resume = True
    parser.args.output_file = None

    mocker.patch.object(parser, 'error', side_effect=SystemExit)

    with pytest.raises(SystemExit):
        parser._process_download_options()
