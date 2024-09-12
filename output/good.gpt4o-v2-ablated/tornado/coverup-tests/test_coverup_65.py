# file: tornado/locale.py:75-86
# asked: {"lines": [75, 85, 86], "branches": []}
# gained: {"lines": [75, 85, 86], "branches": []}

import pytest
from tornado import locale

@pytest.fixture(autouse=True)
def reset_locale_globals(monkeypatch):
    # Backup the original globals
    original_default_locale = locale._default_locale
    original_supported_locales = locale._supported_locales
    original_translations = locale._translations

    # Reset the globals after each test
    yield

    locale._default_locale = original_default_locale
    locale._supported_locales = original_supported_locales
    locale._translations = original_translations

def test_set_default_locale(monkeypatch):
    # Mock the _translations dictionary
    mock_translations = {
        'en_US': 'English (US)',
        'es_ES': 'Spanish (Spain)'
    }
    monkeypatch.setattr(locale, '_translations', mock_translations)

    # Set a new default locale
    new_default_locale = 'fr_FR'
    locale.set_default_locale(new_default_locale)

    # Assertions to verify the postconditions
    assert locale._default_locale == new_default_locale
    assert locale._supported_locales == frozenset(['en_US', 'es_ES', 'fr_FR'])
