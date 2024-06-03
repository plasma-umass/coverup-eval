# file apimd/parser.py:326-339
# lines [328, 329, 330, 331, 332, 333, 334, 336, 337, 338, 339]
# branches ['328->329', '328->332', '329->exit', '329->330', '332->exit', '332->333', '333->334', '333->336', '337->exit', '337->338']

import pytest
from unittest.mock import Mock
from dataclasses import dataclass

# Assuming _I, Import, and other dependencies are defined elsewhere in apimd.parser
from apimd.parser import Parser, _I, Import, _m, parent

@dataclass
class MockAlias:
    alias: dict

@pytest.fixture
def parser():
    return Parser(link=True, b_level=1, toc=False, level={}, doc={}, docstring={}, imp={}, root={}, alias={}, const={})

def test_imports_with_import_node(parser):
    # Mocking an Import node
    import_node = Mock(spec=Import)
    import_node.names = [Mock(name='a', asname=None), Mock(name='b', asname='b_alias')]
    import_node.names[0].name = 'a'
    import_node.names[1].name = 'b'
    
    parser.imports('root', import_node)
    
    assert parser.alias == {
        _m('root', 'a'): 'a',
        _m('root', 'b_alias'): 'b'
    }

def test_imports_with_module_node(parser, mocker):
    # Mocking a node with module and level
    node = Mock()
    node.module = 'module'
    node.level = 1
    node.names = [Mock(name='a', asname=None), Mock(name='b', asname='b_alias')]
    node.names[0].name = 'a'
    node.names[1].name = 'b'
    
    mocker.patch('apimd.parser.parent', return_value='parent')
    
    parser.imports('root', node)
    
    assert parser.alias == {
        _m('root', 'a'): _m('parent', 'module', 'a'),
        _m('root', 'b_alias'): _m('parent', 'module', 'b')
    }

def test_imports_with_module_node_no_level(parser):
    # Mocking a node with module and no level
    node = Mock()
    node.module = 'module'
    node.level = 0
    node.names = [Mock(name='a', asname=None), Mock(name='b', asname='b_alias')]
    node.names[0].name = 'a'
    node.names[1].name = 'b'
    
    parser.imports('root', node)
    
    assert parser.alias == {
        _m('root', 'a'): _m('', 'module', 'a'),
        _m('root', 'b_alias'): _m('', 'module', 'b')
    }
