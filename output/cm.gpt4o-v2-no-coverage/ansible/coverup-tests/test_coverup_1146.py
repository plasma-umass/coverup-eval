# file: lib/ansible/plugins/filter/urls.py:31-39
# asked: {"lines": [32, 33, 34, 36, 37, 38, 39], "branches": [[33, 34], [33, 36], [37, 38], [37, 39]]}
# gained: {"lines": [32, 33, 34, 36, 37, 38], "branches": [[33, 34], [33, 36], [37, 38]]}

import pytest
from ansible.module_utils.six import PY3
from ansible.module_utils.six.moves.urllib.parse import quote, quote_plus
from ansible.module_utils._text import to_bytes, to_text
from ansible.plugins.filter.urls import unicode_urlencode

@pytest.mark.parametrize("input_string, for_qs, expected", [
    ("test", False, "test"),
    ("test", True, "test"),
    ("/test", False, "/test"),
    ("/test", True, "%2Ftest"),
    ("t e s t", False, "t%20e%20s%20t"),
    ("t e s t", True, "t+e+s+t"),
])
def test_unicode_urlencode(input_string, for_qs, expected):
    result = unicode_urlencode(input_string, for_qs)
    assert result == expected

def test_unicode_urlencode_py2(monkeypatch):
    monkeypatch.setattr("ansible.module_utils.six.PY3", False)
    input_string = "test"
    expected = "test"
    result = unicode_urlencode(input_string, False)
    assert result == expected

    input_string = "t e s t"
    expected = "t%20e%20s%20t"
    result = unicode_urlencode(input_string, False)
    assert result == expected

    input_string = "t e s t"
    expected = "t+e+s+t"
    result = unicode_urlencode(input_string, True)
    assert result == expected
