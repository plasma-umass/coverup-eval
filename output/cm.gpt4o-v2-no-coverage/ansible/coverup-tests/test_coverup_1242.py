# file: lib/ansible/parsing/dataloader.py:171-173
# asked: {"lines": [173], "branches": []}
# gained: {"lines": [173], "branches": []}

import pytest
from ansible.parsing.dataloader import DataLoader

def test_get_basedir():
    dl = DataLoader()
    assert dl.get_basedir() == '.', "The default basedir should be '.'"

    dl.set_basedir('/new/basedir')
    assert dl.get_basedir() == '/new/basedir', "The basedir should be '/new/basedir' after setting it"

    # Clean up by resetting the basedir to the default
    dl.set_basedir('.')
    assert dl.get_basedir() == '.', "The basedir should be reset to '.'"
