# file flutils/txtutils.py:25-56
# lines [25, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 55, 56]
# branches ['44->45', '44->47', '50->51', '50->56', '51->50', '51->52', '52->53', '52->55']

import pytest
from flutils.txtutils import len_without_ansi

def test_len_without_ansi():
    # Test with a string containing ANSI codes
    text_with_ansi = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text_with_ansi) == 6

    # Test with a list of strings containing ANSI codes
    list_with_ansi = ['\x1b[38;5;209mfoo\x1b[0m', '\x1b[38;5;209mbar\x1b[0m']
    assert len_without_ansi(list_with_ansi) == 6

    # Test with a tuple of strings containing ANSI codes
    tuple_with_ansi = ('\x1b[38;5;209mfoo\x1b[0m', '\x1b[38;5;209mbar\x1b[0m')
    assert len_without_ansi(tuple_with_ansi) == 6

    # Test with a string without ANSI codes
    text_without_ansi = 'foobar'
    assert len_without_ansi(text_without_ansi) == 6

    # Test with an empty string
    empty_string = ''
    assert len_without_ansi(empty_string) == 0

    # Test with an empty list
    empty_list = []
    assert len_without_ansi(empty_list) == 0

    # Test with an empty tuple
    empty_tuple = ()
    assert len_without_ansi(empty_tuple) == 0

    # Test with a list of strings without ANSI codes
    list_without_ansi = ['foo', 'bar']
    assert len_without_ansi(list_without_ansi) == 6

    # Test with a tuple of strings without ANSI codes
    tuple_without_ansi = ('foo', 'bar')
    assert len_without_ansi(tuple_without_ansi) == 6
