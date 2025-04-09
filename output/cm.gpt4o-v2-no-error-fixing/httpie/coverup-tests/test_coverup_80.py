# file: httpie/cli/argparser.py:428-438
# asked: {"lines": [], "branches": [[434, 436]]}
# gained: {"lines": [], "branches": [[434, 436]]}

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

def test_download_resume_without_download(parser, mocker):
    mock_args = MockArgs(download_resume=True)
    parser.args = mock_args
    mocker.patch.object(parser, 'error', side_effect=Exception('--continue only works with --download'))
    
    with pytest.raises(Exception) as excinfo:
        parser._process_download_options()
    assert str(excinfo.value) == '--continue only works with --download'

def test_download_resume_without_output_file(parser, mocker):
    mock_args = MockArgs(download=True, download_resume=True, output_file=None)
    parser.args = mock_args
    mocker.patch.object(parser, 'error', side_effect=Exception('--continue requires --output to be specified'))
    
    with pytest.raises(Exception) as excinfo:
        parser._process_download_options()
    assert str(excinfo.value) == '--continue requires --output to be specified'

def test_download_resume_with_output_file(parser):
    mock_args = MockArgs(download=True, download_resume=True, output_file='output.txt')
    parser.args = mock_args
    
    try:
        parser._process_download_options()
    except Exception:
        pytest.fail("Unexpected error raised")

def test_no_download_no_resume(parser):
    mock_args = MockArgs(download=False, download_resume=False)
    parser.args = mock_args
    
    try:
        parser._process_download_options()
    except Exception:
        pytest.fail("Unexpected error raised")
