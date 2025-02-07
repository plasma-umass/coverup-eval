# file: apimd/parser.py:518-526
# asked: {"lines": [520, 521, 522, 523, 524, 525, 526], "branches": [[520, 0], [520, 521], [521, 522], [521, 523], [525, 520], [525, 526]]}
# gained: {"lines": [520, 521, 522, 523, 524, 525, 526], "branches": [[520, 0], [520, 521], [521, 522], [521, 523], [525, 526]]}

import pytest
from types import ModuleType
from unittest.mock import Mock
from apimd.parser import Parser

def _attr(module, attr):
    """Mock function to simulate attribute fetching from a module."""
    return getattr(module, attr, None)

def doctest(doc):
    """Mock function to simulate doctest processing."""
    return doc

@pytest.fixture
def mock_module():
    """Fixture to create a mock module with docstrings."""
    module = Mock(spec=ModuleType)
    module.func = Mock(__doc__="Function docstring")
    module.cls = Mock(__doc__="Class docstring")
    return module

def test_load_docstring_executes_all_lines(mock_module, monkeypatch):
    parser = Parser()
    parser.doc = {
        'root.func': 'Function docstring',
        'root.cls': 'Class docstring',
        'other.func': 'Other function docstring'
    }
    parser.docstring = {}

    monkeypatch.setattr('apimd.parser._attr', _attr)
    monkeypatch.setattr('apimd.parser.doctest', doctest)

    parser.load_docstring('root', mock_module)

    assert 'root.func' in parser.docstring
    assert parser.docstring['root.func'] == 'Function docstring'
    assert 'root.cls' in parser.docstring
    assert parser.docstring['root.cls'] == 'Class docstring'
    assert 'other.func' not in parser.docstring
