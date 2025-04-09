# file: lib/ansible/plugins/filter/core.py:101-105
# asked: {"lines": [101, 103, 104, 105], "branches": [[103, 104], [103, 105]]}
# gained: {"lines": [101, 103, 104, 105], "branches": [[103, 104], [103, 105]]}

import pytest
from ansible.plugins.filter.core import quote
from ansible.module_utils.six.moves import shlex_quote
from ansible.module_utils._text import to_text

def test_quote_with_none():
    result = quote(None)
    expected = shlex_quote(to_text(''))
    assert result == expected

def test_quote_with_string():
    test_string = "test"
    result = quote(test_string)
    expected = shlex_quote(to_text(test_string))
    assert result == expected

def test_quote_with_special_characters():
    test_string = "test with spaces and $pecial characters!"
    result = quote(test_string)
    expected = shlex_quote(to_text(test_string))
    assert result == expected
