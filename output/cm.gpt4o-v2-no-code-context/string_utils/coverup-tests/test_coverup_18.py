# file: string_utils/validation.py:177-201
# asked: {"lines": [177, 193, 194, 196, 198, 199, 201], "branches": [[193, 194], [193, 196], [198, 199], [198, 201]]}
# gained: {"lines": [177, 193, 194, 196, 198, 199, 201], "branches": [[193, 194], [193, 196], [198, 199], [198, 201]]}

import pytest
from string_utils.validation import is_url

def test_is_url_valid_http():
    assert is_url('http://www.mysite.com') is True

def test_is_url_valid_https():
    assert is_url('https://mysite.com') is True

def test_is_url_invalid():
    assert is_url('.mysite.com') is False

def test_is_url_invalid_scheme():
    assert is_url('ftp://mysite.com', allowed_schemes=['http', 'https']) is False

def test_is_url_valid_with_allowed_schemes():
    assert is_url('http://mysite.com', allowed_schemes=['http', 'https']) is True

def test_is_url_invalid_with_allowed_schemes():
    assert is_url('ftp://mysite.com', allowed_schemes=['http', 'https']) is False

def test_is_url_no_scheme():
    assert is_url('mysite.com') is False

def test_is_url_empty_string():
    assert is_url('') is False

def test_is_url_none_input():
    assert is_url(None) is False

def test_is_url_non_string_input():
    assert is_url(12345) is False
