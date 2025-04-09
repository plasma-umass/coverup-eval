# file: lib/ansible/parsing/dataloader.py:345-357
# asked: {"lines": [347, 348, 349, 350, 351, 352, 353, 354, 356, 357], "branches": []}
# gained: {"lines": [347, 348, 349, 350, 351, 356, 357], "branches": []}

import os
import tempfile
import pytest
from unittest import mock
from ansible.parsing.dataloader import DataLoader
from ansible.module_utils._text import to_bytes
import ansible.constants as C

@pytest.fixture
def dataloader():
    return DataLoader()

def test_create_content_tempfile_success(dataloader, monkeypatch):
    content = "test content"
    temp_dir = tempfile.gettempdir()
    monkeypatch.setattr(C, 'DEFAULT_LOCAL_TMP', temp_dir)
    
    temp_file = dataloader._create_content_tempfile(content)
    
    assert os.path.isfile(temp_file)
    with open(temp_file, 'rb') as f:
        assert f.read() == to_bytes(content)
    
    os.remove(temp_file)

def test_create_content_tempfile_exception(dataloader, monkeypatch):
    content = "test content"
    temp_dir = tempfile.gettempdir()
    monkeypatch.setattr(C, 'DEFAULT_LOCAL_TMP', temp_dir)
    
    with mock.patch('os.fdopen', side_effect=Exception("fdopen error")):
        with pytest.raises(Exception) as excinfo:
            dataloader._create_content_tempfile(content)
        assert "fdopen error" in str(excinfo.value)
