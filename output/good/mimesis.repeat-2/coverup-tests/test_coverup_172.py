# file mimesis/providers/base.py:120-155
# lines [135, 153]
# branches ['134->135', '152->153']

import json
import pytest
from mimesis.providers.base import BaseDataProvider
from unittest.mock import patch
from pathlib import Path

# Define a test class to encapsulate the tests
class TestBaseDataProvider:

    # Test function to cover line 135
    @pytest.fixture
    def provider_with_default_datafile(self, tmp_path):
        # Create a fake locale directory and JSON file
        locale_dir = tmp_path / 'en'
        locale_dir.mkdir()
        datafile_path = locale_dir / 'default.json'
        with open(datafile_path, 'w', encoding='utf8') as f:
            json.dump({'key': 'value'}, f)

        # Instantiate the provider with a fake locale
        provider = BaseDataProvider(locale='en')
        provider._data_dir = str(tmp_path)
        provider._datafile = 'default.json'
        return provider

    def test__pull_without_datafile(self, provider_with_default_datafile):
        # Call the _pull method without specifying a datafile
        provider_with_default_datafile._pull()

        # Assert that the data was loaded correctly
        assert provider_with_default_datafile._data == {'key': 'value'}

    # Test function to cover line 153
    def test__pull_with_locale_separator(self, tmp_path):
        # Create fake locale directories and JSON files
        master_locale_dir = tmp_path / 'en'
        master_locale_dir.mkdir()
        master_datafile_path = master_locale_dir / 'data.json'
        with open(master_datafile_path, 'w', encoding='utf8') as f:
            json.dump({'key': 'master_value'}, f)

        specific_locale_dir = tmp_path / 'en-gb'
        specific_locale_dir.mkdir()
        specific_datafile_path = specific_locale_dir / 'data.json'
        with open(specific_datafile_path, 'w', encoding='utf8') as f:
            json.dump({'specific_key': 'specific_value'}, f)

        # Instantiate the provider with a specific locale
        provider = BaseDataProvider(locale='en-gb')
        provider._data_dir = str(tmp_path)

        # Call the _pull method specifying the datafile
        provider._pull(datafile='data.json')

        # Assert that the data was merged correctly
        assert provider._data == {'key': 'master_value', 'specific_key': 'specific_value'}
