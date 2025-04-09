# file: httpie/client.py:176-178
# asked: {"lines": [176, 177, 178], "branches": []}
# gained: {"lines": [176, 177, 178], "branches": []}

import pytest
import sys
from io import StringIO
from httpie.client import dump_request

def test_dump_request(monkeypatch):
    # Prepare a dictionary to pass to dump_request
    kwargs = {'method': 'GET', 'url': 'http://example.com'}

    # Capture the output to stderr
    stderr = StringIO()
    monkeypatch.setattr(sys, 'stderr', stderr)

    # Call the function
    dump_request(kwargs)

    # Get the output and verify it
    output = stderr.getvalue()
    expected_output = "\n>>> requests.request(**{'method': 'GET', 'url': 'http://example.com'})\n\n"
    assert output == expected_output

    # Clean up
    stderr.close()
