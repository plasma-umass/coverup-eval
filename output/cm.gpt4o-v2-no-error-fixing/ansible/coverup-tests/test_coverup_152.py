# file: lib/ansible/plugins/lookup/first_found.py:146-159
# asked: {"lines": [146, 149, 150, 151, 152, 153, 156, 157, 159], "branches": [[150, 151], [150, 156], [151, 152], [151, 153], [156, 157], [156, 159]]}
# gained: {"lines": [146, 149, 150, 151, 152, 153, 156, 157, 159], "branches": [[150, 151], [150, 156], [151, 152], [151, 153], [156, 157], [156, 159]]}

import pytest
from ansible.plugins.lookup.first_found import _split_on
from ansible.module_utils.six import string_types

def test_split_on_string():
    terms = "a,b,c"
    spliters = ","
    expected = ["a", "b", "c"]
    result = _split_on(terms, spliters)
    assert result == expected

def test_split_on_list_of_strings():
    terms = ["a,b", "c,d"]
    spliters = ","
    expected = ["a", "b", "c", "d"]
    result = _split_on(terms, spliters)
    assert result == expected

def test_split_on_mixed_list():
    terms = ["a,b", ["c,d", "e,f"]]
    spliters = ","
    expected = ["a", "b", "c", "d", "e", "f"]
    result = _split_on(terms, spliters)
    assert result == expected

def test_split_on_no_spliters():
    terms = "a b c"
    spliters = ","
    expected = ["a", "b", "c"]
    result = _split_on(terms, spliters)
    assert result == expected

def test_split_on_empty_string():
    terms = ""
    spliters = ","
    expected = [""]
    result = _split_on(terms, spliters)
    assert result == expected
