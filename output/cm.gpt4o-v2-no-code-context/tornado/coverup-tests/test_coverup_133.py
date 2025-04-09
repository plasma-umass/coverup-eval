# file: tornado/locale.py:219-221
# asked: {"lines": [219, 221], "branches": []}
# gained: {"lines": [219, 221], "branches": []}

import pytest
from tornado.locale import get_supported_locales, _supported_locales

def test_get_supported_locales(monkeypatch):
    # Mock the _supported_locales to ensure the test is isolated
    mock_locales = ['en_US', 'fr_FR', 'es_ES']
    monkeypatch.setattr('tornado.locale._supported_locales', mock_locales)
    
    # Call the function and assert the result
    result = get_supported_locales()
    assert result == mock_locales
