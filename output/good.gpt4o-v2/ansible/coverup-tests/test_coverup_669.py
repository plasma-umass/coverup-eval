# file: lib/ansible/parsing/dataloader.py:175-179
# asked: {"lines": [175, 178, 179], "branches": [[178, 0], [178, 179]]}
# gained: {"lines": [175, 178, 179], "branches": [[178, 0], [178, 179]]}

import pytest
from ansible.parsing.dataloader import DataLoader
from ansible.module_utils._text import to_text

def test_set_basedir_with_none():
    loader = DataLoader()
    loader.set_basedir(None)
    assert loader._basedir == '.'

def test_set_basedir_with_value():
    loader = DataLoader()
    test_dir = '/test/directory'
    loader.set_basedir(test_dir)
    assert loader._basedir == to_text(test_dir)
