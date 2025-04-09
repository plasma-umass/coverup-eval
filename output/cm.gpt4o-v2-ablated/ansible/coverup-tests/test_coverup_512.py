# file: lib/ansible/plugins/filter/urls.py:31-39
# asked: {"lines": [39], "branches": [[37, 39]]}
# gained: {"lines": [39], "branches": [[37, 39]]}

import pytest
from ansible.plugins.filter.urls import unicode_urlencode
from ansible.module_utils._text import to_text, to_bytes
from urllib.parse import quote, quote_plus

@pytest.mark.parametrize("string, for_qs, expected", [
    ("test", False, quote("test", safe=b'/')),
    ("test", True, quote_plus("test", safe=b'')),
    ("test/test", False, quote("test/test", safe=b'/')),
    ("test/test", True, quote_plus("test/test", safe=b'')),
    ("", False, quote("", safe=b'/')),
    ("", True, quote_plus("", safe=b'')),
])
def test_unicode_urlencode(monkeypatch, string, for_qs, expected):
    # Mock PY3 to True
    monkeypatch.setattr("ansible.plugins.filter.urls.PY3", True)
    assert unicode_urlencode(string, for_qs) == expected

    # Mock PY3 to False
    monkeypatch.setattr("ansible.plugins.filter.urls.PY3", False)
    if for_qs:
        assert unicode_urlencode(string, for_qs) == to_text(quote_plus(to_bytes(string), safe=b''))
    else:
        assert unicode_urlencode(string, for_qs) == to_text(quote(to_bytes(string), safe=b'/'))
