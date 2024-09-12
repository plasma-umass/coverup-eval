# file: tornado/locale.py:537-581
# asked: {"lines": [563, 564, 565, 566, 567, 568, 570, 571, 573, 574, 576, 577, 578, 580, 581], "branches": [[563, 564], [563, 576], [571, 573], [571, 574], [578, 580], [578, 581]]}
# gained: {"lines": [563, 564, 565, 566, 567, 568, 570, 571, 573, 574, 576, 577, 578, 580, 581], "branches": [[563, 564], [563, 576], [571, 573], [571, 574], [578, 580], [578, 581]]}

import gettext
import pytest
from tornado.locale import GettextLocale

CONTEXT_SEPARATOR = "\x04"

@pytest.fixture
def gettext_locale():
    translations = gettext.NullTranslations()
    return GettextLocale("en_US", translations)

def test_pgettext_with_plural_message(gettext_locale, mocker):
    mock_ngettext = mocker.patch.object(gettext_locale, 'ngettext', return_value="clubs")
    context = "organization"
    message = "club"
    plural_message = "clubs"
    count = 2

    result = gettext_locale.pgettext(context, message, plural_message, count)

    mock_ngettext.assert_called_with(f"{context}{CONTEXT_SEPARATOR}{message}", f"{context}{CONTEXT_SEPARATOR}{plural_message}", count)
    assert result == "clubs"

def test_pgettext_with_plural_message_translation_not_found(gettext_locale, mocker):
    context = "organization"
    message = "club"
    plural_message = "clubs"
    count = 2
    mock_ngettext = mocker.patch.object(gettext_locale, 'ngettext', side_effect=[
        f"{context}{CONTEXT_SEPARATOR}{message}",
        plural_message
    ])

    result = gettext_locale.pgettext(context, message, plural_message, count)

    assert result == plural_message

def test_pgettext_without_plural_message(gettext_locale, mocker):
    mock_gettext = mocker.patch.object(gettext_locale, 'gettext', return_value="right")
    context = "law"
    message = "right"

    result = gettext_locale.pgettext(context, message)

    mock_gettext.assert_called_with(f"{context}{CONTEXT_SEPARATOR}{message}")
    assert result == "right"

def test_pgettext_without_plural_message_translation_not_found(gettext_locale, mocker):
    context = "law"
    message = "right"
    mock_gettext = mocker.patch.object(gettext_locale, 'gettext', side_effect=lambda msg: f"{context}{CONTEXT_SEPARATOR}{message}")

    result = gettext_locale.pgettext(context, message)

    assert result == message
