# file: lib/ansible/plugins/filter/core.py:113-124
# asked: {"lines": [120, 122], "branches": [[119, 120], [121, 122]]}
# gained: {"lines": [120, 122], "branches": [[119, 120], [121, 122]]}

import re
import pytest
from ansible.plugins.filter.core import regex_replace

def test_regex_replace_ignorecase(monkeypatch):
    # Test case where ignorecase is True
    result = regex_replace(value='Hello World', pattern='hello', replacement='Hi', ignorecase=True)
    assert result == 'Hi World'

def test_regex_replace_multiline(monkeypatch):
    # Test case where multiline is True
    value = 'Hello\nWorld'
    pattern = '^Hello'
    replacement = 'Hi'
    result = regex_replace(value=value, pattern=pattern, replacement=replacement, multiline=True)
    assert result == 'Hi\nWorld'

def test_regex_replace_ignorecase_and_multiline(monkeypatch):
    # Test case where both ignorecase and multiline are True
    value = 'Hello\nworld'
    pattern = '^hello'
    replacement = 'Hi'
    result = regex_replace(value=value, pattern=pattern, replacement=replacement, ignorecase=True, multiline=True)
    assert result == 'Hi\nworld'
