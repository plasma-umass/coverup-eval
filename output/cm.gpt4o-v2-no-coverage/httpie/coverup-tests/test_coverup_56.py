# file: httpie/cli/requestitems.py:139-151
# asked: {"lines": [139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 150], "branches": []}
# gained: {"lines": [139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 150], "branches": []}

import os
import pytest
from httpie.cli.argtypes import KeyValueArg
from httpie.cli.exceptions import ParseError
from httpie.cli.requestitems import load_text_file

def test_load_text_file_success(monkeypatch):
    # Arrange
    item = KeyValueArg(key='test', value='testfile.txt', sep='=', orig='testfile.txt')
    test_content = 'This is a test file.'

    def mock_open(path, mode='r', *args, **kwargs):
        if path == os.path.expanduser('testfile.txt'):
            return original_open('testfile.txt', mode)
        return original_open(path, mode, *args, **kwargs)

    original_open = open
    monkeypatch.setattr('builtins.open', mock_open)
    with original_open('testfile.txt', 'w') as f:
        f.write(test_content)

    # Act
    result = load_text_file(item)

    # Assert
    assert result == test_content

    # Cleanup
    os.remove('testfile.txt')

def test_load_text_file_ioerror(monkeypatch):
    # Arrange
    item = KeyValueArg(key='test', value='nonexistentfile.txt', sep='=', orig='nonexistentfile.txt')

    def mock_open(path, mode='r', *args, **kwargs):
        raise IOError("File not found")

    monkeypatch.setattr('builtins.open', mock_open)

    # Act & Assert
    with pytest.raises(ParseError) as excinfo:
        load_text_file(item)
    assert '"nonexistentfile.txt": File not found' in str(excinfo.value)

def test_load_text_file_unicode_decode_error(monkeypatch):
    # Arrange
    item = KeyValueArg(key='test', value='binaryfile.bin', sep='=', orig='binaryfile.bin')

    def mock_open(path, mode='r', *args, **kwargs):
        if path == os.path.expanduser('binaryfile.bin'):
            return original_open('binaryfile.bin', mode)
        return original_open(path, mode, *args, **kwargs)

    original_open = open
    monkeypatch.setattr('builtins.open', mock_open)
    with original_open('binaryfile.bin', 'wb') as f:
        f.write(b'\x80\x81\x82')

    # Act & Assert
    with pytest.raises(ParseError) as excinfo:
        load_text_file(item)
    assert '"binaryfile.bin": cannot embed the content of "binaryfile.bin",' in str(excinfo.value)

    # Cleanup
    os.remove('binaryfile.bin')
