# file tornado/locale.py:518-523
# lines [518, 519, 520, 523]
# branches []

import gettext
import pytest
from tornado.locale import Locale, GettextLocale

# Assuming the existence of the following function in tornado/locale.py
# If it does not exist, it should be created accordingly.
def load_gettext_translations(directory, locale_code):
    # This function would typically load the .mo file for the given locale code
    # from the specified directory using gettext.
    pass

@pytest.fixture
def gettext_translations(mocker):
    # Mock the gettext.NullTranslations object
    mock_translations = mocker.MagicMock(spec=gettext.NullTranslations)
    mock_translations.gettext.return_value = 'translated text'
    mock_translations.ngettext.return_value = 'translated plural text'
    return mock_translations

def test_gettext_locale_initialization(gettext_translations):
    # Test the initialization of GettextLocale
    locale_code = 'en_US'
    locale = GettextLocale(locale_code, gettext_translations)

    # Assertions to verify postconditions
    assert locale.gettext('text') == 'translated text'
    assert locale.ngettext('singular', 'plural', 2) == 'translated plural text'
    assert isinstance(locale, Locale)
    assert locale.code == locale_code

    # Clean up is not necessary here as we are using a fixture with a mock object
