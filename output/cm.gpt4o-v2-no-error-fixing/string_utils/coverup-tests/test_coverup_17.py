# file: string_utils/validation.py:393-415
# asked: {"lines": [393, 407, 408, 411, 412, 413, 415], "branches": [[407, 408], [407, 411], [411, 412], [411, 415], [412, 411], [412, 413]]}
# gained: {"lines": [393, 407, 408, 411, 412, 413, 415], "branches": [[407, 408], [407, 411], [411, 412], [411, 415], [412, 411], [412, 413]]}

import pytest
from string_utils.validation import is_ip_v4

def test_is_ip_v4_valid_ip():
    assert is_ip_v4('255.200.100.75') == True

def test_is_ip_v4_invalid_string():
    assert is_ip_v4('nope') == False

def test_is_ip_v4_out_of_range():
    assert is_ip_v4('255.200.100.999') == False

def test_is_ip_v4_empty_string():
    assert is_ip_v4('') == False

def test_is_ip_v4_none():
    assert is_ip_v4(None) == False

def test_is_ip_v4_partial_ip():
    assert is_ip_v4('255.200.100') == False

def test_is_ip_v4_with_spaces():
    assert is_ip_v4(' 255.200.100.75 ') == False

def test_is_ip_v4_with_leading_zeros():
    assert is_ip_v4('001.002.003.004') == True
