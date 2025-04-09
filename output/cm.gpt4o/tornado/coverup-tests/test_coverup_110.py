# file tornado/locale.py:75-86
# lines [75, 85, 86]
# branches []

import pytest
from tornado import locale

def test_set_default_locale(mocker):
    # Mock the _translations dictionary
    mock_translations = mocker.patch.object(locale, '_translations', new_callable=dict)
    mock_translations.update({'en_US': {}, 'es_ES': {}})

    # Set the default locale
    locale.set_default_locale('fr_FR')

    # Verify that the default locale is set correctly
    assert locale._default_locale == 'fr_FR'

    # Verify that the supported locales include the new default locale
    expected_locales = frozenset(['en_US', 'es_ES', 'fr_FR'])
    assert locale._supported_locales == expected_locales

    # Clean up by resetting the default locale and supported locales
    locale.set_default_locale('en_US')
    assert locale._default_locale == 'en_US'
    assert locale._supported_locales == frozenset(['en_US', 'es_ES'])

