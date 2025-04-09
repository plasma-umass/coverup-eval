# file: string_utils/validation.py:177-201
# asked: {"lines": [193, 194, 196, 198, 199, 201], "branches": [[193, 194], [193, 196], [198, 199], [198, 201]]}
# gained: {"lines": [193, 194, 196, 198, 199, 201], "branches": [[193, 194], [193, 196], [198, 199], [198, 201]]}

import pytest
from string_utils.validation import is_url
from string_utils._regex import URL_RE

def test_is_url_valid_http():
    assert is_url('http://www.mysite.com') == True

def test_is_url_valid_https():
    assert is_url('https://mysite.com') == True

def test_is_url_invalid():
    assert is_url('.mysite.com') == False

def test_is_url_invalid_scheme():
    assert is_url('ftp://mysite.com', allowed_schemes=['http', 'https']) == False

def test_is_url_valid_with_allowed_schemes():
    assert is_url('http://mysite.com', allowed_schemes=['http', 'https']) == True

def test_is_url_invalid_with_allowed_schemes():
    assert is_url('ftp://mysite.com', allowed_schemes=['http', 'https']) == False

def test_is_url_empty_string():
    assert is_url('') == False

def test_is_url_none():
    assert is_url(None) == False

def test_is_url_spaces():
    assert is_url('   ') == False
