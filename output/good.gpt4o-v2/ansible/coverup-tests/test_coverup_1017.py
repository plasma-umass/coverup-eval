# file: lib/ansible/parsing/dataloader.py:171-173
# asked: {"lines": [171, 173], "branches": []}
# gained: {"lines": [171, 173], "branches": []}

import pytest
from ansible.parsing.dataloader import DataLoader

def test_get_basedir():
    dl = DataLoader()
    assert dl.get_basedir() == '.', "The default basedir should be '.'"

    dl.set_basedir('/new/basedir')
    assert dl.get_basedir() == '/new/basedir', "The basedir should be '/new/basedir' after setting it"

    # Clean up by resetting the basedir to its default value
    dl.set_basedir('.')
    assert dl.get_basedir() == '.', "The basedir should be reset to '.'"

@pytest.fixture
def dataloader():
    dl = DataLoader()
    yield dl
    # Clean up by resetting the basedir to its default value
    dl.set_basedir('.')

def test_get_basedir_with_fixture(dataloader):
    assert dataloader.get_basedir() == '.', "The default basedir should be '.'"

    dataloader.set_basedir('/another/basedir')
    assert dataloader.get_basedir() == '/another/basedir', "The basedir should be '/another/basedir' after setting it"
