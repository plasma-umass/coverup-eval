# file: tornado/locale.py:75-86
# asked: {"lines": [75, 85, 86], "branches": []}
# gained: {"lines": [75, 85, 86], "branches": []}

import pytest

# Assuming _default_locale and _supported_locales are part of the module's global state
# and _translations is a dictionary also in the module's global state.
from tornado import locale

@pytest.fixture(autouse=True)
def cleanup_globals(monkeypatch):
    # Backup the original globals
    original_default_locale = locale._default_locale
    original_supported_locales = locale._supported_locales
    original_translations = locale._translations

    yield

    # Restore the original globals
    monkeypatch.setattr(locale, '_default_locale', original_default_locale)
    monkeypatch.setattr(locale, '_supported_locales', original_supported_locales)
    monkeypatch.setattr(locale, '_translations', original_translations)

def test_set_default_locale(monkeypatch):
    # Setup initial state
    monkeypatch.setattr(locale, '_translations', {'en': 'English', 'es': 'Spanish'})
    monkeypatch.setattr(locale, '_default_locale', 'en')
    monkeypatch.setattr(locale, '_supported_locales', frozenset(['en', 'es']))

    # Call the function
    locale.set_default_locale('fr')

    # Assertions
    assert locale._default_locale == 'fr'
    assert locale._supported_locales == frozenset(['en', 'es', 'fr'])
