# file: apimd/parser.py:62-71
# asked: {"lines": [62, 64, 66, 67, 69, 70, 71], "branches": [[64, 66], [64, 71], [66, 67], [66, 69], [69, 64], [69, 70]]}
# gained: {"lines": [62, 64, 66, 67, 69, 70, 71], "branches": [[64, 66], [64, 71], [66, 67], [66, 69], [69, 64], [69, 70]]}

import pytest
from apimd.parser import is_public_family

def test_is_public_family_with_public_name():
    assert is_public_family("public.module") == True

def test_is_public_family_with_private_name():
    assert is_public_family("private._module") == False

def test_is_public_family_with_magic_name():
    assert is_public_family("public.__magic__") == True

def test_is_public_family_with_mixed_names():
    assert is_public_family("public.__magic__.private._module") == False

def test_is_public_family_with_empty_string():
    assert is_public_family("") == True
