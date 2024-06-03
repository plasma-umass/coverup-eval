# file lib/ansible/plugins/lookup/csvfile.py:80-93
# lines [80, 81, 84, 85, 87, 88, 90, 91, 93]
# branches []

import pytest
import codecs
from io import BytesIO
from ansible.plugins.lookup.csvfile import CSVRecoder

def test_csvrecoder_utf8_encoding():
    # Create a mock file with some content
    mock_file_content = b"name,age\nAlice,30\nBob,25\n"
    mock_file = BytesIO(mock_file_content)
    
    # Initialize CSVRecoder with the mock file
    recoder = CSVRecoder(mock_file, encoding='utf-8')
    
    # Read the lines using the recoder
    lines = list(recoder)
    
    # Verify the lines are correctly encoded in UTF-8
    assert lines == [b"name,age\n", b"Alice,30\n", b"Bob,25\n"]

    # Clean up
    mock_file.close()

def test_csvrecoder_non_utf8_encoding():
    # Create a mock file with some content in a different encoding
    mock_file_content = "name,age\nAlice,30\nBob,25\n".encode('latin-1')
    mock_file = BytesIO(mock_file_content)
    
    # Initialize CSVRecoder with the mock file and latin-1 encoding
    recoder = CSVRecoder(mock_file, encoding='latin-1')
    
    # Read the lines using the recoder
    lines = list(recoder)
    
    # Verify the lines are correctly encoded in UTF-8
    assert lines == [b"name,age\n", b"Alice,30\n", b"Bob,25\n"]

    # Clean up
    mock_file.close()
