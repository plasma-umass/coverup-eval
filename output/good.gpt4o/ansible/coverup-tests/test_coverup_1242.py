# file lib/ansible/parsing/dataloader.py:175-179
# lines [178, 179]
# branches ['178->exit', '178->179']

import pytest
from ansible.parsing.dataloader import DataLoader
from ansible.module_utils._text import to_text

@pytest.fixture
def dataloader():
    return DataLoader()

def test_set_basedir_with_none(dataloader):
    original_basedir = getattr(dataloader, '_basedir', None)
    dataloader.set_basedir(None)
    assert dataloader._basedir == original_basedir

def test_set_basedir_with_value(dataloader, mocker):
    basedir = '/some/path'
    mock_to_text = mocker.patch('ansible.parsing.dataloader.to_text', return_value=basedir)
    dataloader.set_basedir(basedir)
    mock_to_text.assert_called_once_with(basedir)
    assert dataloader._basedir == basedir
