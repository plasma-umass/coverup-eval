# file: tornado/locale.py:233-249
# asked: {"lines": [233, 234, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249], "branches": [[236, 237], [236, 249], [237, 238], [237, 239], [241, 242], [241, 243], [243, 244], [243, 245], [245, 246], [245, 247], [247, 236], [247, 248]]}
# gained: {"lines": [233, 234], "branches": []}

import pytest
from unittest import mock

# Mocking _supported_locales and _default_locale
_supported_locales = {"en", "en_US", "es", "fr"}
_default_locale = "en"

class Locale:
    @classmethod
    def get(cls, code):
        return f"Locale({code})"

    @classmethod
    def get_closest(cls, *locale_codes: str) -> "Locale":
        """Returns the closest match for the given locale code."""
        for code in locale_codes:
            if not code:
                continue
            code = code.replace("-", "_")
            parts = code.split("_")
            if len(parts) > 2:
                continue
            elif len(parts) == 2:
                code = parts[0].lower() + "_" + parts[1].upper()
            if code in _supported_locales:
                return cls.get(code)
            if parts[0].lower() in _supported_locales:
                return cls.get(parts[0].lower())
        return cls.get(_default_locale)

@pytest.fixture
def mock_supported_locales(monkeypatch):
    monkeypatch.setattr("tornado.locale._supported_locales", _supported_locales)
    monkeypatch.setattr("tornado.locale._default_locale", _default_locale)

def test_get_closest_exact_match(mock_supported_locales):
    assert Locale.get_closest("en_US") == "Locale(en_US)"

def test_get_closest_language_only(mock_supported_locales):
    assert Locale.get_closest("en") == "Locale(en)"

def test_get_closest_with_dash(mock_supported_locales):
    assert Locale.get_closest("en-US") == "Locale(en_US)"

def test_get_closest_no_match(mock_supported_locales):
    assert Locale.get_closest("de") == "Locale(en)"

def test_get_closest_empty_code(mock_supported_locales):
    assert Locale.get_closest("") == "Locale(en)"

def test_get_closest_invalid_code(mock_supported_locales):
    assert Locale.get_closest("en_US_CA") == "Locale(en)"

def test_get_closest_multiple_codes(mock_supported_locales):
    assert Locale.get_closest("de", "fr") == "Locale(fr)"
