# file: apimd/parser.py:56-59
# asked: {"lines": [56, 58, 59], "branches": []}
# gained: {"lines": [56, 58, 59], "branches": []}

import pytest

from apimd.parser import is_magic

def test_is_magic_with_magic_name():
    assert is_magic('__init__') is True

def test_is_magic_with_non_magic_name():
    assert is_magic('init') is False

def test_is_magic_with_partial_magic_name():
    assert is_magic('__init') is False

def test_is_magic_with_dotted_name():
    assert is_magic('module.__init__') is True

def test_is_magic_with_non_magic_dotted_name():
    assert is_magic('module.init') is False

def test_is_magic_with_partial_magic_dotted_name():
    assert is_magic('module.__init') is False
