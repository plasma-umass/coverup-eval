# file: lib/ansible/plugins/filter/core.py:113-124
# asked: {"lines": [113, 116, 118, 119, 120, 121, 122, 123, 124], "branches": [[119, 120], [119, 121], [121, 122], [121, 123]]}
# gained: {"lines": [113, 116, 118, 119, 120, 121, 122, 123, 124], "branches": [[119, 120], [119, 121], [121, 122], [121, 123]]}

import pytest
from ansible.plugins.filter.core import regex_replace

def test_regex_replace_no_flags():
    result = regex_replace(value='hello world', pattern='world', replacement='there')
    assert result == 'hello there'

def test_regex_replace_ignorecase():
    result = regex_replace(value='hello World', pattern='world', replacement='there', ignorecase=True)
    assert result == 'hello there'

def test_regex_replace_multiline():
    result = regex_replace(value='hello\nworld', pattern='^world$', replacement='there', multiline=True)
    assert result == 'hello\nthere'

def test_regex_replace_ignorecase_multiline():
    result = regex_replace(value='hello\nWorld', pattern='^world$', replacement='there', ignorecase=True, multiline=True)
    assert result == 'hello\nthere'
