# file lib/ansible/parsing/dataloader.py:171-173
# lines [171, 173]
# branches []

import pytest
from unittest.mock import patch

# Assuming the DataLoader class is imported from ansible.parsing.dataloader
from ansible.parsing.dataloader import DataLoader

class MockDataLoader(DataLoader):
    def __init__(self, basedir):
        self._basedir = basedir

@pytest.fixture
def dataloader():
    return MockDataLoader('/mock/basedir')

def test_get_basedir(dataloader):
    assert dataloader.get_basedir() == '/mock/basedir'
