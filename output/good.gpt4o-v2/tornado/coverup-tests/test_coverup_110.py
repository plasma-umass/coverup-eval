# file: tornado/locale.py:75-86
# asked: {"lines": [75, 85, 86], "branches": []}
# gained: {"lines": [75, 85, 86], "branches": []}

import pytest
from tornado.locale import set_default_locale

def test_set_default_locale(monkeypatch):
    # Arrange
    initial_default_locale = 'en_US'
    initial_supported_locales = frozenset([initial_default_locale])
    translations = {'es_ES': 'Spanish', 'fr_FR': 'French'}

    monkeypatch.setattr('tornado.locale._default_locale', initial_default_locale)
    monkeypatch.setattr('tornado.locale._supported_locales', initial_supported_locales)
    monkeypatch.setattr('tornado.locale._translations', translations)

    new_locale = 'de_DE'

    # Act
    set_default_locale(new_locale)

    # Assert
    from tornado.locale import _default_locale, _supported_locales
    assert _default_locale == new_locale
    assert _supported_locales == frozenset(list(translations.keys()) + [new_locale])
