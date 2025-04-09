# file: httpie/cli/requestitems.py:124-125
# asked: {"lines": [124, 125], "branches": []}
# gained: {"lines": [124, 125], "branches": []}

import pytest
from httpie.cli.requestitems import process_data_embed_file_contents_arg, KeyValueArg
from unittest.mock import patch

def test_process_data_embed_file_contents_arg(monkeypatch):
    # Mock the load_text_file function to avoid actual file I/O
    def mock_load_text_file(arg):
        return "mocked file content"

    monkeypatch.setattr('httpie.cli.requestitems.load_text_file', mock_load_text_file)

    # Create a KeyValueArg instance with all required arguments
    arg = KeyValueArg(key='test', value='test.txt', sep='=', orig='test=test.txt')

    # Call the function and assert the result
    result = process_data_embed_file_contents_arg(arg)
    assert result == "mocked file content"
