# file apimd/parser.py:341-379
# lines [368]
# branches ['356->368', '373->375', '378->377']

import pytest
from apimd.parser import Parser
from ast import parse, Assign, Name, Constant, AnnAssign, Tuple, List

@pytest.fixture
def parser():
    return Parser()

def test_parser_globals_assign_non_constant_to_all(parser, mocker):
    # Mock the unparse function to return a dummy string
    mocker.patch("apimd.parser.unparse", return_value="dummy_expression")
    # Mock the const_type function to return a dummy type
    mocker.patch("apimd.parser.const_type", return_value="dummy_type")

    # Create a node that represents `SOME_VAR = 'value'` which should trigger line 368
    node = Assign(
        targets=[Name(id='SOME_VAR', ctx=None)],
        value=Constant(value='value'),
        type_comment=None
    )

    # Set up the initial state of the parser
    parser.alias = {}
    parser.root = {}
    parser.const = {}
    parser.imp = {'root': set()}

    # Call the method under test
    parser.globals('root', node)

    # Check postconditions for line 368
    assert parser.alias == {'root.SOME_VAR': 'dummy_expression'}
    assert parser.root == {'root.SOME_VAR': 'root'}
    assert parser.const == {'root.SOME_VAR': 'dummy_type'}
    assert parser.imp == {'root': set()}

    # Create a node that represents `__all__ = ['MODULE1', SOME_VAR]`
    # SOME_VAR is not a constant, so it should not be added to parser.imp
    node = Assign(
        targets=[Name(id='__all__', ctx=None)],
        value=List(elts=[Constant(value='MODULE1'), Name(id='SOME_VAR')], ctx=None),
        type_comment=None
    )

    # Call the method under test
    parser.globals('root', node)

    # Check postconditions for branches 373->375, 378->377
    assert parser.alias == {'root.__all__': 'dummy_expression', 'root.SOME_VAR': 'dummy_expression'}
    assert parser.root == {'root.SOME_VAR': 'root'}
    assert parser.const == {'root.SOME_VAR': 'dummy_type'}
    assert parser.imp == {'root': {'root.MODULE1'}}

    # Clean up the patches
    mocker.stopall()
