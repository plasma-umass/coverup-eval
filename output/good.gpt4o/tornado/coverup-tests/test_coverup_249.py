# file tornado/locale.py:537-581
# lines [563, 564, 565, 566, 567, 568, 570, 571, 573, 574, 576, 577, 578, 580, 581]
# branches ['563->564', '563->576', '571->573', '571->574', '578->580', '578->581']

import pytest
from tornado.locale import Locale, GettextLocale
from gettext import NullTranslations

class MockGettextLocale(GettextLocale):
    def __init__(self):
        super().__init__('en', NullTranslations())

    def ngettext(self, singular, plural, count):
        if singular.startswith("context|"):
            return singular if count == 1 else plural
        return singular if count == 1 else plural

    def gettext(self, message):
        if message.startswith("context|"):
            return message
        return message

@pytest.fixture
def mock_gettext_locale():
    return MockGettextLocale()

def test_pgettext_with_plural_message(mock_gettext_locale):
    context = "context"
    message = "singular"
    plural_message = "plural"
    count = 2

    result = mock_gettext_locale.pgettext(context, message, plural_message, count)
    assert result == plural_message

def test_pgettext_without_plural_message(mock_gettext_locale):
    context = "context"
    message = "singular"

    result = mock_gettext_locale.pgettext(context, message)
    assert result == message

def test_pgettext_plural_message_not_found(mock_gettext_locale):
    context = "context"
    message = "singular"
    plural_message = "plural"
    count = 2

    mock_gettext_locale.ngettext = lambda s, p, c: s if c == 1 else p
    result = mock_gettext_locale.pgettext(context, message, plural_message, count)
    assert result == plural_message

def test_pgettext_message_not_found(mock_gettext_locale):
    context = "context"
    message = "singular"

    mock_gettext_locale.gettext = lambda m: m
    result = mock_gettext_locale.pgettext(context, message)
    assert result == message
