# file mimesis/providers/base.py:167-175
# lines [173, 174, 175]
# branches []

import pytest
from mimesis.providers.base import BaseDataProvider
from mimesis import locales

@pytest.fixture
def base_data_provider():
    return BaseDataProvider()

def test_override_locale(mocker, base_data_provider):
    mock_pull = mocker.patch.object(base_data_provider, '_pull')
    mock_cache_clear = mocker.patch.object(base_data_provider._pull, 'cache_clear')

    new_locale = locales.DEFAULT_LOCALE
    base_data_provider._override_locale(new_locale)

    assert base_data_provider.locale == new_locale
    mock_cache_clear.assert_called_once()
    mock_pull.assert_called_once()
