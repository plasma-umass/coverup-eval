# file: lib/ansible/plugins/lookup/csvfile.py:80-93
# asked: {"lines": [85, 88, 91], "branches": []}
# gained: {"lines": [85, 88, 91], "branches": []}

import pytest
import codecs
from io import BytesIO
from ansible.plugins.lookup.csvfile import CSVRecoder

def test_csvrecoder_init():
    # Prepare a sample CSV content
    sample_csv = b"name,age\nAlice,30\nBob,25"
    f = BytesIO(sample_csv)
    
    # Initialize CSVRecoder
    recoder = CSVRecoder(f, encoding='utf-8')
    
    # Assert that the reader is correctly initialized
    assert recoder.reader is not None

def test_csvrecoder_iter():
    # Prepare a sample CSV content
    sample_csv = b"name,age\nAlice,30\nBob,25"
    f = BytesIO(sample_csv)
    
    # Initialize CSVRecoder
    recoder = CSVRecoder(f, encoding='utf-8')
    
    # Assert that __iter__ returns self
    assert iter(recoder) is recoder

def test_csvrecoder_next():
    # Prepare a sample CSV content
    sample_csv = b"name,age\nAlice,30\nBob,25"
    f = BytesIO(sample_csv)
    
    # Initialize CSVRecoder with correct encoding
    recoder = CSVRecoder(f, encoding='utf-8')
    
    # Read the first line
    first_line = next(recoder)
    
    # Assert that the first line is correctly encoded to UTF-8
    assert first_line == b"name,age\n"
    
    # Read the second line
    second_line = next(recoder)
    
    # Assert that the second line is correctly encoded to UTF-8
    assert second_line == b"Alice,30\n"
