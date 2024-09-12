# file: src/blib2to3/pgen2/tokenize.py:66-67
# asked: {"lines": [66, 67], "branches": []}
# gained: {"lines": [66, 67], "branches": []}

import pytest
from blib2to3.pgen2.tokenize import group

def test_any_with_single_choice(monkeypatch):
    from blib2to3.pgen2.tokenize import any as any_func

    def mock_group(*choices):
        return ''.join(choices)

    monkeypatch.setattr('blib2to3.pgen2.tokenize.group', mock_group)

    result = any_func('a')
    assert result == 'a*'

def test_any_with_multiple_choices(monkeypatch):
    from blib2to3.pgen2.tokenize import any as any_func

    def mock_group(*choices):
        return ''.join(choices)

    monkeypatch.setattr('blib2to3.pgen2.tokenize.group', mock_group)

    result = any_func('a', 'b', 'c')
    assert result == 'abc*'
