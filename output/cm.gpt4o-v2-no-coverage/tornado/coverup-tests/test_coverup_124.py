# file: tornado/locale.py:219-221
# asked: {"lines": [219, 221], "branches": []}
# gained: {"lines": [219, 221], "branches": []}

import pytest
from unittest import mock
from tornado.locale import get_supported_locales

@pytest.fixture
def mock_supported_locales(monkeypatch):
    mock_locales = frozenset(["en_US", "es_ES", "fr_FR"])
    monkeypatch.setattr("tornado.locale._supported_locales", mock_locales)
    return mock_locales

def test_get_supported_locales(mock_supported_locales):
    result = get_supported_locales()
    assert result == mock_supported_locales
