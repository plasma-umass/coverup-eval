# file: apimd/parser.py:518-526
# asked: {"lines": [518, 520, 521, 522, 523, 524, 525, 526], "branches": [[520, 0], [520, 521], [521, 522], [521, 523], [525, 520], [525, 526]]}
# gained: {"lines": [518, 520, 521, 523, 524, 525, 526], "branches": [[520, 0], [520, 521], [521, 523], [525, 526]]}

import pytest
from types import ModuleType
from unittest.mock import Mock, patch
from apimd.parser import Parser

def _attr(module, attr):
    return getattr(module, attr)

def doctest(doc):
    return doc

@pytest.fixture
def mock_module():
    module = Mock(spec=ModuleType)
    module.some_function = Mock(__doc__="This is a test function.")
    return module

def test_load_docstring(mock_module):
    parser = Parser()
    parser.doc = {"root.some_function": "some doc"}
    parser.docstring = {}

    with patch('apimd.parser._attr', side_effect=_attr):
        with patch('apimd.parser.doctest', side_effect=doctest):
            parser.load_docstring("root", mock_module)

    assert parser.docstring == {"root.some_function": "This is a test function."}
