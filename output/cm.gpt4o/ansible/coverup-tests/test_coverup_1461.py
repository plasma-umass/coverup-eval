# file lib/ansible/plugins/lookup/csvfile.py:96-117
# lines [104]
# branches ['103->104']

import pytest
import csv
import codecs
from unittest import mock

# Assuming the CSVReader class is defined in ansible.plugins.lookup.csvfile
from ansible.plugins.lookup.csvfile import CSVReader

# Mocking PY2 to be True to test the branch
@pytest.fixture
def mock_py2_true(monkeypatch):
    monkeypatch.setattr('ansible.plugins.lookup.csvfile.PY2', True)

# Mocking CSVRecoder for the test
class MockCSVRecoder:
    def __init__(self, f, encoding):
        self.f = f
        self.encoding = encoding

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.f)

    next = __next__  # For Python 2

@pytest.fixture
def mock_csvrecoder(monkeypatch):
    monkeypatch.setattr('ansible.plugins.lookup.csvfile.CSVRecoder', MockCSVRecoder)

def test_csvreader_py2(mock_py2_true, mock_csvrecoder):
    csv_content = "col1,col2\nval1,val2\n"
    f = iter(csv_content.splitlines())
    
    reader = CSVReader(f)
    rows = list(reader)
    
    assert rows == [['col1', 'col2'], ['val1', 'val2']]
