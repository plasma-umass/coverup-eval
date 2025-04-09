# file: cookiecutter/repository.py:26-28
# asked: {"lines": [26, 28], "branches": []}
# gained: {"lines": [26, 28], "branches": []}

import pytest

from cookiecutter.repository import is_zip_file

def test_is_zip_file_with_zip_extension():
    assert is_zip_file('test.zip') is True

def test_is_zip_file_with_uppercase_zip_extension():
    assert is_zip_file('test.ZIP') is True

def test_is_zip_file_with_non_zip_extension():
    assert is_zip_file('test.txt') is False

def test_is_zip_file_with_no_extension():
    assert is_zip_file('test') is False

def test_is_zip_file_with_mixed_case_extension():
    assert is_zip_file('test.ZiP') is True
