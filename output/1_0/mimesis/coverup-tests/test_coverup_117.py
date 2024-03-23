# file mimesis/providers/file.py:84-99
# lines [93, 94, 96, 97, 98]
# branches []

import pytest
from mimesis.enums import FileType
from mimesis.providers import File
from unittest.mock import patch

@pytest.fixture
def file_provider():
    return File()

def test_file_name_with_file_type(file_provider):
    with patch.object(file_provider, '_File__text') as mock_text, \
         patch.object(file_provider, 'extension') as mock_extension:
        mock_text.word.return_value = 'legislative'
        mock_extension.return_value = '.txt'
        file_name = file_provider.file_name(file_type=FileType.TEXT)
        assert file_name.endswith('.txt')
        assert 'legislative' in file_name

def test_file_name_without_file_type(file_provider):
    with patch.object(file_provider, '_File__text') as mock_text, \
         patch.object(file_provider, 'extension') as mock_extension:
        mock_text.word.return_value = 'legislative'
        mock_extension.return_value = '.log'
        file_name = file_provider.file_name()
        assert file_name.endswith('.log')
        assert 'legislative' in file_name
