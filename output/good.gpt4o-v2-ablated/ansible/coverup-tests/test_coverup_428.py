# file: lib/ansible/plugins/filter/urls.py:31-39
# asked: {"lines": [32, 33, 34, 36, 37, 38, 39], "branches": [[33, 34], [33, 36], [37, 38], [37, 39]]}
# gained: {"lines": [32, 33, 34, 36, 37, 38], "branches": [[33, 34], [33, 36], [37, 38]]}

import pytest
from ansible.plugins.filter.urls import unicode_urlencode
from ansible.module_utils.six import PY3
from urllib.parse import quote, quote_plus

@pytest.mark.parametrize("string, for_qs, expected", [
    ("test", False, quote("test", b'/') if PY3 else quote("test".encode(), b'/').decode()),
    ("test", True, quote_plus("test") if PY3 else quote_plus("test".encode()).decode()),
    ("/path/to/resource", False, quote("/path/to/resource", b'/') if PY3 else quote("/path/to/resource".encode(), b'/').decode()),
    ("key=value&another_key=another_value", True, quote_plus("key=value&another_key=another_value") if PY3 else quote_plus("key=value&another_key=another_value".encode()).decode()),
])
def test_unicode_urlencode(string, for_qs, expected):
    assert unicode_urlencode(string, for_qs) == expected
