# file: cookiecutter/repository.py:26-28
# asked: {"lines": [26, 28], "branches": []}
# gained: {"lines": [26, 28], "branches": []}

import pytest

from cookiecutter.repository import is_zip_file

def test_is_zip_file_with_zip_extension():
    assert is_zip_file('example.zip') is True

def test_is_zip_file_with_uppercase_zip_extension():
    assert is_zip_file('example.ZIP') is True

def test_is_zip_file_with_mixedcase_zip_extension():
    assert is_zip_file('example.ZiP') is True

def test_is_zip_file_without_zip_extension():
    assert is_zip_file('example.txt') is False

def test_is_zip_file_with_no_extension():
    assert is_zip_file('example') is False

def test_is_zip_file_with_empty_string():
    assert is_zip_file('') is False
