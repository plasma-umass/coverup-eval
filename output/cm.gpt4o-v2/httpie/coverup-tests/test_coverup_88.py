# file: httpie/cli/requestitems.py:124-125
# asked: {"lines": [124, 125], "branches": []}
# gained: {"lines": [124, 125], "branches": []}

import pytest
from httpie.cli.argtypes import KeyValueArg
from httpie.cli.requestitems import process_data_embed_file_contents_arg
from httpie.cli.exceptions import ParseError

def test_process_data_embed_file_contents_arg(monkeypatch):
    # Mock the open function to simulate file reading
    def mock_open(*args, **kwargs):
        class MockFile:
            def read(self):
                return b"file content"
            def __enter__(self):
                return self
            def __exit__(self, *args):
                pass
        return MockFile()
    
    monkeypatch.setattr("builtins.open", mock_open)
    
    arg = KeyValueArg(key="key", value="path/to/file", sep="=", orig="key=path/to/file")
    result = process_data_embed_file_contents_arg(arg)
    assert result == "file content"

def test_process_data_embed_file_contents_arg_ioerror(monkeypatch):
    # Mock the open function to raise an IOError
    def mock_open(*args, **kwargs):
        raise IOError("File not found")
    
    monkeypatch.setattr("builtins.open", mock_open)
    
    arg = KeyValueArg(key="key", value="path/to/file", sep="=", orig="key=path/to/file")
    with pytest.raises(ParseError) as excinfo:
        process_data_embed_file_contents_arg(arg)
    assert "File not found" in str(excinfo.value)

def test_process_data_embed_file_contents_arg_unicode_error(monkeypatch):
    # Mock the open function to simulate a UnicodeDecodeError
    def mock_open(*args, **kwargs):
        class MockFile:
            def read(self):
                raise UnicodeDecodeError("utf-8", b"", 0, 1, "reason")
            def __enter__(self):
                return self
            def __exit__(self, *args):
                pass
        return MockFile()
    
    monkeypatch.setattr("builtins.open", mock_open)
    
    arg = KeyValueArg(key="key", value="path/to/file", sep="=", orig="key=path/to/file")
    with pytest.raises(ParseError) as excinfo:
        process_data_embed_file_contents_arg(arg)
    assert "cannot embed the content" in str(excinfo.value)
