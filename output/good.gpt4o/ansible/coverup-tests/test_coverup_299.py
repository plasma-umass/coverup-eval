# file lib/ansible/plugins/lookup/csvfile.py:122-134
# lines [122, 124, 125, 126, 128, 129, 130, 131, 132, 134]
# branches ['128->129', '128->134', '129->128', '129->130']

import pytest
from unittest import mock
from ansible.errors import AnsibleError
from ansible.plugins.lookup.csvfile import LookupModule

@pytest.fixture
def mock_open(mocker):
    return mocker.patch("builtins.open", mock.mock_open(read_data="key1,value1\nkey2,value2"))

@pytest.fixture
def mock_csv_reader(mocker):
    return mocker.patch("ansible.plugins.lookup.csvfile.CSVReader", return_value=[["key1", "value1"], ["key2", "value2"]])

def test_read_csv_success(mock_open, mock_csv_reader):
    lookup = LookupModule()
    result = lookup.read_csv("dummy.csv", "key1", ",")
    assert result == "value1"

def test_read_csv_key_not_found(mock_open, mock_csv_reader):
    lookup = LookupModule()
    result = lookup.read_csv("dummy.csv", "key3", ",", dflt="default_value")
    assert result == "default_value"

def test_read_csv_exception(mock_open, mock_csv_reader, mocker):
    mock_open.side_effect = IOError("File not found")
    lookup = LookupModule()
    with pytest.raises(AnsibleError, match="csvfile: File not found"):
        lookup.read_csv("dummy.csv", "key1", ",")
