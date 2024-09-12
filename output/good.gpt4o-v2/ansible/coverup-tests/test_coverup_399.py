# file: lib/ansible/parsing/dataloader.py:345-357
# asked: {"lines": [345, 347, 348, 349, 350, 351, 352, 353, 354, 356, 357], "branches": []}
# gained: {"lines": [345, 347, 348, 349, 350, 351, 356, 357], "branches": []}

import os
import tempfile
import pytest
from unittest import mock
from ansible.parsing.dataloader import DataLoader
from ansible import constants as C
from ansible.module_utils._text import to_bytes

@pytest.fixture
def dataloader():
    return DataLoader()

def test_create_content_tempfile_success(dataloader, monkeypatch):
    test_content = "test content"
    test_content_bytes = to_bytes(test_content)

    with tempfile.TemporaryDirectory() as tmpdir:
        monkeypatch.setattr(C, 'DEFAULT_LOCAL_TMP', tmpdir)
        
        temp_file_path = dataloader._create_content_tempfile(test_content)
        
        assert os.path.isfile(temp_file_path)
        
        with open(temp_file_path, 'rb') as f:
            assert f.read() == test_content_bytes
        
        os.remove(temp_file_path)

def test_create_content_tempfile_exception(dataloader, monkeypatch):
    test_content = "test content"
    
    with tempfile.TemporaryDirectory() as tmpdir:
        monkeypatch.setattr(C, 'DEFAULT_LOCAL_TMP', tmpdir)
        
        with mock.patch('ansible.parsing.dataloader.to_bytes', side_effect=Exception("mocked exception")):
            with pytest.raises(Exception, match="mocked exception"):
                dataloader._create_content_tempfile(test_content)
