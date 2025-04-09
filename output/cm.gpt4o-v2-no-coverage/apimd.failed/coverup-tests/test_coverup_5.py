# file: apimd/parser.py:62-71
# asked: {"lines": [62, 64, 66, 67, 69, 70, 71], "branches": [[64, 66], [64, 71], [66, 67], [66, 69], [69, 64], [69, 70]]}
# gained: {"lines": [62, 64, 66, 67, 69, 70, 71], "branches": [[64, 66], [64, 71], [66, 67], [66, 69], [69, 64], [69, 70]]}

import pytest
from apimd.parser import is_public_family

def test_is_public_family_with_magic_name(monkeypatch):
    def mock_is_magic(name):
        return name == '__magic__'
    
    monkeypatch.setattr('apimd.parser.is_magic', mock_is_magic)
    
    assert is_public_family('__magic__.module') == True

def test_is_public_family_with_private_name(monkeypatch):
    def mock_is_magic(name):
        return False
    
    monkeypatch.setattr('apimd.parser.is_magic', mock_is_magic)
    
    assert is_public_family('_private.module') == False

def test_is_public_family_with_public_name(monkeypatch):
    def mock_is_magic(name):
        return False
    
    monkeypatch.setattr('apimd.parser.is_magic', mock_is_magic)
    
    assert is_public_family('public.module') == True
