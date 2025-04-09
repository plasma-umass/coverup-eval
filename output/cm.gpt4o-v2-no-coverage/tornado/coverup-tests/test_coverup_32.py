# file: tornado/locale.py:251-267
# asked: {"lines": [251, 252, 257, 258, 259, 260, 261, 262, 263, 265, 266, 267], "branches": [[257, 258], [257, 267], [260, 261], [260, 262], [262, 263], [262, 265]]}
# gained: {"lines": [251, 252, 257, 258, 259, 260, 261, 262, 263, 265, 266, 267], "branches": [[257, 258], [257, 267], [260, 261], [260, 262], [262, 263], [262, 265]]}

import pytest
from unittest.mock import patch
import gettext
from tornado.locale import Locale, CSVLocale, GettextLocale

class TestLocale:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.original_cache = Locale._cache
        Locale._cache = {}
        yield
        Locale._cache = self.original_cache

    def test_get_locale_cached(self):
        locale_code = 'en'
        locale_instance = CSVLocale(locale_code, {})
        Locale._cache[locale_code] = locale_instance

        result = Locale.get(locale_code)
        assert result is locale_instance

    def test_get_locale_not_supported(self):
        with pytest.raises(AssertionError):
            Locale.get('unsupported_code')

    def test_get_locale_no_translations(self, monkeypatch):
        locale_code = 'en'
        monkeypatch.setattr('tornado.locale._supported_locales', {locale_code})
        monkeypatch.setattr('tornado.locale._translations', {})

        result = Locale.get(locale_code)
        assert isinstance(result, CSVLocale)
        assert result.translations == {}

    def test_get_locale_with_translations_csv(self, monkeypatch):
        locale_code = 'en'
        translations = {'hello': 'world'}
        monkeypatch.setattr('tornado.locale._supported_locales', {locale_code})
        monkeypatch.setattr('tornado.locale._translations', {locale_code: translations})
        monkeypatch.setattr('tornado.locale._use_gettext', False)

        result = Locale.get(locale_code)
        assert isinstance(result, CSVLocale)
        assert result.translations == translations

    def test_get_locale_with_translations_gettext(self, monkeypatch):
        locale_code = 'en'
        translations = gettext.NullTranslations()
        monkeypatch.setattr('tornado.locale._supported_locales', {locale_code})
        monkeypatch.setattr('tornado.locale._translations', {locale_code: translations})
        monkeypatch.setattr('tornado.locale._use_gettext', True)

        result = Locale.get(locale_code)
        assert isinstance(result, GettextLocale)
        assert result.gettext == translations.gettext
