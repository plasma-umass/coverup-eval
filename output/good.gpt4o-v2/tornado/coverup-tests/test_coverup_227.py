# file: tornado/locale.py:251-267
# asked: {"lines": [257, 258, 259, 260, 261, 262, 263, 265, 266, 267], "branches": [[257, 258], [257, 267], [260, 261], [260, 262], [262, 263], [262, 265]]}
# gained: {"lines": [257, 258, 259, 260, 261, 262, 263, 265, 266, 267], "branches": [[257, 258], [260, 261], [260, 262], [262, 263], [262, 265]]}

import pytest
from unittest.mock import patch
from tornado.locale import Locale, CSVLocale, GettextLocale, _translations, _use_gettext

@pytest.fixture
def setup_locale_cache():
    Locale._cache = {}
    yield
    Locale._cache = {}

@pytest.fixture
def setup_supported_locales(monkeypatch):
    supported_locales = {'en', 'fr', 'es'}
    monkeypatch.setattr('tornado.locale._supported_locales', supported_locales)
    yield
    monkeypatch.setattr('tornado.locale._supported_locales', frozenset(['en_US']))

def test_locale_get_with_csvlocale(setup_locale_cache, setup_supported_locales):
    code = 'en'
    _translations[code] = None

    locale = Locale.get(code)
    assert isinstance(locale, CSVLocale)
    assert locale.translations == {}

def test_locale_get_with_gettextlocale(setup_locale_cache, setup_supported_locales, monkeypatch):
    code = 'fr'
    mock_translations = patch('gettext.NullTranslations').start()
    _translations[code] = mock_translations
    monkeypatch.setattr('tornado.locale._use_gettext', True)

    locale = Locale.get(code)
    assert isinstance(locale, GettextLocale)
    assert locale.ngettext == mock_translations.ngettext
    assert locale.gettext == mock_translations.gettext

    patch.stopall()

def test_locale_get_with_csvlocale_translations(setup_locale_cache, setup_supported_locales):
    code = 'es'
    _translations[code] = {'hello': 'hola'}

    locale = Locale.get(code)
    assert isinstance(locale, CSVLocale)
    assert locale.translations == {'hello': 'hola'}
