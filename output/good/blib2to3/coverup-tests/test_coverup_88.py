# file src/blib2to3/pgen2/tokenize.py:292-302
# lines [297]
# branches ['296->297']

import pytest
from blib2to3.pgen2.tokenize import _get_normal_name

def test_get_normal_name_utf8_variant():
    # Test a variant of utf-8 that is longer than 12 characters and has underscores
    encoding = "utf_8_sig_extra"
    normalized = _get_normal_name(encoding)
    assert normalized == "utf-8", "The normalized encoding should be 'utf-8'"

def test_get_normal_name_non_utf8():
    # Test an encoding that is not a utf-8 variant and is longer than 12 characters
    encoding = "some_other_enc"
    normalized = _get_normal_name(encoding)
    assert normalized == encoding, "The normalized encoding should be the same as the original"
