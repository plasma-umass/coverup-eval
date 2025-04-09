# file: lib/ansible/module_utils/splitter.py:215-219
# asked: {"lines": [215, 217, 218, 219], "branches": [[217, 218], [217, 219]]}
# gained: {"lines": [215, 217, 218, 219], "branches": [[217, 218], [217, 219]]}

import pytest
from ansible.module_utils.splitter import unquote

def test_unquote_no_quotes():
    assert unquote("no_quotes") == "no_quotes"

def test_unquote_single_quotes():
    assert unquote("'single_quotes'") == "single_quotes"

def test_unquote_double_quotes():
    assert unquote('"double_quotes"') == "double_quotes"

def test_unquote_mismatched_quotes():
    assert unquote("'mismatched_quotes\"") == "'mismatched_quotes\""

def test_unquote_empty_string():
    assert unquote("") == ""

def test_unquote_single_character():
    assert unquote("a") == "a"
