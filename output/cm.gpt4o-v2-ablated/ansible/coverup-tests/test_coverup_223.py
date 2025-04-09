# file: lib/ansible/plugins/filter/core.py:101-105
# asked: {"lines": [101, 103, 104, 105], "branches": [[103, 104], [103, 105]]}
# gained: {"lines": [101, 103, 104, 105], "branches": [[103, 104], [103, 105]]}

import pytest
from ansible.plugins.filter.core import quote
from ansible.module_utils._text import to_text
from shlex import quote as shlex_quote

def test_quote_none():
    assert quote(None) == shlex_quote(to_text(''))

def test_quote_empty_string():
    assert quote('') == shlex_quote(to_text(''))

def test_quote_string():
    assert quote('test') == shlex_quote(to_text('test'))

def test_quote_special_chars():
    special_string = 'a&b|c;d'
    assert quote(special_string) == shlex_quote(to_text(special_string))
