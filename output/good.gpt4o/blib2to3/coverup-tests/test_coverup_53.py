# file src/blib2to3/pgen2/parse.py:219-224
# lines [219, 221, 222, 223, 224]
# branches []

import pytest
from blib2to3.pgen2.parse import Parser, Context
from blib2to3.pgen2.grammar import Grammar

class MockDFAS:
    pass

class MockContext:
    pass

@pytest.fixture
def parser():
    grammar = Grammar()
    return Parser(grammar)

def test_push(parser):
    # Setup initial state
    initial_dfa = MockDFAS()
    initial_state = 0
    initial_node = (0, None, MockContext(), [])
    parser.stack = [(initial_dfa, initial_state, initial_node)]

    # New DFA and state to push
    new_dfa = MockDFAS()
    new_state = 1
    new_type = 1
    new_context = MockContext()

    # Call the method
    parser.push(new_type, new_dfa, new_state, new_context)

    # Assertions to verify the postconditions
    assert len(parser.stack) == 2
    assert parser.stack[0] == (initial_dfa, new_state, initial_node)
    assert parser.stack[1] == (new_dfa, 0, (new_type, None, new_context, []))
