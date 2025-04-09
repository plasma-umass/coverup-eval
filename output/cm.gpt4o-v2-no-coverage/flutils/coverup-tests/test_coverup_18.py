# file: flutils/txtutils.py:25-56
# asked: {"lines": [25, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 55, 56], "branches": [[44, 45], [44, 47], [50, 51], [50, 56], [51, 50], [51, 52], [52, 53], [52, 55]]}
# gained: {"lines": [25, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 55, 56], "branches": [[44, 45], [44, 47], [50, 51], [50, 56], [51, 52], [52, 53], [52, 55]]}

import pytest
from flutils.txtutils import len_without_ansi
import re

_ANSI_RE = re.compile('(\x1b\\[[0-9;:]+[ABCDEFGHJKSTfhilmns])')

def test_len_without_ansi_string():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6

def test_len_without_ansi_list():
    text_list = ['\x1b[38;5;209mfoo\x1b[0m', 'bar']
    assert len_without_ansi(text_list) == 6

def test_len_without_ansi_empty_string():
    text = ''
    assert len_without_ansi(text) == 0

def test_len_without_ansi_no_ansi():
    text = 'foobar'
    assert len_without_ansi(text) == 6

def test_len_without_ansi_mixed():
    text_list = ['\x1b[38;5;209mfoo\x1b[0m', 'bar', '\x1b[38;5;209mbaz\x1b[0m']
    assert len_without_ansi(text_list) == 9
