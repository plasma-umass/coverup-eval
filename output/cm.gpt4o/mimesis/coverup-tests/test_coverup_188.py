# file mimesis/decorators.py:15-47
# lines [15, 26, 27, 28, 29, 32, 33, 34, 35, 36, 38, 39, 41, 42, 43, 45, 47]
# branches []

import pytest
from mimesis.decorators import romanize
from mimesis.exceptions import UnsupportedLocale

# Mock data to simulate the mimesis data module
class MockData:
    ROMANIZATION_DICT = {
        'ru': {'а': 'a', 'б': 'b', 'в': 'v'},
        'uk': {'г': 'h', 'ґ': 'g', 'д': 'd'},
        'kk': {'е': 'e', 'ё': 'yo', 'ж': 'zh'}
    }
    COMMON_LETTERS = {' ': ' ', ',': ',', '.': '.'}

@pytest.fixture
def mock_data(mocker):
    mocker.patch('mimesis.decorators.data', new=MockData)

def test_romanize_ru(mock_data):
    @romanize(locale='ru')
    def cyrillic_text():
        return 'абв,.'

    result = cyrillic_text()
    assert result == 'abv,.'

def test_romanize_uk(mock_data):
    @romanize(locale='uk')
    def cyrillic_text():
        return 'гґд,.'

    result = cyrillic_text()
    assert result == 'hgd,.'

def test_romanize_kk(mock_data):
    @romanize(locale='kk')
    def cyrillic_text():
        return 'еёж,.'

    result = cyrillic_text()
    assert result == 'eyozh,.'

def test_romanize_unsupported_locale(mock_data):
    with pytest.raises(UnsupportedLocale):
        @romanize(locale='unsupported')
        def cyrillic_text():
            return 'абв,.'
        
        cyrillic_text()
