# file flutils/txtutils.py:25-56
# lines [25, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 55, 56]
# branches ['44->45', '44->47', '50->51', '50->56', '51->50', '51->52', '52->53', '52->55']

import pytest
from flutils.txtutils import len_without_ansi

@pytest.fixture
def ansi_string():
    return '\x1b[38;5;209mfoobar\x1b[0m'

@pytest.fixture
def non_ansi_string():
    return 'foobar'

@pytest.fixture
def mixed_ansi_string():
    return 'foo\x1b[38;5;209mbar\x1b[0m'

def test_len_without_ansi_on_ansi_string(ansi_string):
    assert len_without_ansi(ansi_string) == 6

def test_len_without_ansi_on_non_ansi_string(non_ansi_string):
    assert len_without_ansi(non_ansi_string) == 6

def test_len_without_ansi_on_mixed_ansi_string(mixed_ansi_string):
    assert len_without_ansi(mixed_ansi_string) == 6

def test_len_without_ansi_on_list_of_strings(ansi_string, non_ansi_string, mixed_ansi_string):
    strings = [ansi_string, non_ansi_string, mixed_ansi_string]
    expected_length = len(non_ansi_string) * 3  # 6 * 3 = 18
    assert len_without_ansi(strings) == expected_length

def test_len_without_ansi_on_tuple_of_strings(ansi_string, non_ansi_string, mixed_ansi_string):
    strings = (ansi_string, non_ansi_string, mixed_ansi_string)
    expected_length = len(non_ansi_string) * 3  # 6 * 3 = 18
    assert len_without_ansi(strings) == expected_length

def test_len_without_ansi_on_empty_string():
    assert len_without_ansi('') == 0

def test_len_without_ansi_on_empty_list():
    assert len_without_ansi([]) == 0

def test_len_without_ansi_on_empty_tuple():
    assert len_without_ansi(()) == 0

def test_len_without_ansi_on_list_with_empty_string():
    assert len_without_ansi(['']) == 0

def test_len_without_ansi_on_tuple_with_empty_string():
    assert len_without_ansi(('')) == 0

def test_len_without_ansi_on_string_with_only_ansi_codes():
    assert len_without_ansi('\x1b[38;5;209m\x1b[0m') == 0
