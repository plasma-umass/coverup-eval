# file: tornado/locale.py:233-249
# asked: {"lines": [236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249], "branches": [[236, 237], [236, 249], [237, 238], [237, 239], [241, 242], [241, 243], [243, 244], [243, 245], [245, 246], [245, 247], [247, 236], [247, 248]]}
# gained: {"lines": [236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249], "branches": [[236, 237], [236, 249], [237, 238], [237, 239], [241, 242], [241, 243], [243, 244], [243, 245], [245, 246], [245, 247], [247, 236], [247, 248]]}

import pytest
from tornado.locale import Locale

_supported_locales = {"en", "en_US", "es", "fr"}
_default_locale = "en"

class TestLocale:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self, monkeypatch):
        monkeypatch.setattr("tornado.locale._supported_locales", _supported_locales)
        monkeypatch.setattr("tornado.locale._default_locale", _default_locale)
        yield
        # No teardown necessary as monkeypatch will revert changes

    def test_get_closest_with_empty_code(self):
        result = Locale.get_closest("")
        assert result == Locale.get(_default_locale)

    def test_get_closest_with_hyphen(self):
        result = Locale.get_closest("en-US")
        assert result == Locale.get("en_US")

    def test_get_closest_with_unsupported_locale(self):
        result = Locale.get_closest("de")
        assert result == Locale.get(_default_locale)

    def test_get_closest_with_two_part_locale(self):
        result = Locale.get_closest("es_MX")
        assert result == Locale.get("es")

    def test_get_closest_with_three_part_locale(self):
        result = Locale.get_closest("en_US_POSIX")
        assert result == Locale.get(_default_locale)

    def test_get_closest_with_supported_locale(self):
        result = Locale.get_closest("fr")
        assert result == Locale.get("fr")
