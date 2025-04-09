# file: tornado/locale.py:75-86
# asked: {"lines": [75, 85, 86], "branches": []}
# gained: {"lines": [75, 85, 86], "branches": []}

import pytest
from tornado import locale

@pytest.fixture(autouse=True)
def reset_locale_globals(monkeypatch):
    # Save original state
    original_default_locale = locale._default_locale
    original_supported_locales = locale._supported_locales
    original_translations = locale._translations.copy()

    yield

    # Restore original state
    monkeypatch.setattr(locale, '_default_locale', original_default_locale)
    monkeypatch.setattr(locale, '_supported_locales', original_supported_locales)
    locale._translations = original_translations

def test_set_default_locale(monkeypatch):
    # Arrange
    monkeypatch.setattr(locale, '_translations', {'en': {}, 'es': {}})
    new_default_locale = 'fr'

    # Act
    locale.set_default_locale(new_default_locale)

    # Assert
    assert locale._default_locale == new_default_locale
    assert locale._supported_locales == frozenset(['en', 'es', 'fr'])
