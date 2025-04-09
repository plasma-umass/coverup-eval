# file: lib/ansible/plugins/filter/core.py:127-137
# asked: {"lines": [127, 130, 132, 133, 134, 135, 136, 137], "branches": [[133, 134], [133, 135], [135, 136], [135, 137]]}
# gained: {"lines": [127, 130, 132, 133, 134, 135, 136, 137], "branches": [[133, 134], [133, 135], [135, 136], [135, 137]]}

import pytest
import re
from ansible.plugins.filter.core import regex_findall

def test_regex_findall_no_flags():
    result = regex_findall("hello world", r"\w+")
    assert result == ["hello", "world"]

def test_regex_findall_ignorecase():
    result = regex_findall("Hello World", r"hello", ignorecase=True)
    assert result == ["Hello"]

def test_regex_findall_multiline():
    result = regex_findall("hello\nworld", r"^world$", multiline=True)
    assert result == ["world"]

def test_regex_findall_ignorecase_and_multiline():
    result = regex_findall("Hello\nWorld", r"^world$", ignorecase=True, multiline=True)
    assert result == ["World"]
