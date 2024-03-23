# file mimesis/decorators.py:15-47
# lines [15, 26, 27, 28, 29, 32, 33, 34, 35, 36, 38, 39, 41, 42, 43, 45, 47]
# branches []

import pytest
from mimesis.exceptions import UnsupportedLocale
from mimesis.decorators import romanize
from mimesis import data

# Mock function to be decorated
def mock_cyrillic_text():
    return "Привет"

# Test for supported locale
@pytest.mark.parametrize("locale", ['ru', 'uk', 'kk'])
def test_romanize_supported_locale(locale):
    decorated_func = romanize(locale)(mock_cyrillic_text)
    result = decorated_func()
    assert isinstance(result, str)
    assert result.isascii()  # The result should be ASCII characters only

# Test for unsupported locale
def test_romanize_unsupported_locale():
    with pytest.raises(UnsupportedLocale):
        decorated_func = romanize('unsupported_locale')(mock_cyrillic_text)
        decorated_func()
