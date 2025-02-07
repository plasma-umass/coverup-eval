# file: httpie/cli/argparser.py:285-296
# asked: {"lines": [291, 292, 296], "branches": [[291, 292], [291, 296]]}
# gained: {"lines": [291, 292, 296], "branches": [[291, 292], [291, 296]]}

import pytest
from unittest import mock
from httpie.cli.argparser import HTTPieArgumentParser
import argparse
from httpie.context import Environment

class MockArgs:
    def __init__(self, data=None, files=None):
        self.data = data
        self.files = files

def test_body_from_file_with_data(monkeypatch):
    parser = HTTPieArgumentParser()
    parser.env = Environment()
    parser.args = MockArgs(data='some_data')

    with pytest.raises(SystemExit) as excinfo:
        parser._body_from_file(mock.Mock())
    assert excinfo.value.code == 2

def test_body_from_file_with_files(monkeypatch):
    parser = HTTPieArgumentParser()
    parser.env = Environment()
    parser.args = MockArgs(files='some_files')

    with pytest.raises(SystemExit) as excinfo:
        parser._body_from_file(mock.Mock())
    assert excinfo.value.code == 2

def test_body_from_file_without_data_or_files(monkeypatch):
    parser = HTTPieArgumentParser()
    parser.env = Environment()
    parser.args = MockArgs()

    mock_fd = mock.Mock()
    del mock_fd.buffer  # Ensure 'buffer' attribute does not exist
    parser._body_from_file(mock_fd)
    assert parser.args.data == mock_fd

def test_body_from_file_without_data_or_files_with_buffer(monkeypatch):
    parser = HTTPieArgumentParser()
    parser.env = Environment()
    parser.args = MockArgs()

    mock_fd = mock.Mock()
    mock_fd.buffer = 'buffered_data'
    parser._body_from_file(mock_fd)
    assert parser.args.data == 'buffered_data'
