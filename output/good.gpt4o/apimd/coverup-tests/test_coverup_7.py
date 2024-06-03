# file apimd/parser.py:518-526
# lines [518, 520, 521, 522, 523, 524, 525, 526]
# branches ['520->exit', '520->521', '521->522', '521->523', '525->520', '525->526']

import pytest
from types import ModuleType
from unittest.mock import Mock, patch
from dataclasses import dataclass

# Assuming the Parser class is defined in apimd.parser
from apimd.parser import Parser

@dataclass
class MockModule:
    __name__: str = "mock_module"
    def mock_function(self):
        """This is a mock function docstring."""
        pass

@pytest.fixture
def mock_module():
    return MockModule()

@pytest.fixture
def parser():
    return Parser(doc={"mock_module.mock_function": None}, docstring={})

def test_load_docstring(parser, mock_module):
    with patch('apimd.parser.getdoc', return_value="This is a mock function docstring."), \
         patch('apimd.parser._attr', return_value=mock_module.mock_function):
        parser.load_docstring("mock_module", mock_module)
        assert "mock_module.mock_function" in parser.docstring
        assert parser.docstring["mock_module.mock_function"] == "This is a mock function docstring."
