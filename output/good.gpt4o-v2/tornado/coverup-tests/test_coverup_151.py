# file: tornado/locale.py:219-221
# asked: {"lines": [219, 221], "branches": []}
# gained: {"lines": [219, 221], "branches": []}

import pytest
from tornado.locale import get_supported_locales, set_default_locale

def test_get_supported_locales(monkeypatch):
    # Backup the original _supported_locales
    from tornado.locale import _supported_locales, _default_locale

    # Mock _supported_locales
    mock_locales = frozenset(['en_US', 'es_ES'])
    monkeypatch.setattr('tornado.locale._supported_locales', mock_locales)

    # Test the function
    supported_locales = get_supported_locales()
    assert supported_locales == mock_locales

    # Restore the original _supported_locales
    monkeypatch.setattr('tornado.locale._supported_locales', _supported_locales)

    # Test with default locale
    monkeypatch.setattr('tornado.locale._supported_locales', frozenset([_default_locale]))
    supported_locales = get_supported_locales()
    assert supported_locales == frozenset([_default_locale])
