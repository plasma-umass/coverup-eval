# file mimesis/providers/base.py:167-175
# lines [167, 173, 174, 175]
# branches []

import pytest
from mimesis.providers.base import BaseDataProvider
from mimesis import locales
from unittest.mock import patch

class DummyProvider(BaseDataProvider):
    def _pull(self):
        pass  # Dummy _pull method to avoid actual data pulling in tests

@pytest.fixture
def dummy_provider():
    return DummyProvider()

def test_override_locale(dummy_provider):
    with patch.object(dummy_provider, '_pull') as mock_pull:
        # Ensure the cache is cleared and _pull is called
        dummy_provider._override_locale()
        mock_pull.cache_clear.assert_called_once()
        mock_pull.assert_called_once()

        # Change the locale and ensure _pull is called with the new locale
        new_locale = locales.RU
        dummy_provider._override_locale(new_locale)
        assert dummy_provider.locale == new_locale
        mock_pull.cache_clear.assert_called()
        mock_pull.assert_called()
