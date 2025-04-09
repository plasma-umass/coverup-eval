# file: cookiecutter/repository.py:26-28
# asked: {"lines": [26, 28], "branches": []}
# gained: {"lines": [26, 28], "branches": []}

import pytest
from cookiecutter import repository

def test_is_zip_file_with_zip_extension():
    assert repository.is_zip_file('example.zip') is True

def test_is_zip_file_with_uppercase_zip_extension():
    assert repository.is_zip_file('example.ZIP') is True

def test_is_zip_file_with_non_zip_extension():
    assert repository.is_zip_file('example.txt') is False

def test_is_zip_file_with_no_extension():
    assert repository.is_zip_file('example') is False
