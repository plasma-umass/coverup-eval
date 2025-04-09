# file: httpie/cli/argparser.py:428-438
# asked: {"lines": [428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438], "branches": [[429, 430], [429, 433], [433, 434], [433, 436], [434, 435], [434, 436], [436, 0], [436, 438]]}
# gained: {"lines": [428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438], "branches": [[429, 430], [429, 433], [433, 434], [433, 436], [434, 435], [436, 0], [436, 438]]}

import pytest
from httpie.cli.argparser import HTTPieArgumentParser
import argparse

class MockArgs:
    def __init__(self, offline=False, download=False, download_resume=False, output_file=None):
        self.offline = offline
        self.download = download
        self.download_resume = download_resume
        self.output_file = output_file

@pytest.fixture
def parser():
    return HTTPieArgumentParser()

def test_process_download_options_offline(parser, mocker):
    args = MockArgs(offline=True)
    parser.args = args
    parser._process_download_options()
    assert parser.args.download is False
    assert parser.args.download_resume is False

def test_process_download_options_download_resume_without_download(parser, mocker):
    args = MockArgs(download_resume=True)
    parser.args = args
    mocker.patch.object(parser, 'error', side_effect=Exception('--continue only works with --download'))
    with pytest.raises(Exception) as excinfo:
        parser._process_download_options()
    assert str(excinfo.value) == '--continue only works with --download'

def test_process_download_options_download_resume_without_output_file(parser, mocker):
    args = MockArgs(download=True, download_resume=True)
    parser.args = args
    mocker.patch.object(parser, 'error', side_effect=Exception('--continue requires --output to be specified'))
    with pytest.raises(Exception) as excinfo:
        parser._process_download_options()
    assert str(excinfo.value) == '--continue requires --output to be specified'

def test_process_download_options_valid(parser):
    args = MockArgs(download=True, download_resume=True, output_file='output.txt')
    parser.args = args
    parser._process_download_options()
    assert parser.args.download is True
    assert parser.args.download_resume is True
    assert parser.args.output_file == 'output.txt'
