# file: lib/ansible/plugins/filter/urls.py:20-23
# asked: {"lines": [20, 21, 22, 23], "branches": [[21, 22], [21, 23]]}
# gained: {"lines": [20, 21, 22], "branches": [[21, 22]]}

import pytest
from ansible.plugins.filter.urls import unicode_urldecode
from ansible.module_utils.six import PY3

@pytest.mark.parametrize("input_string, expected_output", [
    ("hello%20world", "hello world"),
    ("a%2Bb%3Dc", "a+b=c"),
])
def test_unicode_urldecode_py3(input_string, expected_output, monkeypatch):
    if PY3:
        assert unicode_urldecode(input_string) == expected_output

@pytest.mark.parametrize("input_string, expected_output", [
    ("hello%20world", "hello world"),
    ("a%2Bb%3Dc", "a+b=c"),
])
def test_unicode_urldecode_py2(input_string, expected_output, monkeypatch):
    if not PY3:
        assert unicode_urldecode(input_string) == expected_output
