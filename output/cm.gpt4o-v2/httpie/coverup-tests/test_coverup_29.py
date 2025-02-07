# file: httpie/cli/requestitems.py:139-151
# asked: {"lines": [139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 150], "branches": []}
# gained: {"lines": [139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 150], "branches": []}

import os
import pytest
from httpie.cli.argtypes import KeyValueArg
from httpie.cli.exceptions import ParseError
from httpie.cli.requestitems import load_text_file

def test_load_text_file_success(monkeypatch):
    # Setup
    test_content = "test content"
    test_path = "/tmp/testfile.txt"
    with open(test_path, "w") as f:
        f.write(test_content)
    
    item = KeyValueArg(key="test", value=test_path, sep="=", orig="test=/tmp/testfile.txt")
    
    # Exercise
    result = load_text_file(item)
    
    # Verify
    assert result == test_content
    
    # Cleanup
    os.remove(test_path)

def test_load_text_file_ioerror(monkeypatch):
    # Setup
    item = KeyValueArg(key="test", value="/non/existent/path.txt", sep="=", orig="test=/non/existent/path.txt")
    
    # Exercise and Verify
    with pytest.raises(ParseError) as excinfo:
        load_text_file(item)
    assert 'No such file or directory' in str(excinfo.value)

def test_load_text_file_unicode_decode_error(monkeypatch):
    # Setup
    test_path = "/tmp/testfile.bin"
    with open(test_path, "wb") as f:
        f.write(b'\x80\x81\x82')
    
    item = KeyValueArg(key="test", value=test_path, sep="=", orig="test=/tmp/testfile.bin")
    
    # Exercise and Verify
    with pytest.raises(ParseError) as excinfo:
        load_text_file(item)
    assert 'not a UTF8 or ASCII-encoded text file' in str(excinfo.value)
    
    # Cleanup
    os.remove(test_path)
