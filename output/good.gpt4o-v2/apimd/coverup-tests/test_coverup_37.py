# file: apimd/parser.py:182-195
# asked: {"lines": [], "branches": [[192, 195]]}
# gained: {"lines": [], "branches": [[192, 195]]}

import pytest
from ast import Call, Name, Load
from apimd.parser import const_type

def test_const_type_with_pep585_key(monkeypatch):
    class MockPEP585:
        @staticmethod
        def keys():
            return {'list'}

        @staticmethod
        def values():
            return {'List'}

    monkeypatch.setattr('apimd.parser.PEP585', MockPEP585)

    node = Call(func=Name(id='list', ctx=Load()), args=[], keywords=[])
    assert const_type(node) == 'list'

def test_const_type_with_pep585_value(monkeypatch):
    class MockPEP585:
        @staticmethod
        def keys():
            return {'list'}

        @staticmethod
        def values():
            return {'List'}

    monkeypatch.setattr('apimd.parser.PEP585', MockPEP585)

    node = Call(func=Name(id='List', ctx=Load()), args=[], keywords=[])
    assert const_type(node) == 'List'

def test_const_type_with_non_pep585_function():
    node = Call(func=Name(id='non_pep585_func', ctx=Load()), args=[], keywords=[])
    assert const_type(node) == 'Any'
