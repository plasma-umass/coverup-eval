# file: cookiecutter/repository.py:26-28
# asked: {"lines": [26, 28], "branches": []}
# gained: {"lines": [26, 28], "branches": []}

import pytest
from cookiecutter.repository import is_zip_file

def test_is_zip_file_with_zip_extension():
    assert is_zip_file("example.zip") == True

def test_is_zip_file_with_uppercase_zip_extension():
    assert is_zip_file("example.ZIP") == True

def test_is_zip_file_with_non_zip_extension():
    assert is_zip_file("example.txt") == False

def test_is_zip_file_with_no_extension():
    assert is_zip_file("example") == False
