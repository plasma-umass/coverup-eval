# file: httpie/cli/requestitems.py:124-125
# asked: {"lines": [124, 125], "branches": []}
# gained: {"lines": [124, 125], "branches": []}

import pytest
from httpie.cli.argtypes import KeyValueArg
from httpie.cli.requestitems import process_data_embed_file_contents_arg
from httpie.cli.exceptions import ParseError
import os

def test_process_data_embed_file_contents_arg_valid_file(monkeypatch):
    # Setup
    key_value_arg = KeyValueArg(key='test', value='testfile.txt', sep='=', orig='test=testfile.txt')
    
    # Create a temporary file
    with open('testfile.txt', 'w') as f:
        f.write('test content')

    # Test
    result = process_data_embed_file_contents_arg(key_value_arg)
    assert result == 'test content'

    # Cleanup
    os.remove('testfile.txt')

def test_process_data_embed_file_contents_arg_file_not_found(monkeypatch):
    # Setup
    key_value_arg = KeyValueArg(key='test', value='nonexistentfile.txt', sep='=', orig='test=nonexistentfile.txt')

    # Test and Assert
    with pytest.raises(ParseError) as excinfo:
        process_data_embed_file_contents_arg(key_value_arg)
    assert 'nonexistentfile.txt' in str(excinfo.value)

def test_process_data_embed_file_contents_arg_unicode_error(monkeypatch):
    # Setup
    key_value_arg = KeyValueArg(key='test', value='binaryfile.bin', sep='=', orig='test=binaryfile.bin')
    
    # Create a temporary binary file
    with open('binaryfile.bin', 'wb') as f:
        f.write(b'\x80\x81\x82')

    # Test and Assert
    with pytest.raises(ParseError) as excinfo:
        process_data_embed_file_contents_arg(key_value_arg)
    assert 'binaryfile.bin' in str(excinfo.value)

    # Cleanup
    os.remove('binaryfile.bin')
