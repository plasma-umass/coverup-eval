# file: tornado/locale.py:251-267
# asked: {"lines": [257, 258, 259, 260, 261, 262, 263, 265, 266, 267], "branches": [[257, 258], [257, 267], [260, 261], [260, 262], [262, 263], [262, 265]]}
# gained: {"lines": [257, 258, 259, 260, 262, 263, 265, 266, 267], "branches": [[257, 258], [257, 267], [260, 262], [262, 263], [262, 265]]}

import pytest
from unittest import mock
from tornado.locale import Locale, CSVLocale, GettextLocale

@pytest.fixture
def setup_locale_cache(monkeypatch):
    # Setup the _cache and _supported_locales
    cache = {}
    supported_locales = {'en': True, 'es': True}
    translations = {'en': mock.Mock(), 'es': mock.Mock()}
    use_gettext = False

    monkeypatch.setattr(Locale, '_cache', cache)
    monkeypatch.setattr('tornado.locale._supported_locales', supported_locales)
    monkeypatch.setattr('tornado.locale._translations', translations)
    monkeypatch.setattr('tornado.locale._use_gettext', use_gettext)

    yield

    # Cleanup
    cache.clear()

def test_get_locale_not_in_cache_no_translations(setup_locale_cache):
    # Test when locale is not in cache and no translations are available
    with mock.patch('tornado.locale._translations', {'fr': None}):
        with pytest.raises(AssertionError):
            Locale.get('fr')

def test_get_locale_not_in_cache_with_translations(setup_locale_cache):
    # Test when locale is not in cache and translations are available
    locale = Locale.get('en')
    assert isinstance(locale, CSVLocale)
    assert locale.code == 'en'

def test_get_locale_not_in_cache_with_gettext(setup_locale_cache, monkeypatch):
    # Test when locale is not in cache and _use_gettext is True
    mock_translations = mock.Mock()
    monkeypatch.setattr('tornado.locale._translations', {'en': mock_translations})
    monkeypatch.setattr('tornado.locale._use_gettext', True)
    locale = Locale.get('en')
    assert isinstance(locale, GettextLocale)
    assert locale.code == 'en'

def test_get_locale_in_cache(setup_locale_cache):
    # Test when locale is already in cache
    locale = CSVLocale('es', mock.Mock())
    Locale._cache['es'] = locale
    cached_locale = Locale.get('es')
    assert cached_locale is locale
    assert cached_locale.code == 'es'
