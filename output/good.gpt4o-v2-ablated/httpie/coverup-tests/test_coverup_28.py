# file: httpie/client.py:176-178
# asked: {"lines": [176, 177, 178], "branches": []}
# gained: {"lines": [176, 177, 178], "branches": []}

import sys
import pytest
from unittest.mock import patch
from httpie.client import dump_request

def test_dump_request(monkeypatch):
    # Mock sys.stderr to capture the output
    mock_stderr = patch('sys.stderr.write')
    mock_write = mock_stderr.start()

    # Sample input for the function
    kwargs = {'method': 'GET', 'url': 'http://example.com'}

    # Call the function
    dump_request(kwargs)

    # Verify the output
    mock_write.assert_called_once_with(
        "\n>>> requests.request(**{'method': 'GET', 'url': 'http://example.com'})\n\n"
    )

    # Clean up
    mock_stderr.stop()
