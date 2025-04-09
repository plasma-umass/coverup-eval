# file: lib/ansible/plugins/filter/core.py:140-170
# asked: {"lines": [140, 143, 145, 146, 147, 148, 149, 150, 151, 152, 154, 156, 157, 158, 159, 160, 162, 163, 164, 165, 167, 168, 169, 170], "branches": [[146, 147], [146, 156], [147, 148], [147, 150], [150, 151], [150, 154], [157, 158], [157, 159], [159, 160], [159, 162], [163, 0], [163, 164], [164, 165], [164, 167], [168, 169], [168, 170]]}
# gained: {"lines": [140, 143, 145, 146, 147, 148, 149, 150, 151, 152, 154, 156, 157, 158, 159, 160, 162, 163, 164, 165, 167, 168, 169, 170], "branches": [[146, 147], [146, 156], [147, 148], [147, 150], [150, 151], [150, 154], [157, 158], [157, 159], [159, 160], [159, 162], [163, 0], [163, 164], [164, 165], [164, 167], [168, 169], [168, 170]]}

import pytest
from ansible.errors import AnsibleFilterError
from ansible.module_utils._text import to_text
from ansible.plugins.filter.core import regex_search

def test_regex_search_no_groups():
    result = regex_search("hello world", r"world")
    assert result == "world"

def test_regex_search_with_named_group():
    result = regex_search("hello world", r"(?P<word>world)", r"\g<word>")
    assert result == ["world"]

def test_regex_search_with_numbered_group():
    result = regex_search("hello world", r"(world)", r"\1")
    assert result == ["world"]

def test_regex_search_ignorecase():
    result = regex_search("Hello World", r"world", ignorecase=True)
    assert result == "World"

def test_regex_search_multiline():
    result = regex_search("hello\nworld", r"^world", multiline=True)
    assert result == "world"

def test_regex_search_unknown_argument():
    with pytest.raises(AnsibleFilterError, match="Unknown argument"):
        regex_search("hello world", r"world", r"unknown")

def test_regex_search_no_match():
    result = regex_search("hello world", r"planet")
    assert result is None
