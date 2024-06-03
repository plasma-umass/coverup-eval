# file sanic/helpers.py:142-157
# lines [142, 152, 153, 154, 155, 156, 157]
# branches ['155->156', '155->157']

import pytest
from sanic.helpers import import_string
from unittest.mock import patch, MagicMock
from types import ModuleType

def test_import_string_module():
    with patch('sanic.helpers.import_module') as mock_import_module:
        mock_module = ModuleType('some_module')
        mock_import_module.return_value = mock_module
        mock_module.some_module = ModuleType('some_module.some_module')
        
        result = import_string('some_module.some_module')
        
        mock_import_module.assert_called_once_with('some_module', package=None)
        assert result == mock_module.some_module

def test_import_string_class():
    with patch('sanic.helpers.import_module') as mock_import_module:
        mock_module = ModuleType('some_module')
        mock_import_module.return_value = mock_module
        mock_class = MagicMock()
        mock_module.SomeClass = mock_class
        
        result = import_string('some_module.SomeClass')
        
        mock_import_module.assert_called_once_with('some_module', package=None)
        mock_class.assert_called_once()
        assert result == mock_class.return_value
