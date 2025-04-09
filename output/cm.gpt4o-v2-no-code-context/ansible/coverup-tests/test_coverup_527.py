# file: lib/ansible/plugins/filter/core.py:101-105
# asked: {"lines": [101, 103, 104, 105], "branches": [[103, 104], [103, 105]]}
# gained: {"lines": [101, 103, 104, 105], "branches": [[103, 104], [103, 105]]}

import pytest
from ansible.plugins.filter.core import quote
from ansible.module_utils._text import to_text
from shlex import quote as shlex_quote

def test_quote_with_none():
    result = quote(None)
    assert result == shlex_quote(to_text(''))

def test_quote_with_empty_string():
    result = quote('')
    assert result == shlex_quote(to_text(''))

def test_quote_with_string():
    result = quote('test')
    assert result == shlex_quote(to_text('test'))

def test_quote_with_special_characters():
    result = quote('test with spaces')
    assert result == shlex_quote(to_text('test with spaces'))
