# file: lib/ansible/plugins/filter/urls.py:31-39
# asked: {"lines": [31, 32, 33, 34, 36, 37, 38, 39], "branches": [[33, 34], [33, 36], [37, 38], [37, 39]]}
# gained: {"lines": [31, 32, 33, 34, 36, 37, 38], "branches": [[33, 34], [33, 36], [37, 38]]}

import pytest
from ansible.plugins.filter.urls import unicode_urlencode
from ansible.module_utils.six import PY3

def test_unicode_urlencode_quote():
    # Test with for_qs=False (default)
    result = unicode_urlencode('test/string')
    if PY3:
        assert result == 'test/string'
    else:
        assert result == 'test%2Fstring'

def test_unicode_urlencode_quote_plus():
    # Test with for_qs=True
    result = unicode_urlencode('test string', for_qs=True)
    if PY3:
        assert result == 'test+string'
    else:
        assert result == 'test%20string'

def test_unicode_urlencode_non_ascii():
    # Test with non-ASCII characters
    result = unicode_urlencode('tëst/strïng')
    if PY3:
        assert result == 't%C3%ABst/str%C3%AFng'
    else:
        assert result == 't%C3%ABst%2Fstr%C3%AFng'

def test_unicode_urlencode_non_ascii_for_qs():
    # Test with non-ASCII characters and for_qs=True
    result = unicode_urlencode('tëst strïng', for_qs=True)
    if PY3:
        assert result == 't%C3%ABst+str%C3%AFng'
    else:
        assert result == 't%C3%ABst%20str%C3%AFng'
