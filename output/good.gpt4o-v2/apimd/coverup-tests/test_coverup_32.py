# file: apimd/parser.py:532-548
# asked: {"lines": [534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548], "branches": [[534, 0], [534, 535], [535, 536], [535, 537], [537, 534], [537, 538], [538, 539], [538, 540], [547, 537], [547, 548]]}
# gained: {"lines": [534, 535, 537, 538, 540, 541, 542, 543, 544, 545, 546, 547, 548], "branches": [[534, 0], [534, 535], [535, 537], [537, 534], [537, 538], [538, 540], [547, 548]]}

import pytest
from apimd.parser import Parser

@pytest.fixture
def parser():
    return Parser()

def test_find_alias(parser, mocker):
    # Setup the parser state
    parser.alias = {'alias1': 'doc1'}
    parser.doc = {'doc1': 'some documentation'}
    parser.docstring = {'doc1': 'some docstring'}
    parser.root = {'doc1': 'alias1'}
    parser.level = {'doc1': 0}
    parser.const = {'doc1': 'const1'}

    # Mock the __is_immediate_family method to return True
    mocker.patch.object(parser, '_Parser__is_immediate_family', return_value=True)

    # Call the method
    parser._Parser__find_alias()

    # Assertions to verify the state changes
    assert 'alias1' in parser.doc
    assert parser.doc['alias1'] == 'some documentation'
    assert 'doc1' not in parser.doc

    assert 'alias1' in parser.docstring
    assert parser.docstring['alias1'] == 'some docstring'
    assert 'doc1' not in parser.docstring

    assert 'alias1' in parser.root
    assert parser.root['alias1'] == 'alias1'
    assert 'doc1' not in parser.root

    assert 'alias1' in parser.level
    assert parser.level['alias1'] == 0
    assert 'doc1' not in parser.level

    assert 'alias1' in parser.const
    assert parser.const['alias1'] == 'const1'
    assert 'doc1' not in parser.const
