# file: src/blib2to3/pygram.py:157-197
# asked: {"lines": [157, 167, 168, 169, 173, 175, 178, 179, 182, 183, 184, 187, 188, 190, 191, 194, 195, 197], "branches": []}
# gained: {"lines": [157, 167, 168, 169, 173, 175, 178, 179, 182, 183, 184, 187, 188, 190, 191, 194, 195, 197], "branches": []}

import os
import pytest
from unittest import mock
from blib2to3 import pygram
from blib2to3.pgen2 import driver
from blib2to3.pgen2.grammar import Grammar

@pytest.fixture
def mock_load_packaged_grammar(monkeypatch):
    def mock_load(package, grammar_source, cache_dir=None):
        grammar = Grammar()
        grammar.keywords = {"print": "print", "exec": "exec"}
        return grammar
    monkeypatch.setattr(driver, 'load_packaged_grammar', mock_load)

@pytest.fixture
def mock_python_symbols(monkeypatch):
    def mock_symbols(grammar):
        return mock.Mock()
    monkeypatch.setattr(pygram, '_python_symbols', mock_symbols)

@pytest.fixture
def mock_pattern_symbols(monkeypatch):
    def mock_symbols(grammar):
        return mock.Mock()
    monkeypatch.setattr(pygram, '_pattern_symbols', mock_symbols)

def test_initialize_all_branches(mock_load_packaged_grammar, mock_python_symbols, mock_pattern_symbols):
    cache_dir = "/tmp/test_cache"
    
    pygram.initialize(cache_dir)
    
    assert pygram.python_grammar is not None
    assert pygram.python_grammar_no_print_statement is not None
    assert pygram.python_grammar_no_print_statement_no_exec_statement is not None
    assert pygram.python_grammar_no_print_statement_no_exec_statement_async_keywords is not None
    assert pygram.python_symbols is not None
    assert pygram.pattern_grammar is not None
    assert pygram.pattern_symbols is not None

    assert "print" not in pygram.python_grammar_no_print_statement.keywords
    assert "print" not in pygram.python_grammar_no_print_statement_no_exec_statement.keywords
    assert "exec" not in pygram.python_grammar_no_print_statement_no_exec_statement.keywords
    assert pygram.python_grammar_no_print_statement_no_exec_statement_async_keywords.async_keywords is True
