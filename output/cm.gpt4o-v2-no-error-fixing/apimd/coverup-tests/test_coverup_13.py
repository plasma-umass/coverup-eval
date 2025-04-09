# file: apimd/parser.py:326-339
# asked: {"lines": [326, 328, 329, 330, 331, 332, 333, 334, 336, 337, 338, 339], "branches": [[328, 329], [328, 332], [329, 0], [329, 330], [332, 0], [332, 333], [333, 334], [333, 336], [337, 0], [337, 338]]}
# gained: {"lines": [326, 328, 329, 330, 331, 332, 333, 334, 336, 337, 338, 339], "branches": [[328, 329], [328, 332], [329, 0], [329, 330], [332, 333], [333, 334], [333, 336], [337, 0], [337, 338]]}

import pytest
from ast import Import, ImportFrom, alias
from apimd.parser import Parser, _m, parent

@pytest.fixture
def parser():
    return Parser()

def test_imports_import_node(parser):
    node = Import(names=[alias(name='os', asname=None)])
    parser.imports('root', node)
    assert parser.alias[_m('root', 'os')] == 'os'

def test_imports_importfrom_node_with_module_and_level(parser):
    node = ImportFrom(module='sys', names=[alias(name='path', asname=None)], level=1)
    parser.imports('root', node)
    assert parser.alias[_m('root', 'path')] == _m(parent('root', level=0), 'sys', 'path')

def test_imports_importfrom_node_with_module_no_level(parser):
    node = ImportFrom(module='sys', names=[alias(name='path', asname=None)], level=0)
    parser.imports('root', node)
    assert parser.alias[_m('root', 'path')] == _m('', 'sys', 'path')

def test_imports_importfrom_node_with_asname(parser):
    node = ImportFrom(module='sys', names=[alias(name='path', asname='p')], level=0)
    parser.imports('root', node)
    assert parser.alias[_m('root', 'p')] == _m('', 'sys', 'path')
