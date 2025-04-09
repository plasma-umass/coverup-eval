# file: lib/ansible/plugins/lookup/csvfile.py:122-134
# asked: {"lines": [122, 124, 125, 126, 128, 129, 130, 131, 132, 134], "branches": [[128, 129], [128, 134], [129, 128], [129, 130]]}
# gained: {"lines": [122, 124, 125, 126, 128, 129, 130, 131, 132, 134], "branches": [[128, 129], [128, 134], [129, 128], [129, 130]]}

import pytest
from ansible.plugins.lookup.csvfile import LookupModule
from ansible.errors import AnsibleError
from unittest.mock import mock_open, patch
from ansible.module_utils._text import to_bytes, to_native

@pytest.fixture
def lookup_module():
    return LookupModule()

def test_read_csv_key_found(lookup_module):
    mock_csv_content = b"key1,value1\nkey2,value2\n"
    with patch("builtins.open", mock_open(read_data=mock_csv_content)) as mock_file:
        result = lookup_module.read_csv("dummy.csv", "key1", ",")
        assert result == "value1"
        mock_file.assert_called_once_with(to_bytes("dummy.csv"), 'rb')

def test_read_csv_key_not_found(lookup_module):
    mock_csv_content = b"key1,value1\nkey2,value2\n"
    with patch("builtins.open", mock_open(read_data=mock_csv_content)) as mock_file:
        result = lookup_module.read_csv("dummy.csv", "key3", ",", dflt="default_value")
        assert result == "default_value"
        mock_file.assert_called_once_with(to_bytes("dummy.csv"), 'rb')

def test_read_csv_exception(lookup_module):
    with patch("builtins.open", side_effect=Exception("file not found")):
        with pytest.raises(AnsibleError, match="csvfile: file not found"):
            lookup_module.read_csv("dummy.csv", "key1", ",")

def test_read_csv_custom_delimiter(lookup_module):
    mock_csv_content = b"key1|value1\nkey2|value2\n"
    with patch("builtins.open", mock_open(read_data=mock_csv_content)) as mock_file:
        result = lookup_module.read_csv("dummy.csv", "key2", "|")
        assert result == "value2"
        mock_file.assert_called_once_with(to_bytes("dummy.csv"), 'rb')

def test_read_csv_custom_encoding(lookup_module):
    mock_csv_content = b"key1,value1\nkey2,value2\n"
    with patch("builtins.open", mock_open(read_data=mock_csv_content)) as mock_file:
        result = lookup_module.read_csv("dummy.csv", "key1", ",", encoding="utf-8")
        assert result == "value1"
        mock_file.assert_called_once_with(to_bytes("dummy.csv"), 'rb')

def test_read_csv_custom_column(lookup_module):
    mock_csv_content = b"key1,value1,extra1\nkey2,value2,extra2\n"
    with patch("builtins.open", mock_open(read_data=mock_csv_content)) as mock_file:
        result = lookup_module.read_csv("dummy.csv", "key1", ",", col=2)
        assert result == "extra1"
        mock_file.assert_called_once_with(to_bytes("dummy.csv"), 'rb')
