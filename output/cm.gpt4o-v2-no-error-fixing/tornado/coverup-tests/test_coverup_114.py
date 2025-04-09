# file: tornado/locale.py:219-221
# asked: {"lines": [219, 221], "branches": []}
# gained: {"lines": [219, 221], "branches": []}

import pytest
from tornado.locale import get_supported_locales

def test_get_supported_locales(monkeypatch):
    # Mock the _supported_locales to ensure the test is isolated
    mock_supported_locales = frozenset(["en_US", "es_ES"])
    monkeypatch.setattr("tornado.locale._supported_locales", mock_supported_locales)

    # Call the function and check the result
    result = get_supported_locales()
    assert result == mock_supported_locales

    # Clean up is handled by monkeypatch

