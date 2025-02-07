# file: httpie/cli/argparser.py:428-438
# asked: {"lines": [429, 430, 431, 432, 433, 434, 435, 436, 437, 438], "branches": [[429, 430], [429, 433], [433, 434], [433, 436], [434, 435], [434, 436], [436, 0], [436, 438]]}
# gained: {"lines": [429, 430, 431, 432, 433, 434, 435, 436, 437, 438], "branches": [[429, 430], [429, 433], [433, 434], [433, 436], [434, 435], [436, 0], [436, 438]]}

import pytest
from httpie.cli.argparser import HTTPieArgumentParser
import argparse
from unittest import mock

class MockArgs:
    def __init__(self, offline=False, download=False, download_resume=False, output_file=None):
        self.offline = offline
        self.download = download
        self.download_resume = download_resume
        self.output_file = output_file

class MockEnv:
    def __init__(self):
        self.stdout = mock.Mock()
        self.stderr = mock.Mock()

@pytest.fixture
def parser():
    parser = HTTPieArgumentParser()
    parser.env = MockEnv()
    return parser

def test_process_download_options_offline(parser):
    parser.args = MockArgs(offline=True, download=True, download_resume=True)
    parser._process_download_options()
    assert not parser.args.download
    assert not parser.args.download_resume

def test_process_download_options_no_download_with_resume(parser):
    parser.args = MockArgs(download=False, download_resume=True)
    with pytest.raises(SystemExit):
        parser._process_download_options()

def test_process_download_options_resume_without_output(parser):
    parser.args = MockArgs(download=True, download_resume=True, output_file=None)
    with pytest.raises(SystemExit):
        parser._process_download_options()

def test_process_download_options_valid(parser):
    parser.args = MockArgs(download=True, download_resume=True, output_file='file.txt')
    parser._process_download_options()
    assert parser.args.download
    assert parser.args.download_resume
    assert parser.args.output_file == 'file.txt'
