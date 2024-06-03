# file src/blib2to3/pgen2/tokenize.py:292-302
# lines [292, 295, 296, 297, 298, 299, 301, 302]
# branches ['296->297', '296->298', '298->301', '298->302']

import pytest
from blib2to3.pgen2.tokenize import _get_normal_name

def test_get_normal_name_utf8():
    assert _get_normal_name("utf-8") == "utf-8"
    assert _get_normal_name("utf-8-sig") == "utf-8"
    assert _get_normal_name("UTF_8") == "utf-8"
    assert _get_normal_name("utf_8_sig") == "utf-8"

def test_get_normal_name_latin1():
    assert _get_normal_name("latin-1") == "iso-8859-1"
    assert _get_normal_name("iso-8859-1") == "iso-8859-1"
    assert _get_normal_name("iso-latin-1") == "iso-8859-1"
    assert _get_normal_name("latin-1-something") == "iso-8859-1"
    assert _get_normal_name("iso-8859-1-something") == "iso-8859-1"
    assert _get_normal_name("iso-latin-1-something") == "iso-8859-1"

def test_get_normal_name_other():
    assert _get_normal_name("ascii") == "ascii"
    assert _get_normal_name("utf-16") == "utf-16"
    assert _get_normal_name("latin-2") == "latin-2"
    assert _get_normal_name("iso-8859-2") == "iso-8859-2"
    assert _get_normal_name("some-encoding") == "some-encoding"
