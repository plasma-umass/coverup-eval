# file httpie/cli/argparser.py:285-296
# lines [291, 292, 296]
# branches ['291->292', '291->296']

import pytest
import argparse
from unittest import mock
from httpie.cli.argparser import HTTPieArgumentParser

class MockEnv:
    stdout = mock.Mock()
    stderr = mock.Mock()

def test_body_from_file_with_data(mocker):
    parser = HTTPieArgumentParser()
    parser.env = MockEnv()
    parser.args = mocker.Mock()
    parser.args.data = True
    parser.args.files = False

    with pytest.raises(SystemExit) as excinfo:
        parser._body_from_file(mock.Mock())
    assert excinfo.value.code == 2

def test_body_from_file_with_files(mocker):
    parser = HTTPieArgumentParser()
    parser.env = MockEnv()
    parser.args = mocker.Mock()
    parser.args.data = False
    parser.args.files = True

    with pytest.raises(SystemExit) as excinfo:
        parser._body_from_file(mock.Mock())
    assert excinfo.value.code == 2

def test_body_from_file_without_data_or_files(mocker):
    parser = HTTPieArgumentParser()
    parser.env = MockEnv()
    parser.args = mocker.Mock()
    parser.args.data = False
    parser.args.files = False

    fd_mock = mocker.Mock()
    buffer_mock = mocker.Mock()
    fd_mock.buffer = buffer_mock

    parser._body_from_file(fd_mock)
    assert parser.args.data == buffer_mock
