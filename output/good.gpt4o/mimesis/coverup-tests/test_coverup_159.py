# file mimesis/providers/base.py:157-165
# lines [157, 165]
# branches []

import pytest
from mimesis.providers.base import BaseProvider

class TestBaseDataProvider:
    @pytest.fixture
    def base_data_provider(self, mocker):
        class MockBaseDataProvider(BaseProvider):
            def __init__(self, locale=None):
                self.locale = locale or 'en'
            
            def get_current_locale(self) -> str:
                return self.locale
        
        return MockBaseDataProvider

    def test_get_current_locale_default(self, base_data_provider):
        provider = base_data_provider()
        assert provider.get_current_locale() == 'en'

    def test_get_current_locale_custom(self, base_data_provider):
        provider = base_data_provider(locale='fr')
        assert provider.get_current_locale() == 'fr'
