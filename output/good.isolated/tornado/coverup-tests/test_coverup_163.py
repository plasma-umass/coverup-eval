# file tornado/locale.py:515-517
# lines [515, 516]
# branches []

import pytest
from tornado.locale import GettextLocale
from gettext import NullTranslations

# Corrected test function
def test_gettext_locale_initialization(mocker):
    # Mock gettext translation object
    mock_translation = mocker.MagicMock(spec=NullTranslations)
    mocker.patch('gettext.translation', return_value=mock_translation)

    # Initialize GettextLocale with a mock domain and languages
    locale = GettextLocale('mock_domain', mock_translation)

    # Assertions to ensure GettextLocale is initialized correctly
    assert locale.gettext('hello') == mock_translation.gettext.return_value
    assert locale.ngettext('apple', 'apples', 2) == mock_translation.ngettext.return_value

    # Clean up by undoing all patches
    mocker.stopall()
