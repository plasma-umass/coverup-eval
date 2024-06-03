# file src/blib2to3/pgen2/grammar.py:115-117
# lines [115, 116, 117]
# branches ['116->exit', '116->117']

import pytest
from blib2to3.pgen2.grammar import Grammar

def test_grammar_update():
    grammar = Grammar()
    attrs = {'attr1': 'value1', 'attr2': 42, 'attr3': [1, 2, 3]}
    
    grammar._update(attrs)
    
    assert grammar.attr1 == 'value1'
    assert grammar.attr2 == 42
    assert grammar.attr3 == [1, 2, 3]
    
    # Clean up
    del grammar.attr1
    del grammar.attr2
    del grammar.attr3
