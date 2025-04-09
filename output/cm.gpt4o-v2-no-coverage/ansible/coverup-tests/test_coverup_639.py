# file: lib/ansible/plugins/filter/urls.py:20-23
# asked: {"lines": [20, 21, 22, 23], "branches": [[21, 22], [21, 23]]}
# gained: {"lines": [20, 21, 22], "branches": [[21, 22]]}

import pytest
from ansible.plugins.filter.urls import unicode_urldecode
from ansible.module_utils.six import PY3
from ansible.module_utils.six.moves.urllib.parse import unquote_plus
from ansible.module_utils._text import to_bytes, to_text

@pytest.mark.parametrize("input_str, expected_output", [
    ("hello%20world", "hello world"),
    ("a%2Bb%3Dc", "a+b=c"),
    ("", ""),
])
def test_unicode_urldecode_py3(input_str, expected_output, monkeypatch):
    monkeypatch.setattr("ansible.module_utils.six.PY3", True)
    assert unicode_urldecode(input_str) == expected_output

@pytest.mark.parametrize("input_str, expected_output", [
    ("hello%20world", "hello world"),
    ("a%2Bb%3Dc", "a+b=c"),
    ("", ""),
])
def test_unicode_urldecode_py2(input_str, expected_output, monkeypatch):
    monkeypatch.setattr("ansible.module_utils.six.PY3", False)
    assert unicode_urldecode(input_str) == expected_output
