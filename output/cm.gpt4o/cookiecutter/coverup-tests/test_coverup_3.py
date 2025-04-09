# file cookiecutter/repository.py:26-28
# lines [26, 28]
# branches []

import pytest
from unittest import mock

# Assuming the function is_zip_file is imported from cookiecutter.repository
from cookiecutter.repository import is_zip_file

def test_is_zip_file():
    # Test cases for is_zip_file function
    assert is_zip_file('example.zip') == True
    assert is_zip_file('example.ZIP') == True
    assert is_zip_file('example.Zip') == True
    assert is_zip_file('example.txt') == False
    assert is_zip_file('example.zip.txt') == False
    assert is_zip_file('example') == False
    assert is_zip_file('') == False
