# file: src/blib2to3/pgen2/grammar.py:115-117
# asked: {"lines": [115, 116, 117], "branches": [[116, 0], [116, 117]]}
# gained: {"lines": [115, 116, 117], "branches": [[116, 0], [116, 117]]}

import pytest
from blib2to3.pgen2.grammar import Grammar

@pytest.fixture
def grammar():
    return Grammar()

def test_update_method(grammar):
    attrs = {'attr1': 'value1', 'attr2': 'value2'}
    grammar._update(attrs)
    
    assert grammar.attr1 == 'value1'
    assert grammar.attr2 == 'value2'
