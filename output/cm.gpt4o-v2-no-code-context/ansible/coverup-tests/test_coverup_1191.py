# file: lib/ansible/plugins/lookup/csvfile.py:96-117
# asked: {"lines": [104], "branches": [[103, 104]]}
# gained: {"lines": [104], "branches": [[103, 104]]}

import pytest
import csv
import codecs
from io import StringIO, BytesIO
from ansible.plugins.lookup.csvfile import CSVReader

class MockCSVRecoder:
    def __init__(self, f, encoding):
        self.f = f
        self.encoding = encoding

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.f)

    next = __next__  # For Python 2

def test_csvreader_py2(monkeypatch):
    # Mock PY2 to be True
    monkeypatch.setattr('ansible.plugins.lookup.csvfile.PY2', True)
    monkeypatch.setattr('ansible.plugins.lookup.csvfile.CSVRecoder', MockCSVRecoder)

    data = "col1,col2\nval1,val2\n"
    f = iter(data.splitlines())

    reader = CSVReader(f)
    rows = list(reader)

    assert rows == [['col1', 'col2'], ['val1', 'val2']]

def test_csvreader_py3(monkeypatch):
    # Mock PY2 to be False
    monkeypatch.setattr('ansible.plugins.lookup.csvfile.PY2', False)

    data = "col1,col2\nval1,val2\n"
    f = BytesIO(data.encode('utf-8'))

    reader = CSVReader(f)
    rows = list(reader)

    assert rows == [['col1', 'col2'], ['val1', 'val2']]
