# file: flutils/txtutils.py:25-56
# asked: {"lines": [25, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 55, 56], "branches": [[44, 45], [44, 47], [50, 51], [50, 56], [51, 50], [51, 52], [52, 53], [52, 55]]}
# gained: {"lines": [25, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 55, 56], "branches": [[44, 45], [44, 47], [50, 51], [50, 56], [51, 52], [52, 53], [52, 55]]}

import pytest
from flutils.txtutils import len_without_ansi

def test_len_without_ansi_with_ansi_codes():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6

def test_len_without_ansi_without_ansi_codes():
    text = 'foobar'
    assert len_without_ansi(text) == 6

def test_len_without_ansi_mixed_ansi_and_plain_text():
    text = 'foo\x1b[38;5;209mbar\x1b[0mbaz'
    assert len_without_ansi(text) == 9

def test_len_without_ansi_empty_string():
    text = ''
    assert len_without_ansi(text) == 0

def test_len_without_ansi_list_of_strings():
    text = ['foo', '\x1b[38;5;209mbar\x1b[0m', 'baz']
    assert len_without_ansi(text) == 9

def test_len_without_ansi_tuple_of_strings():
    text = ('foo', '\x1b[38;5;209mbar\x1b[0m', 'baz')
    assert len_without_ansi(text) == 9
