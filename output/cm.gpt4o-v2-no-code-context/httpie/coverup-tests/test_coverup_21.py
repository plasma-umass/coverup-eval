# file: httpie/cli/requestitems.py:105-117
# asked: {"lines": [105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116], "branches": []}
# gained: {"lines": [105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116], "branches": []}

import os
import pytest
from httpie.cli.requestitems import process_file_upload_arg, KeyValueArg, ParseError
from unittest.mock import mock_open, patch

class MockKeyValueArg(KeyValueArg):
    def __init__(self, value):
        self.value = value
        self.sep = '@'
        self.orig = value

def test_process_file_upload_arg_with_mime_type(monkeypatch):
    arg = MockKeyValueArg('file@/path/to/file.txt;type=text/plain')
    mock_file = mock_open(read_data='data')
    
    with patch('builtins.open', mock_file):
        with patch('os.path.expanduser', return_value='/path/to/file.txt'):
            result = process_file_upload_arg(arg)
    
    assert result[0] == 'file.txt'
    assert result[1].read() == 'data'
    assert result[2] == 'text/plain'
    result[1].close()

def test_process_file_upload_arg_without_mime_type(monkeypatch):
    arg = MockKeyValueArg('file@/path/to/file.txt')
    mock_file = mock_open(read_data='data')
    
    with patch('builtins.open', mock_file):
        with patch('os.path.expanduser', return_value='/path/to/file.txt'):
            with patch('httpie.cli.requestitems.get_content_type', return_value='text/plain'):
                result = process_file_upload_arg(arg)
    
    assert result[0] == 'file.txt'
    assert result[1].read() == 'data'
    assert result[2] == 'text/plain'
    result[1].close()

def test_process_file_upload_arg_file_not_found(monkeypatch):
    arg = MockKeyValueArg('file@/path/to/nonexistent.txt')
    
    with patch('os.path.expanduser', return_value='/path/to/nonexistent.txt'):
        with pytest.raises(ParseError) as excinfo:
            process_file_upload_arg(arg)
    
    assert 'file@/path/to/nonexistent.txt' in str(excinfo.value)
