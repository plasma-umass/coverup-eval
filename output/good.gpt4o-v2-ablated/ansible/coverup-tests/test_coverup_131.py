# file: lib/ansible/plugins/filter/core.py:127-137
# asked: {"lines": [127, 130, 132, 133, 134, 135, 136, 137], "branches": [[133, 134], [133, 135], [135, 136], [135, 137]]}
# gained: {"lines": [127, 130, 132, 133, 134, 135, 136, 137], "branches": [[133, 134], [133, 135], [135, 136], [135, 137]]}

import pytest
import re
from ansible.plugins.filter.core import regex_findall
from ansible.module_utils._text import to_text

def test_regex_findall_basic():
    value = "hello world"
    regex = r"\w+"
    result = regex_findall(value, regex)
    assert result == ["hello", "world"]

def test_regex_findall_multiline(monkeypatch):
    value = "hello\nworld"
    regex = r"^world"
    result = regex_findall(value, regex, multiline=True)
    assert result == ["world"]

def test_regex_findall_ignorecase(monkeypatch):
    value = "Hello World"
    regex = r"hello"
    result = regex_findall(value, regex, ignorecase=True)
    assert result == ["Hello"]

def test_regex_findall_multiline_ignorecase(monkeypatch):
    value = "Hello\nworld"
    regex = r"^world"
    result = regex_findall(value, regex, multiline=True, ignorecase=True)
    assert result == ["world"]

def test_regex_findall_no_match():
    value = "hello world"
    regex = r"\d+"
    result = regex_findall(value, regex)
    assert result == []

def test_regex_findall_nonstring():
    value = 12345
    regex = r"\d"
    result = regex_findall(value, regex)
    assert result == ["1", "2", "3", "4", "5"]
