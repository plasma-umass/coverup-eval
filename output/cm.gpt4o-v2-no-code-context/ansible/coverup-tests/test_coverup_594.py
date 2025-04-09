# file: lib/ansible/parsing/dataloader.py:175-179
# asked: {"lines": [175, 178, 179], "branches": [[178, 0], [178, 179]]}
# gained: {"lines": [175, 178, 179], "branches": [[178, 0], [178, 179]]}

import pytest
from ansible.parsing.dataloader import DataLoader
from ansible.module_utils._text import to_text

@pytest.fixture
def dataloader():
    return DataLoader()

def test_set_basedir_none(dataloader):
    dataloader.set_basedir(None)
    assert dataloader._basedir == '.'

def test_set_basedir_non_none(dataloader):
    basedir = '/some/path'
    dataloader.set_basedir(basedir)
    assert dataloader._basedir == to_text(basedir)
