# file: lib/ansible/parsing/dataloader.py:171-173
# asked: {"lines": [171, 173], "branches": []}
# gained: {"lines": [171, 173], "branches": []}

import pytest
from ansible.parsing.dataloader import DataLoader

@pytest.fixture
def dataloader():
    return DataLoader()

def test_get_basedir(monkeypatch, dataloader):
    # Mock the _basedir attribute
    monkeypatch.setattr(dataloader, '_basedir', '/mock/basedir')
    
    # Call the method and assert the return value
    assert dataloader.get_basedir() == '/mock/basedir'
