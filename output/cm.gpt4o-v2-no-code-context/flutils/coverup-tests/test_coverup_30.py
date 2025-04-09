# file: flutils/txtutils.py:25-56
# asked: {"lines": [25, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 55, 56], "branches": [[44, 45], [44, 47], [50, 51], [50, 56], [51, 50], [51, 52], [52, 53], [52, 55]]}
# gained: {"lines": [25, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 55, 56], "branches": [[44, 45], [44, 47], [50, 51], [50, 56], [51, 52], [52, 53], [52, 55]]}

import pytest
from flutils.txtutils import len_without_ansi

def test_len_without_ansi_with_ansi_codes():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    result = len_without_ansi(text)
    assert result == 6

def test_len_without_ansi_without_ansi_codes():
    text = 'foobar'
    result = len_without_ansi(text)
    assert result == 6

def test_len_without_ansi_mixed_list():
    seq = ['\x1b[38;5;209mfoo\x1b[0m', 'bar']
    result = len_without_ansi(seq)
    assert result == 6

def test_len_without_ansi_empty_string():
    text = ''
    result = len_without_ansi(text)
    assert result == 0

def test_len_without_ansi_empty_list():
    seq = []
    result = len_without_ansi(seq)
    assert result == 0

def test_len_without_ansi_only_ansi_codes():
    text = '\x1b[38;5;209m\x1b[0m'
    result = len_without_ansi(text)
    assert result == 0

def test_len_without_ansi_mixed_ansi_and_text():
    seq = ['\x1b[38;5;209mfoo\x1b[0m', '\x1b[38;5;209mbar\x1b[0m']
    result = len_without_ansi(seq)
    assert result == 6
