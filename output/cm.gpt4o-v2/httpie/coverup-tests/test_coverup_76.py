# file: httpie/output/processing.py:12-13
# asked: {"lines": [12, 13], "branches": []}
# gained: {"lines": [12, 13], "branches": []}

import pytest
import re
from httpie.output.processing import is_valid_mime

MIME_RE = re.compile('^[^/]+/[^/]+$')

def test_is_valid_mime_valid():
    assert is_valid_mime('text/html')

def test_is_valid_mime_invalid():
    assert not is_valid_mime('invalid-mime')

def test_is_valid_mime_empty():
    assert not is_valid_mime('')

def test_is_valid_mime_none():
    assert not is_valid_mime(None)
