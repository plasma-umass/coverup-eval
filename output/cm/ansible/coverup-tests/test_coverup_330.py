# file lib/ansible/plugins/lookup/csvfile.py:122-134
# lines [122, 124, 125, 126, 128, 129, 130, 131, 132, 134]
# branches ['128->129', '128->134', '129->128', '129->130']

import pytest
from ansible.errors import AnsibleError
from ansible.plugins.lookup.csvfile import LookupModule
from ansible.module_utils._text import to_bytes, to_native
import os
import csv

# Mock CSVReader to control the behavior of csv.reader
class MockCSVReader:
    def __init__(self, rows, *args, **kwargs):
        self.rows = rows

    def __iter__(self):
        return iter(self.rows)

@pytest.fixture
def csvfile(tmp_path):
    # Create a temporary CSV file for testing
    file_path = tmp_path / "test.csv"
    with file_path.open('w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['key', 'value'])
        writer.writerow(['testkey', 'testvalue'])
    return str(file_path)

@pytest.fixture
def lookup():
    return LookupModule()

def test_read_csv_success(csvfile, lookup, mocker):
    # Mock CSVReader to return predefined rows
    mocker.patch('ansible.plugins.lookup.csvfile.CSVReader', return_value=MockCSVReader([['key', 'value'], ['testkey', 'testvalue']]))
    result = lookup.read_csv(csvfile, 'testkey', delimiter=',')
    assert result == 'testvalue', "The lookup should return the value corresponding to the key"

def test_read_csv_default(csvfile, lookup, mocker):
    # Mock CSVReader to return predefined rows
    mocker.patch('ansible.plugins.lookup.csvfile.CSVReader', return_value=MockCSVReader([['key', 'value'], ['testkey', 'testvalue']]))
    result = lookup.read_csv(csvfile, 'nonexistentkey', delimiter=',', dflt='defaultvalue')
    assert result == 'defaultvalue', "The lookup should return the default value when the key is not found"

def test_read_csv_exception(csvfile, lookup, mocker):
    # Mock CSVReader to raise an exception
    def raise_exception(*args, **kwargs):
        raise Exception("Test exception")

    mocker.patch('ansible.plugins.lookup.csvfile.CSVReader', side_effect=raise_exception)
    with pytest.raises(AnsibleError) as excinfo:
        lookup.read_csv(csvfile, 'testkey', delimiter=',')
    assert "csvfile: Test exception" in str(excinfo.value), "The lookup should raise an AnsibleError when an exception occurs"
