# file: httpie/cli/requestitems.py:105-117
# asked: {"lines": [105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116], "branches": []}
# gained: {"lines": [105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116], "branches": []}

import os
import pytest
from httpie.cli.argtypes import KeyValueArg
from httpie.cli.requestitems import process_file_upload_arg
from httpie.cli.exceptions import ParseError
from httpie.cli.constants import SEPARATOR_FILE_UPLOAD_TYPE
from httpie.utils import get_content_type

def test_process_file_upload_arg_success(monkeypatch):
    # Setup
    test_file_path = '/tmp/testfile.txt'
    test_file_content = b'Test content'
    with open(test_file_path, 'wb') as f:
        f.write(test_file_content)
    
    arg = KeyValueArg(key='file', value=f'{test_file_path}{SEPARATOR_FILE_UPLOAD_TYPE}text/plain', sep='=', orig=f'file={test_file_path}{SEPARATOR_FILE_UPLOAD_TYPE}text/plain')

    # Exercise
    result = process_file_upload_arg(arg)

    # Verify
    assert result[0] == 'testfile.txt'
    assert result[1].read() == test_file_content
    assert result[2] == 'text/plain'

    # Cleanup
    result[1].close()
    os.remove(test_file_path)

def test_process_file_upload_arg_no_mime_type(monkeypatch):
    # Setup
    test_file_path = '/tmp/testfile.txt'
    test_file_content = b'Test content'
    with open(test_file_path, 'wb') as f:
        f.write(test_file_content)
    
    arg = KeyValueArg(key='file', value=test_file_path, sep='=', orig=f'file={test_file_path}')

    # Exercise
    result = process_file_upload_arg(arg)

    # Verify
    assert result[0] == 'testfile.txt'
    assert result[1].read() == test_file_content
    assert result[2] == get_content_type(test_file_path)

    # Cleanup
    result[1].close()
    os.remove(test_file_path)

def test_process_file_upload_arg_file_not_found(monkeypatch):
    # Setup
    arg = KeyValueArg(key='file', value='/nonexistentfile.txt', sep='=', orig='file=/nonexistentfile.txt')

    # Exercise & Verify
    with pytest.raises(ParseError) as excinfo:
        process_file_upload_arg(arg)
    assert 'No such file or directory' in str(excinfo.value)
