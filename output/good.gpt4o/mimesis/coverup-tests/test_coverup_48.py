# file mimesis/providers/base.py:76-87
# lines [76, 77, 83, 84, 85, 86, 87]
# branches []

import pytest
from unittest.mock import patch, MagicMock
from mimesis.providers.base import BaseDataProvider
from mimesis import locales

@pytest.fixture
def mock_path(mocker):
    mock_path = mocker.patch('mimesis.providers.base.Path')
    mock_path.return_value.parent.parent.joinpath.return_value = 'mocked_path'
    return mock_path

def test_base_data_provider_initialization(mock_path):
    locale = locales.DEFAULT_LOCALE
    seed = 12345

    with patch('mimesis.providers.base.__file__', new='/output/mimesis/providers/base.py'):
        provider = BaseDataProvider(locale=locale, seed=seed)

    assert provider._data == {}
    assert provider._datafile == ''
    assert provider._data_dir == 'mocked_path'
    mock_path.assert_called_once_with('/output/mimesis/providers/base.py')
    mock_path.return_value.parent.parent.joinpath.assert_called_once_with('data')
