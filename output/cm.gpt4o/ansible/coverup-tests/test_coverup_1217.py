# file lib/ansible/plugins/filter/core.py:101-105
# lines [103, 104, 105]
# branches ['103->104', '103->105']

import pytest
from ansible.plugins.filter.core import quote

def test_quote_none_input():
    result = quote(None)
    assert result == "''"  # shlex_quote of an empty string should be ''

def test_quote_empty_string():
    result = quote('')
    assert result == "''"  # shlex_quote of an empty string should be ''

def test_quote_non_empty_string():
    result = quote('test')
    assert result == "test"  # shlex_quote of 'test' should be test without quotes
