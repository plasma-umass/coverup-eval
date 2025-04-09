# file: lib/ansible/parsing/dataloader.py:142-169
# asked: {"lines": [142, 155, 156, 158, 161, 162, 164, 165, 166, 167, 168, 169], "branches": [[155, 156], [155, 158], [161, 162], [161, 164]]}
# gained: {"lines": [142, 155, 156, 158, 161, 162, 164, 165, 166, 167, 168, 169], "branches": [[155, 156], [155, 158], [161, 162], [161, 164]]}

import pytest
from unittest.mock import mock_open, patch
from ansible.errors import AnsibleFileNotFound, AnsibleParserError
from ansible.module_utils.six import binary_type, text_type
from ansible.module_utils._text import to_bytes, to_native
from ansible.parsing.dataloader import DataLoader

class TestGetFileContents:
    
    @pytest.fixture
    def dataloader(self):
        return DataLoader()

    def test_invalid_filename_none(self, dataloader):
        with pytest.raises(AnsibleParserError, match="Invalid filename: 'None'"):
            dataloader._get_file_contents(None)

    def test_invalid_filename_not_string(self, dataloader):
        with pytest.raises(AnsibleParserError, match="Invalid filename: '123'"):
            dataloader._get_file_contents(123)

    @patch('ansible.parsing.dataloader.DataLoader.path_dwim', return_value='/fake/path')
    @patch('ansible.parsing.dataloader.DataLoader.path_exists', return_value=False)
    def test_file_not_found(self, mock_path_dwim, mock_path_exists, dataloader):
        with pytest.raises(AnsibleFileNotFound, match="Unable to retrieve file contents"):
            dataloader._get_file_contents('nonexistent_file')

    @patch('ansible.parsing.dataloader.DataLoader.path_dwim', return_value=b'/fake/path')
    @patch('ansible.parsing.dataloader.DataLoader.path_exists', return_value=True)
    @patch('builtins.open', new_callable=mock_open, read_data=b'some data')
    @patch('ansible.parsing.dataloader.DataLoader._decrypt_if_vault_data', return_value=(b'some data', True))
    def test_file_read_success(self, mock_decrypt, mock_open, mock_path_exists, mock_path_dwim, dataloader):
        result, show_content = dataloader._get_file_contents('existing_file')
        assert result == b'some data'
        assert show_content is True
        mock_open.assert_called_once_with(b'/fake/path', 'rb')

    @patch('ansible.parsing.dataloader.DataLoader.path_dwim', return_value=b'/fake/path')
    @patch('ansible.parsing.dataloader.DataLoader.path_exists', return_value=True)
    @patch('builtins.open', side_effect=OSError("Permission denied"))
    def test_file_read_oserror(self, mock_open, mock_path_exists, mock_path_dwim, dataloader):
        with pytest.raises(AnsibleParserError, match="an error occurred while trying to read the file 'existing_file'"):
            dataloader._get_file_contents('existing_file')
