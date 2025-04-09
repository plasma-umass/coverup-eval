# file: flutils/txtutils.py:25-56
# asked: {"lines": [25, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 55, 56], "branches": [[44, 45], [44, 47], [50, 51], [50, 56], [51, 50], [51, 52], [52, 53], [52, 55]]}
# gained: {"lines": [25, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 55, 56], "branches": [[44, 45], [44, 47], [50, 51], [50, 56], [51, 52], [52, 53], [52, 55]]}

import pytest
import re
from typing import Sequence, cast
from itertools import chain

_ANSI_RE = re.compile(r'\x1b\[[0-9;]*m')

from flutils.txtutils import len_without_ansi

def test_len_without_ansi_with_ansi_codes():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    result = len_without_ansi(text)
    assert result == 6

def test_len_without_ansi_without_ansi_codes():
    text = 'foobar'
    result = len_without_ansi(text)
    assert result == 6

def test_len_without_ansi_with_mixed_content():
    text = 'foo\x1b[38;5;209mbar\x1b[0mbaz'
    result = len_without_ansi(text)
    assert result == 9

def test_len_without_ansi_with_empty_string():
    text = ''
    result = len_without_ansi(text)
    assert result == 0

def test_len_without_ansi_with_list_of_strings():
    text = ['foo', '\x1b[38;5;209mbar\x1b[0m', 'baz']
    result = len_without_ansi(text)
    assert result == 9

def test_len_without_ansi_with_tuple_of_strings():
    text = ('foo', '\x1b[38;5;209mbar\x1b[0m', 'baz')
    result = len_without_ansi(text)
    assert result == 9

def test_len_without_ansi_with_nested_ansi_codes():
    text = '\x1b[38;5;209mfoo\x1b[0m\x1b[38;5;209mbar\x1b[0m'
    result = len_without_ansi(text)
    assert result == 6

def test_len_without_ansi_with_only_ansi_codes():
    text = '\x1b[38;5;209m\x1b[0m'
    result = len_without_ansi(text)
    assert result == 0
