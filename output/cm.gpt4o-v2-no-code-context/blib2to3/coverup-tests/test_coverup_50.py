# file: src/blib2to3/pgen2/pgen.py:29-30
# asked: {"lines": [29, 30], "branches": []}
# gained: {"lines": [29, 30], "branches": []}

import pytest
from blib2to3.pgen2 import pgen
from blib2to3.pgen2 import grammar

def test_pgen_grammar_class():
    # Ensure that PgenGrammar is a subclass of grammar.Grammar
    assert issubclass(pgen.PgenGrammar, grammar.Grammar)

    # Ensure that an instance of PgenGrammar can be created
    instance = pgen.PgenGrammar()
    assert isinstance(instance, pgen.PgenGrammar)
    assert isinstance(instance, grammar.Grammar)
