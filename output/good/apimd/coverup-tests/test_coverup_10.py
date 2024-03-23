# file apimd/parser.py:518-526
# lines [518, 520, 521, 522, 523, 524, 525, 526]
# branches ['520->exit', '520->521', '521->522', '521->523', '525->520', '525->526']

import pytest
from apimd.parser import Parser
from types import ModuleType
from inspect import getdoc

def _attr(module, attribute):
    """Mock helper function to mimic attribute retrieval from a module."""
    return getattr(module, attribute, None)

def doctest(docstring):
    """Mock helper function to mimic doctest parsing."""
    return f"Tested {docstring}"

@pytest.fixture
def mock_module(mocker):
    """Create a mock module with a docstring."""
    mock_mod = ModuleType('mock_module')
    mock_mod.__doc__ = "Module docstring"
    mock_mod.sub_attr = "Sub attribute"
    mocker.patch('apimd.parser.getdoc', return_value="Mocked docstring")
    mocker.patch('apimd.parser._attr', side_effect=lambda m, a: _attr(mock_mod, a))
    mocker.patch('apimd.parser.doctest', side_effect=doctest)
    return mock_mod

def test_load_docstring_with_root_prefix(mock_module):
    parser = Parser()
    parser.doc = {'mock_module': '', 'mock_module.sub_attr': ''}
    parser.docstring = {}
    parser.load_docstring('mock_module', mock_module)
    assert parser.docstring == {
        'mock_module': 'Tested Mocked docstring',
        'mock_module.sub_attr': 'Tested Mocked docstring'
    }
