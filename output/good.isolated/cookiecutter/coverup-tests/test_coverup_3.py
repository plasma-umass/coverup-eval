# file cookiecutter/repository.py:26-28
# lines [26, 28]
# branches []

import os
import pytest
from cookiecutter.repository import is_zip_file

def test_is_zip_file_true():
    assert is_zip_file('example.zip') is True

def test_is_zip_file_false():
    assert is_zip_file('example.tar.gz') is False

def test_is_zip_file_uppercase_extension():
    assert is_zip_file('EXAMPLE.ZIP') is True

def test_is_zip_file_mixed_case_extension():
    assert is_zip_file('Example.ZiP') is True
