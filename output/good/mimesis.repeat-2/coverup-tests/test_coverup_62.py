# file mimesis/providers/base.py:167-175
# lines [167, 173, 174, 175]
# branches []

import pytest
from mimesis.providers.base import BaseDataProvider
from mimesis import locales
from unittest.mock import MagicMock

class TestBaseDataProvider:
    @pytest.fixture
    def provider(self):
        return BaseDataProvider()

    @pytest.fixture
    def mock_pull(self, mocker, provider):
        mocker.patch.object(provider, '_pull', MagicMock())

    def test_override_locale(self, provider, mock_pull):
        # Test default locale
        provider._override_locale()
        provider._pull.assert_called_once()
        assert provider.locale == locales.DEFAULT_LOCALE

        provider._pull.reset_mock()

        # Test overriding locale
        new_locale = 'es'
        provider._override_locale(new_locale)
        provider._pull.assert_called_once()
        assert provider.locale == new_locale
