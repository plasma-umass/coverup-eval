# file: httpie/output/processing.py:12-13
# asked: {"lines": [12, 13], "branches": []}
# gained: {"lines": [12, 13], "branches": []}

import pytest
import re

# Assuming MIME_RE is defined somewhere in the module
MIME_RE = re.compile(r'^[\w\.-]+/[\w\.-]+$')

from httpie.output.processing import is_valid_mime

def test_is_valid_mime_valid(monkeypatch):
    valid_mime = "application/json"
    assert is_valid_mime(valid_mime) is not None

def test_is_valid_mime_invalid(monkeypatch):
    invalid_mime = "invalid_mime"
    assert is_valid_mime(invalid_mime) is None

def test_is_valid_mime_empty(monkeypatch):
    empty_mime = ""
    assert is_valid_mime(empty_mime) == ""

def test_is_valid_mime_none(monkeypatch):
    none_mime = None
    assert is_valid_mime(none_mime) is None
