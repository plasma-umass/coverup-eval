# file: apimd/parser.py:326-339
# asked: {"lines": [326, 328, 329, 330, 331, 332, 333, 334, 336, 337, 338, 339], "branches": [[328, 329], [328, 332], [329, 0], [329, 330], [332, 0], [332, 333], [333, 334], [333, 336], [337, 0], [337, 338]]}
# gained: {"lines": [326], "branches": []}

import pytest
from unittest.mock import MagicMock
from dataclasses import dataclass

@dataclass
class Import:
    names: list

@dataclass
class ImportFrom:
    module: str
    level: int
    names: list

@dataclass
class Alias:
    name: str
    asname: str = None

@dataclass
class Parser:
    alias: dict

    def imports(self, root: str, node) -> None:
        """Save import names."""
        if isinstance(node, Import):
            for a in node.names:
                name = a.name if a.asname is None else a.asname
                self.alias[_m(root, name)] = a.name
        elif node.module is not None:
            if node.level:
                m = parent(root, level=node.level - 1)
            else:
                m = ''
            for a in node.names:
                name = a.name if a.asname is None else a.asname
                self.alias[_m(root, name)] = _m(m, node.module, a.name)

def _m(*args):
    return '.'.join(arg for arg in args if arg)

def parent(root, level):
    return 'parent_module'

@pytest.fixture
def parser():
    return Parser(alias={})

def test_imports_with_import(parser):
    node = Import(names=[Alias(name='os'), Alias(name='sys', asname='system')])
    parser.imports('root', node)
    assert parser.alias == {'root.os': 'os', 'root.system': 'sys'}

def test_imports_with_importfrom_level(parser, monkeypatch):
    node = ImportFrom(module='submodule', level=2, names=[Alias(name='func')])
    monkeypatch.setattr('apimd.parser.parent', lambda root, level: 'parent_module')
    parser.imports('root', node)
    assert parser.alias == {'root.func': 'parent_module.submodule.func'}

def test_imports_with_importfrom_no_level(parser):
    node = ImportFrom(module='submodule', level=0, names=[Alias(name='func', asname='function')])
    parser.imports('root', node)
    assert parser.alias == {'root.function': 'submodule.func'}
