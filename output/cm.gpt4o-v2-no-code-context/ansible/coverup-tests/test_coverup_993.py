# file: lib/ansible/parsing/dataloader.py:345-357
# asked: {"lines": [347, 348, 349, 350, 351, 352, 353, 354, 356, 357], "branches": []}
# gained: {"lines": [347, 348, 349, 350, 351, 356, 357], "branches": []}

import os
import tempfile
import pytest
from ansible.parsing.dataloader import DataLoader
from ansible import constants as C
from ansible.module_utils._text import to_bytes

@pytest.fixture
def dataloader():
    return DataLoader()

def test_create_content_tempfile_success(dataloader, monkeypatch):
    test_content = "test content"
    temp_dir = tempfile.gettempdir()
    
    monkeypatch.setattr(C, 'DEFAULT_LOCAL_TMP', temp_dir)
    
    temp_file = dataloader._create_content_tempfile(test_content)
    
    assert os.path.exists(temp_file)
    
    with open(temp_file, 'rb') as f:
        assert f.read() == to_bytes(test_content)
    
    os.remove(temp_file)

def test_create_content_tempfile_exception(dataloader, monkeypatch, mocker):
    test_content = "test content"
    temp_dir = tempfile.gettempdir()
    
    monkeypatch.setattr(C, 'DEFAULT_LOCAL_TMP', temp_dir)
    
    mocker.patch('os.fdopen', side_effect=Exception("Mocked exception"))
    
    with pytest.raises(Exception, match="Mocked exception"):
        dataloader._create_content_tempfile(test_content)
