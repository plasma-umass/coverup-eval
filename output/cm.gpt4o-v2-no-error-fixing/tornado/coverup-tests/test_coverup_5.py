# file: tornado/locale.py:233-249
# asked: {"lines": [233, 234, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249], "branches": [[236, 237], [236, 249], [237, 238], [237, 239], [241, 242], [241, 243], [243, 244], [243, 245], [245, 246], [245, 247], [247, 236], [247, 248]]}
# gained: {"lines": [233, 234, 236, 237, 238, 239, 240, 241, 243, 244, 245, 246, 247, 249], "branches": [[236, 237], [236, 249], [237, 238], [237, 239], [241, 243], [243, 244], [243, 245], [245, 246], [245, 247], [247, 236]]}

import pytest
from tornado.locale import Locale, _supported_locales, _default_locale

class MockLocale(Locale):
    @classmethod
    def get(cls, code):
        return f"Locale for {code}"

@pytest.fixture
def mock_supported_locales(monkeypatch):
    mock_locales = frozenset(['en_US', 'en', 'es_ES', 'es'])
    monkeypatch.setattr('tornado.locale._supported_locales', mock_locales)
    return mock_locales

@pytest.fixture
def mock_default_locale(monkeypatch):
    monkeypatch.setattr('tornado.locale._default_locale', 'en_US')
    return 'en_US'

def test_get_closest_with_valid_locale(mock_supported_locales, mock_default_locale):
    result = MockLocale.get_closest('en-US')
    assert result == "Locale for en_US"

def test_get_closest_with_empty_locale(mock_supported_locales, mock_default_locale):
    result = MockLocale.get_closest('')
    assert result == "Locale for en_US"

def test_get_closest_with_invalid_locale(mock_supported_locales, mock_default_locale):
    result = MockLocale.get_closest('invalid')
    assert result == "Locale for en_US"

def test_get_closest_with_two_part_locale(mock_supported_locales, mock_default_locale):
    result = MockLocale.get_closest('es-ES')
    assert result == "Locale for es_ES"

def test_get_closest_with_one_part_locale(mock_supported_locales, mock_default_locale):
    result = MockLocale.get_closest('es')
    assert result == "Locale for es"

def test_get_closest_with_multiple_locales(mock_supported_locales, mock_default_locale):
    result = MockLocale.get_closest('fr-FR', 'es-ES')
    assert result == "Locale for es_ES"
