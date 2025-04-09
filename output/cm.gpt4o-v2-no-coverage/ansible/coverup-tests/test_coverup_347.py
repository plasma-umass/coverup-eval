# file: lib/ansible/plugins/lookup/csvfile.py:122-134
# asked: {"lines": [122, 124, 125, 126, 128, 129, 130, 131, 132, 134], "branches": [[128, 129], [128, 134], [129, 128], [129, 130]]}
# gained: {"lines": [122, 124, 125, 126, 128, 129, 130, 131, 132, 134], "branches": [[128, 129], [128, 134], [129, 128], [129, 130]]}

import pytest
from ansible.errors import AnsibleError
from ansible.plugins.lookup.csvfile import LookupModule
from unittest.mock import mock_open, patch

@pytest.fixture
def mock_csv_reader():
    class MockCSVReader:
        def __init__(self, file, delimiter=',', encoding='utf-8'):
            self.rows = [
                ['key1', 'value1'],
                ['key2', 'value2'],
                ['key3', 'value3']
            ]
            self.index = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self.index >= len(self.rows):
                raise StopIteration
            row = self.rows[self.index]
            self.index += 1
            return row

    return MockCSVReader

@pytest.fixture
def mock_open_file():
    m = mock_open(read_data="key1,value1\nkey2,value2\nkey3,value3\n")
    return m

def test_read_csv_found(mock_csv_reader, mock_open_file):
    with patch('ansible.plugins.lookup.csvfile.open', mock_open_file), \
         patch('ansible.plugins.lookup.csvfile.CSVReader', mock_csv_reader):
        lookup = LookupModule()
        result = lookup.read_csv('dummy.csv', 'key2', ',')
        assert result == 'value2'

def test_read_csv_not_found(mock_csv_reader, mock_open_file):
    with patch('ansible.plugins.lookup.csvfile.open', mock_open_file), \
         patch('ansible.plugins.lookup.csvfile.CSVReader', mock_csv_reader):
        lookup = LookupModule()
        result = lookup.read_csv('dummy.csv', 'key4', ',')
        assert result is None

def test_read_csv_default_value(mock_csv_reader, mock_open_file):
    with patch('ansible.plugins.lookup.csvfile.open', mock_open_file), \
         patch('ansible.plugins.lookup.csvfile.CSVReader', mock_csv_reader):
        lookup = LookupModule()
        result = lookup.read_csv('dummy.csv', 'key4', ',', dflt='default_value')
        assert result == 'default_value'

def test_read_csv_exception(mock_open_file):
    with patch('ansible.plugins.lookup.csvfile.open', mock_open_file), \
         patch('ansible.plugins.lookup.csvfile.CSVReader', side_effect=Exception('error')):
        lookup = LookupModule()
        with pytest.raises(AnsibleError, match="csvfile: error"):
            lookup.read_csv('dummy.csv', 'key1', ',')
