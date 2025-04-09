# file lib/ansible/plugins/lookup/csvfile.py:96-117
# lines [96, 97, 102, 103, 104, 106, 108, 110, 111, 112, 114, 116, 117]
# branches ['103->104', '103->106']

import csv
import codecs
import os
import pytest
from ansible.plugins.lookup.csvfile import CSVReader

# Define a test function to improve coverage
def test_csv_reader(mocker, tmp_path):
    # Create a temporary CSV file
    csv_file = tmp_path / "test.csv"
    csv_file.write_text(u"col1,col2\nval1,val3", encoding='utf-8')

    # Mock the PY2 constant to False to test Python 3 code path
    mocker.patch('ansible.plugins.lookup.csvfile.PY2', False)

    # Open the temporary CSV file and test the CSVReader
    with csv_file.open('rb') as f:  # Open in binary mode for the codecs module
        reader = CSVReader(f)
        rows = list(reader)

    # Assert that the CSVReader read the correct data
    assert rows == [['col1', 'col2'], ['val1', 'val3']]

    # Clean up the temporary CSV file
    csv_file.unlink()
