# file tornado/locale.py:515-517
# lines [515, 516]
# branches []

import pytest
from tornado.locale import Locale

class GettextLocale(Locale):
    """Locale implementation using the `gettext` module."""
    
    def translate(self, message, plural_message=None, count=None):
        return message

def test_gettext_locale_initialization():
    locale = GettextLocale("en_US")
    assert isinstance(locale, GettextLocale)
