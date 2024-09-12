# file: lib/ansible/plugins/lookup/csvfile.py:122-134
# asked: {"lines": [122, 124, 125, 126, 128, 129, 130, 131, 132, 134], "branches": [[128, 129], [128, 134], [129, 128], [129, 130]]}
# gained: {"lines": [122, 124, 125, 126, 128, 129, 130, 131, 132, 134], "branches": [[128, 129], [128, 134], [129, 128], [129, 130]]}

import pytest
from ansible.errors import AnsibleError
from ansible.plugins.lookup.csvfile import LookupModule
from ansible.module_utils._text import to_bytes
import os

class MockCSVReader:
    def __init__(self, file, delimiter, encoding):
        self.rows = [
            ["key1", "value1"],
            ["key2", "value2"],
            ["key3", "value3"]
        ]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.rows):
            row = self.rows[self.index]
            self.index += 1
            return row
        else:
            raise StopIteration

@pytest.fixture
def mock_csv_reader(monkeypatch):
    def mock_csv_reader_init(self, file, delimiter, encoding):
        self.rows = [
            ["key1", "value1"],
            ["key2", "value2"],
            ["key3", "value3"]
        ]
        self.index = 0

    monkeypatch.setattr("ansible.plugins.lookup.csvfile.CSVReader.__init__", mock_csv_reader_init)
    monkeypatch.setattr("ansible.plugins.lookup.csvfile.CSVReader.__iter__", lambda self: iter(self.rows))
    monkeypatch.setattr("ansible.plugins.lookup.csvfile.CSVReader.__next__", lambda self: next(iter(self.rows)))

@pytest.fixture
def create_temp_csv_file(tmp_path):
    def _create_temp_csv_file(content):
        file_path = tmp_path / "test.csv"
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        return str(file_path)
    return _create_temp_csv_file

def test_read_csv_success(mock_csv_reader, create_temp_csv_file):
    lookup = LookupModule()
    csv_content = "key1,value1\nkey2,value2\nkey3,value3\n"
    csv_file = create_temp_csv_file(csv_content)
    
    result = lookup.read_csv(csv_file, "key2", ",")
    assert result == "value2"

def test_read_csv_key_not_found(mock_csv_reader, create_temp_csv_file):
    lookup = LookupModule()
    csv_content = "key1,value1\nkey2,value2\nkey3,value3\n"
    csv_file = create_temp_csv_file(csv_content)
    
    result = lookup.read_csv(csv_file, "key4", ",", dflt="default_value")
    assert result == "default_value"

def test_read_csv_exception(mock_csv_reader, create_temp_csv_file, monkeypatch):
    lookup = LookupModule()
    csv_content = "key1,value1\nkey2,value2\nkey3,value3\n"
    csv_file = create_temp_csv_file(csv_content)
    
    def mock_open(*args, **kwargs):
        raise IOError("mocked error")
    
    monkeypatch.setattr("builtins.open", mock_open)
    
    with pytest.raises(AnsibleError, match="csvfile: mocked error"):
        lookup.read_csv(csv_file, "key2", ",")
