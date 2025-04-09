# file src/blib2to3/pgen2/grammar.py:115-117
# lines [115, 116, 117]
# branches ['116->exit', '116->117']

import pytest
from blib2to3.pgen2.grammar import Grammar

def test_grammar_update():
    grammar = Grammar()
    attrs_to_update = {
        'attr1': 'value1',
        'attr2': 'value2',
        'attr3': 42
    }
    grammar._update(attrs_to_update)
    
    # Assertions to verify postconditions
    assert grammar.attr1 == 'value1'
    assert grammar.attr2 == 'value2'
    assert grammar.attr3 == 42
