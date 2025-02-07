# file: lib/ansible/plugins/filter/core.py:101-105
# asked: {"lines": [101, 103, 104, 105], "branches": [[103, 104], [103, 105]]}
# gained: {"lines": [101, 103, 104, 105], "branches": [[103, 104], [103, 105]]}

import pytest
from ansible.module_utils.six.moves import shlex_quote
from ansible.module_utils._text import to_text
from ansible.plugins.filter.core import quote

def test_quote_with_none():
    result = quote(None)
    assert result == shlex_quote(to_text(''))

def test_quote_with_empty_string():
    result = quote('')
    assert result == shlex_quote(to_text(''))

def test_quote_with_string():
    test_str = 'test'
    result = quote(test_str)
    assert result == shlex_quote(to_text(test_str))

def test_quote_with_special_characters():
    test_str = 'special & characters'
    result = quote(test_str)
    assert result == shlex_quote(to_text(test_str))
