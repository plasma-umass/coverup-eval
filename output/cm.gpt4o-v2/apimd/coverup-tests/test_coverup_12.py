# file: apimd/parser.py:326-339
# asked: {"lines": [326, 328, 329, 330, 331, 332, 333, 334, 336, 337, 338, 339], "branches": [[328, 329], [328, 332], [329, 0], [329, 330], [332, 0], [332, 333], [333, 334], [333, 336], [337, 0], [337, 338]]}
# gained: {"lines": [326, 328, 329, 330, 331, 332, 333, 334, 336, 337, 338, 339], "branches": [[328, 329], [328, 332], [329, 0], [329, 330], [332, 333], [333, 334], [333, 336], [337, 0], [337, 338]]}

import pytest
from ast import Import, ImportFrom, alias
from apimd.parser import Parser, _m, parent

@pytest.fixture
def parser():
    return Parser(alias={})

def test_imports_import(parser):
    node = Import(names=[alias(name='module1', asname=None), alias(name='module2', asname='mod2')])
    parser.imports('root', node)
    assert parser.alias == {'root.module1': 'module1', 'root.mod2': 'module2'}

def test_imports_importfrom_with_level(parser, mocker):
    mocker.patch('apimd.parser.parent', return_value='parent_module')
    node = ImportFrom(module='module', names=[alias(name='name1', asname=None), alias(name='name2', asname='n2')], level=2)
    parser.imports('root', node)
    assert parser.alias == {'root.name1': 'parent_module.module.name1', 'root.n2': 'parent_module.module.name2'}

def test_imports_importfrom_without_level(parser):
    node = ImportFrom(module='module', names=[alias(name='name1', asname=None), alias(name='name2', asname='n2')], level=0)
    parser.imports('root', node)
    assert parser.alias == {'root.name1': 'module.name1', 'root.n2': 'module.name2'}
