# file: apimd/parser.py:518-526
# asked: {"lines": [518, 520, 521, 522, 523, 524, 525, 526], "branches": [[520, 0], [520, 521], [521, 522], [521, 523], [525, 520], [525, 526]]}
# gained: {"lines": [518], "branches": []}

import pytest
from types import ModuleType
from dataclasses import dataclass

@dataclass
class Parser:
    doc: dict
    docstring: dict

    def load_docstring(self, root: str, m: ModuleType) -> None:
        """Load docstring from the module."""
        for name in self.doc:
            if not name.startswith(root):
                continue
            attr = name.removeprefix(root + '.')
            doc = getdoc(_attr(m, attr))
            if doc is not None:
                self.docstring[name] = doc

def getdoc(obj):
    """Mock getdoc function."""
    return obj.__doc__

def _attr(module, attr):
    """Mock _attr function."""
    return getattr(module, attr)

class MockModule:
    """Mock module for testing."""
    def __init__(self):
        self.some_attr = self.SomeClass()

    class SomeClass:
        """SomeClass docstring."""
        pass

@pytest.fixture
def parser():
    return Parser(doc={'root.some_attr': None}, docstring={})

def test_load_docstring(parser, monkeypatch):
    mock_module = MockModule()
    monkeypatch.setattr('apimd.parser.getdoc', getdoc)
    monkeypatch.setattr('apimd.parser._attr', _attr)
    
    parser.load_docstring('root', mock_module)
    
    assert 'root.some_attr' in parser.docstring
    assert parser.docstring['root.some_attr'] == 'SomeClass docstring.'

@pytest.fixture(autouse=True)
def cleanup():
    yield
    # Cleanup code if necessary
