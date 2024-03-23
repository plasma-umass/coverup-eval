# file thefuck/rules/dirty_unzip.py:15-25
# lines [15, 20, 21, 22, 23, 25]
# branches ['20->exit', '20->21', '21->20', '21->22', '22->23', '22->25']

import pytest
from thefuck.rules.dirty_unzip import _zip_file
from thefuck.types import Command

@pytest.fixture
def mock_command(mocker):
    return mocker.Mock(spec=Command)

def test_zip_file_with_zip_extension(mock_command):
    mock_command.script_parts = ['unzip', 'archive.zip', 'file1', 'file2']
    assert _zip_file(mock_command) == 'archive.zip'

def test_zip_file_without_zip_extension(mock_command):
    mock_command.script_parts = ['unzip', 'archive', 'file1', 'file2']
    assert _zip_file(mock_command) == 'archive.zip'
