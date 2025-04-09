# file: httpie/client.py:176-178
# asked: {"lines": [177, 178], "branches": []}
# gained: {"lines": [177, 178], "branches": []}

import sys
import pytest
from unittest.mock import patch
from httpie.client import dump_request

def repr_dict(d):
    return ', '.join(f'{k}={repr(v)}' for k, v in d.items())

def test_dump_request(monkeypatch):
    # Mock sys.stderr to capture the output
    mock_stderr = patch('sys.stderr.write')
    mock_write = mock_stderr.start()

    # Define the input for the function
    kwargs = {'method': 'GET', 'url': 'http://example.com'}

    # Call the function
    dump_request(kwargs)

    # Check that sys.stderr.write was called with the expected string
    expected_output = "\n>>> requests.request(**{'method': 'GET', 'url': 'http://example.com'})\n\n"
    mock_write.assert_called_once_with(expected_output)

    # Stop the patch
    mock_stderr.stop()
