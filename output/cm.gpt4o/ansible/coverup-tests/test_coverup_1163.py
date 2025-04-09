# file lib/ansible/plugins/lookup/csvfile.py:96-117
# lines [103, 104, 106, 108, 111, 112, 117]
# branches ['103->104', '103->106']

import pytest
import codecs
import csv
from ansible.plugins.lookup.csvfile import CSVReader
from ansible.module_utils.six import PY2
from ansible.module_utils._text import to_text
import io

def test_csvreader_full_coverage(mocker):
    # Mocking PY2 to be False to cover the else branch
    mocker.patch('ansible.plugins.lookup.csvfile.PY2', False)
    
    # Creating a sample CSV content
    csv_content = "name,age\nJohn Doe,30\nJane Doe,25"
    
    # Using io.BytesIO to simulate file object and encode content to bytes
    f = io.BytesIO(csv_content.encode('utf-8'))
    
    # Creating an instance of CSVReader
    reader = CSVReader(f)
    
    # Asserting that the reader object is an instance of CSVReader
    assert isinstance(reader, CSVReader)
    
    # Reading the first row
    row = next(reader)
    
    # Asserting the first row content
    assert row == ['name', 'age']
    
    # Reading the second row
    row = next(reader)
    
    # Asserting the second row content
    assert row == ['John Doe', '30']
    
    # Reading the third row
    row = next(reader)
    
    # Asserting the third row content
    assert row == ['Jane Doe', '25']
    
    # Asserting that the reader is iterable and returns itself
    assert iter(reader) is reader
