# file: httpie/cli/argparser.py:428-438
# asked: {"lines": [429, 430, 431, 432, 433, 434, 435, 436, 437, 438], "branches": [[429, 430], [429, 433], [433, 434], [433, 436], [434, 435], [434, 436], [436, 0], [436, 438]]}
# gained: {"lines": [429, 430, 431, 432, 433, 434, 435, 436, 437, 438], "branches": [[429, 430], [429, 433], [433, 434], [433, 436], [434, 435], [436, 0], [436, 438]]}

import pytest
import argparse
from httpie.cli.argparser import HTTPieArgumentParser

class MockArgs:
    def __init__(self, offline=False, download=False, download_resume=False, output_file=None):
        self.offline = offline
        self.download = download
        self.download_resume = download_resume
        self.output_file = output_file

@pytest.fixture
def parser(mocker):
    parser = HTTPieArgumentParser()
    mocker.patch.object(parser, 'env', mocker.Mock(stdout=mocker.Mock(), stderr=mocker.Mock()))
    return parser

def test_process_download_options_offline(parser, mocker):
    args = MockArgs(offline=True)
    mocker.patch.object(parser, 'args', args)
    parser._process_download_options()
    assert not parser.args.download
    assert not parser.args.download_resume

def test_process_download_options_no_download(parser, mocker):
    args = MockArgs(download=False, download_resume=True)
    mocker.patch.object(parser, 'args', args)
    with pytest.raises(SystemExit):
        parser._process_download_options()

def test_process_download_options_resume_without_output(parser, mocker):
    args = MockArgs(download=True, download_resume=True, output_file=None)
    mocker.patch.object(parser, 'args', args)
    with pytest.raises(SystemExit):
        parser._process_download_options()

def test_process_download_options_valid(parser, mocker):
    args = MockArgs(download=True, download_resume=True, output_file='output.txt')
    mocker.patch.object(parser, 'args', args)
    parser._process_download_options()
    assert parser.args.download
    assert parser.args.download_resume
    assert parser.args.output_file == 'output.txt'
