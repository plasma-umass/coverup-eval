# file tornado/locale.py:75-86
# lines [75, 85, 86]
# branches []

import pytest
from tornado.locale import set_default_locale, get_supported_locales, _translations

@pytest.fixture
def reset_locales():
    # Backup original state
    original_default_locale = get_supported_locales()
    original_translations = _translations.copy()

    yield

    # Restore original state
    set_default_locale(original_default_locale)
    _translations.clear()
    _translations.update(original_translations)

def test_set_default_locale(reset_locales):
    # Setup
    _translations['en_US'] = 'English (US)'
    _translations['es_ES'] = 'Spanish (Spain)'

    # Test setting a new default locale
    set_default_locale('fr_FR')
    supported_locales = get_supported_locales()
    assert 'fr_FR' in supported_locales
    assert 'en_US' in supported_locales
    assert 'es_ES' in supported_locales
