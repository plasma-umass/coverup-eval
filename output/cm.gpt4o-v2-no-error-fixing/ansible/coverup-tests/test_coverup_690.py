# file: lib/ansible/parsing/dataloader.py:171-173
# asked: {"lines": [171, 173], "branches": []}
# gained: {"lines": [171, 173], "branches": []}

import pytest
from ansible.parsing.dataloader import DataLoader

def test_get_basedir():
    dl = DataLoader()
    assert dl.get_basedir() == '.'

def test_set_and_get_basedir():
    dl = DataLoader()
    new_basedir = '/new/basedir'
    dl.set_basedir(new_basedir)
    assert dl.get_basedir() == new_basedir
