# file: httpie/cli/requestitems.py:139-151
# asked: {"lines": [140, 141, 142, 143, 144, 145, 146, 147, 148, 150], "branches": []}
# gained: {"lines": [140, 141, 142, 143, 144, 145, 146, 147, 148, 150], "branches": []}

import os
import pytest
from httpie.cli.requestitems import load_text_file, KeyValueArg, ParseError

def test_load_text_file_success(monkeypatch):
    test_content = "test content"
    test_path = "/tmp/testfile.txt"

    with open(test_path, 'w') as f:
        f.write(test_content)

    item = KeyValueArg(key=None, value=test_path, orig=test_path, sep='=')
    result = load_text_file(item)
    assert result == test_content

    os.remove(test_path)

def test_load_text_file_io_error(monkeypatch):
    item = KeyValueArg(key=None, value="/non/existent/path.txt", orig="/non/existent/path.txt", sep='=')
    with pytest.raises(ParseError) as excinfo:
        load_text_file(item)
    assert 'No such file or directory' in str(excinfo.value)

def test_load_text_file_unicode_decode_error(monkeypatch):
    test_path = "/tmp/testfile.bin"
    with open(test_path, 'wb') as f:
        f.write(b'\x80\x81\x82')

    item = KeyValueArg(key=None, value=test_path, orig=test_path, sep='=')
    with pytest.raises(ParseError) as excinfo:
        load_text_file(item)
    assert 'not a UTF8 or ASCII-encoded text file' in str(excinfo.value)

    os.remove(test_path)
