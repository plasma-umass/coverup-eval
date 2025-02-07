# file: lib/ansible/plugins/filter/core.py:113-124
# asked: {"lines": [113, 116, 118, 119, 120, 121, 122, 123, 124], "branches": [[119, 120], [119, 121], [121, 122], [121, 123]]}
# gained: {"lines": [113, 116, 118, 119, 120, 121, 122, 123, 124], "branches": [[119, 120], [119, 121], [121, 122], [121, 123]]}

import pytest
from ansible.plugins.filter.core import regex_replace

def test_regex_replace_no_flags():
    result = regex_replace(value='Hello World', pattern='World', replacement='Universe')
    assert result == 'Hello Universe'

def test_regex_replace_ignorecase():
    result = regex_replace(value='Hello world', pattern='WORLD', replacement='Universe', ignorecase=True)
    assert result == 'Hello Universe'

def test_regex_replace_multiline():
    value = 'Hello World\nHello Universe'
    pattern = '^Hello'
    replacement = 'Hi'
    result = regex_replace(value=value, pattern=pattern, replacement=replacement, multiline=True)
    assert result == 'Hi World\nHi Universe'

def test_regex_replace_ignorecase_and_multiline():
    value = 'hello world\nHELLO UNIVERSE'
    pattern = '^hello'
    replacement = 'hi'
    result = regex_replace(value=value, pattern=pattern, replacement=replacement, ignorecase=True, multiline=True)
    assert result == 'hi world\nhi UNIVERSE'
