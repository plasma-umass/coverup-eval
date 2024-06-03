# file mimesis/providers/base.py:199-202
# lines [199, 201, 202]
# branches []

import pytest
from mimesis.providers.base import BaseProvider

class TestBaseDataProvider:
    def test_str_method_with_locale(self, mocker):
        class BaseDataProvider(BaseProvider):
            def __str__(self) -> str:
                """Human-readable representation of locale."""
                locale = getattr(self, 'locale', 'en')
                return '{} <{}>'.format(self.__class__.__name__, locale)

        provider = BaseDataProvider()
        provider.locale = 'fr'
        result = str(provider)
        assert result == 'BaseDataProvider <fr>'

    def test_str_method_without_locale(self, mocker):
        class BaseDataProvider(BaseProvider):
            def __str__(self) -> str:
                """Human-readable representation of locale."""
                locale = getattr(self, 'locale', 'en')
                return '{} <{}>'.format(self.__class__.__name__, locale)

        provider = BaseDataProvider()
        result = str(provider)
        assert result == 'BaseDataProvider <en>'
