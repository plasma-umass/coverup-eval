# file apimd/parser.py:341-379
# lines [368]
# branches ['356->368', '373->375']

import pytest
from apimd.parser import Parser
from ast import parse, Assign, Name, Constant, AnnAssign, Tuple, List

@pytest.fixture
def parser():
    return Parser(link=True, b_level=1, toc=False, level={}, doc={}, docstring={}, imp={}, root={}, alias={}, const={})

def test_parser_globals_assign_without_type_comment(parser, mocker):
    # Mock the unparse function to return a dummy expression
    mocker.patch('apimd.parser.unparse', return_value='dummy_expression')
    # Mock the const_type function to return a dummy annotation
    mocker.patch('apimd.parser.const_type', return_value='dummy_annotation')
    
    # Create an AST node for testing
    node = Assign(
        targets=[Name(id='SOME_CONSTANT', ctx=None)],
        value=Constant(value=42),
        type_comment=None
    )
    
    # Call the globals method with the test node
    parser.globals('root', node)
    
    # Assert that the alias and root have been set correctly
    assert parser.alias['root.SOME_CONSTANT'] == 'dummy_expression'
    assert parser.root['root.SOME_CONSTANT'] == 'root'
    # Assert that the const has been set correctly
    assert parser.const['root.SOME_CONSTANT'] == 'dummy_annotation'

def test_parser_globals_assign_with_type_comment(parser, mocker):
    # Mock the unparse function to return a dummy expression
    mocker.patch('apimd.parser.unparse', return_value='dummy_expression')
    
    # Create an AST node for testing
    node = Assign(
        targets=[Name(id='SOME_CONSTANT', ctx=None)],
        value=Constant(value=42),
        type_comment='int'
    )
    
    # Call the globals method with the test node
    parser.globals('root', node)
    
    # Assert that the alias and root have been set correctly
    assert parser.alias['root.SOME_CONSTANT'] == 'dummy_expression'
    assert parser.root['root.SOME_CONSTANT'] == 'root'
    # Assert that the const has been set correctly
    assert parser.const['root.SOME_CONSTANT'] == 'int'

def test_parser_globals_assign_with_non_constant(parser, mocker):
    # Mock the unparse function to return a dummy expression
    mocker.patch('apimd.parser.unparse', return_value='dummy_expression')
    # Mock the const_type function to return a dummy annotation
    mocker.patch('apimd.parser.const_type', return_value='dummy_annotation')
    
    # Create an AST node for testing
    node = Assign(
        targets=[Name(id='not_a_constant', ctx=None)],
        value=Constant(value=42),
        type_comment=None
    )
    
    # Call the globals method with the test node
    parser.globals('root', node)
    
    # Assert that the alias has been set correctly
    assert parser.alias['root.not_a_constant'] == 'dummy_expression'
    # Assert that the root has not been set for non-constants
    assert 'root.not_a_constant' not in parser.root
    # Assert that the const has not been set for non-constants
    assert 'root.not_a_constant' not in parser.const

def test_parser_globals_assign_with_non_name_target(parser, mocker):
    # Mock the unparse function to return a dummy expression
    mocker.patch('apimd.parser.unparse', return_value='dummy_expression')
    
    # Create an AST node for testing with a non-Name target
    node = Assign(
        targets=[Constant(value=42)],
        value=Constant(value=42),
        type_comment=None
    )
    
    # Call the globals method with the test node
    parser.globals('root', node)
    
    # Assert that no alias, root, or const has been set for non-Name target
    assert parser.alias == {}
    assert parser.root == {}
    assert parser.const == {}

def test_parser_globals_assign_with_multiple_targets(parser, mocker):
    # Mock the unparse function to return a dummy expression
    mocker.patch('apimd.parser.unparse', return_value='dummy_expression')
    
    # Create an AST node for testing with multiple targets
    node = Assign(
        targets=[Name(id='SOME_CONSTANT', ctx=None), Name(id='ANOTHER_CONSTANT', ctx=None)],
        value=Constant(value=42),
        type_comment=None
    )
    
    # Call the globals method with the test node
    parser.globals('root', node)
    
    # Assert that no alias, root, or const has been set for multiple targets
    assert parser.alias == {}
    assert parser.root == {}
    assert parser.const == {}
