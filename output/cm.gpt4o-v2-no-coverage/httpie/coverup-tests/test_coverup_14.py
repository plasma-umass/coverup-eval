# file: httpie/cli/requestitems.py:105-117
# asked: {"lines": [105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116], "branches": []}
# gained: {"lines": [105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116], "branches": []}

import os
import pytest
from unittest import mock
from httpie.cli.requestitems import process_file_upload_arg
from httpie.cli.argtypes import KeyValueArg
from httpie.cli.exceptions import ParseError
from httpie.utils import get_content_type

@pytest.fixture
def mock_open():
    with mock.patch("builtins.open", mock.mock_open(read_data="data")) as m:
        yield m

@pytest.fixture
def mock_expanduser():
    with mock.patch("os.path.expanduser", return_value="/mocked/path/file.txt") as m:
        yield m

@pytest.fixture
def mock_get_content_type():
    with mock.patch("httpie.utils.get_content_type", return_value="text/plain") as m:
        yield m

def test_process_file_upload_arg_success(mock_open, mock_expanduser, mock_get_content_type):
    arg = KeyValueArg(key="file", value="/mocked/path/file.txt", sep="=", orig="file=/mocked/path/file.txt")
    result = process_file_upload_arg(arg)
    assert result == ("file.txt", mock_open.return_value, "text/plain")
    mock_open.assert_called_once_with("/mocked/path/file.txt", "rb")

def test_process_file_upload_arg_with_mime_type(mock_open, mock_expanduser):
    arg = KeyValueArg(key="file", value="/mocked/path/file.txt;type=application/json", sep="=", orig="file=/mocked/path/file.txt;type=application/json")
    result = process_file_upload_arg(arg)
    assert result == ("file.txt", mock_open.return_value, "application/json")
    mock_open.assert_called_once_with("/mocked/path/file.txt", "rb")

def test_process_file_upload_arg_file_not_found(mock_expanduser):
    with mock.patch("builtins.open", side_effect=IOError("File not found")):
        arg = KeyValueArg(key="file", value="/mocked/path/file.txt", sep="=", orig="file=/mocked/path/file.txt")
        with pytest.raises(ParseError) as excinfo:
            process_file_upload_arg(arg)
        assert str(excinfo.value) == '"file=/mocked/path/file.txt": File not found'
