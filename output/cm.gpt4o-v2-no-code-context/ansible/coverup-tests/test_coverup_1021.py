# file: lib/ansible/parsing/dataloader.py:409-418
# asked: {"lines": [414, 415, 416, 417, 418], "branches": [[414, 0], [414, 415]]}
# gained: {"lines": [414, 415, 416, 417, 418], "branches": [[414, 0], [414, 415]]}

import pytest
from unittest import mock
from ansible.parsing.dataloader import DataLoader
from ansible.utils.display import Display

@pytest.fixture
def dataloader():
    loader = DataLoader()
    loader._tempfiles = ['/tmp/testfile1', '/tmp/testfile2']
    return loader

def test_cleanup_all_tmp_files_success(dataloader, monkeypatch):
    mock_cleanup_tmp_file = mock.Mock()
    monkeypatch.setattr(dataloader, 'cleanup_tmp_file', mock_cleanup_tmp_file)
    
    dataloader.cleanup_all_tmp_files()
    
    assert mock_cleanup_tmp_file.call_count == 2
    mock_cleanup_tmp_file.assert_any_call('/tmp/testfile1')
    mock_cleanup_tmp_file.assert_any_call('/tmp/testfile2')

def test_cleanup_all_tmp_files_exception(dataloader, monkeypatch):
    mock_cleanup_tmp_file = mock.Mock(side_effect=Exception("Test Exception"))
    mock_display_warning = mock.Mock()
    monkeypatch.setattr(dataloader, 'cleanup_tmp_file', mock_cleanup_tmp_file)
    monkeypatch.setattr(Display, 'warning', mock_display_warning)
    
    dataloader.cleanup_all_tmp_files()
    
    assert mock_cleanup_tmp_file.call_count == 2
    assert mock_display_warning.call_count == 2
    mock_display_warning.assert_any_call("Unable to cleanup temp files: Test Exception")
