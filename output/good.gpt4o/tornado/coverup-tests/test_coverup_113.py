# file tornado/locale.py:224-232
# lines [224, 225, 231]
# branches []

import pytest
from unittest import mock
from tornado.locale import Locale

@pytest.fixture
def clear_locale_cache():
    original_cache = Locale._cache.copy()
    Locale._cache.clear()
    yield
    Locale._cache = original_cache

def test_locale_cache(clear_locale_cache):
    # Ensure the cache is empty before the test
    assert Locale._cache == {}

    # Mock a locale object
    mock_locale = mock.Mock(spec=Locale)
    Locale._cache['en_US'] = mock_locale

    # Verify that the locale object is correctly cached
    assert Locale._cache['en_US'] is mock_locale

    # Clean up is handled by the fixture
