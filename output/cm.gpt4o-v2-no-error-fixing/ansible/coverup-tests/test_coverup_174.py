# file: lib/ansible/plugins/lookup/csvfile.py:122-134
# asked: {"lines": [122, 124, 125, 126, 128, 129, 130, 131, 132, 134], "branches": [[128, 129], [128, 134], [129, 128], [129, 130]]}
# gained: {"lines": [122, 124, 125, 126, 128, 129, 130, 131, 132, 134], "branches": [[128, 129], [128, 134], [129, 128], [129, 130]]}

import pytest
from ansible.errors import AnsibleError
from ansible.plugins.lookup.csvfile import LookupModule
from unittest.mock import mock_open, patch

@pytest.fixture
def lookup_module():
    return LookupModule()

def test_read_csv_key_found(lookup_module):
    mock_csv_content = b"key1,value1\nkey2,value2\n"
    with patch("builtins.open", mock_open(read_data=mock_csv_content)), \
         patch("ansible.plugins.lookup.csvfile.CSVReader", return_value=[["key1", "value1"], ["key2", "value2"]]):
        result = lookup_module.read_csv("dummy.csv", "key2", ",")
        assert result == "value2"

def test_read_csv_key_not_found(lookup_module):
    mock_csv_content = b"key1,value1\nkey2,value2\n"
    with patch("builtins.open", mock_open(read_data=mock_csv_content)), \
         patch("ansible.plugins.lookup.csvfile.CSVReader", return_value=[["key1", "value1"], ["key2", "value2"]]):
        result = lookup_module.read_csv("dummy.csv", "key3", ",", dflt="default_value")
        assert result == "default_value"

def test_read_csv_exception(lookup_module):
    with patch("builtins.open", side_effect=Exception("file not found")):
        with pytest.raises(AnsibleError, match="csvfile: file not found"):
            lookup_module.read_csv("dummy.csv", "key1", ",")

def test_read_csv_invalid_column(lookup_module):
    mock_csv_content = b"key1,value1\nkey2,value2\n"
    with patch("builtins.open", mock_open(read_data=mock_csv_content)), \
         patch("ansible.plugins.lookup.csvfile.CSVReader", return_value=[["key1", "value1"], ["key2", "value2"]]):
        with pytest.raises(AnsibleError, match="csvfile: list index out of range"):
            lookup_module.read_csv("dummy.csv", "key1", ",", col=5)
