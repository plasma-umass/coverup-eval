# file sanic/helpers.py:142-157
# lines [152, 153, 154, 155, 156, 157]
# branches ['155->156', '155->157']

import pytest
from unittest.mock import MagicMock, patch
from sanic.helpers import import_string
from types import ModuleType

@pytest.fixture
def mock_import_module(mocker):
    mock = mocker.patch('sanic.helpers.import_module', autospec=True)
    return mock

def test_import_string_module(mock_import_module):
    # Mock the import_module to return a new module (mimicking a real module)
    mock_module = ModuleType('mock_module')
    mock_import_module.return_value = mock_module

    # Mock a module object to be returned by getattr
    mock_module_obj = ModuleType('MockModule')
    setattr(mock_module, 'MockModule', mock_module_obj)

    # Test importing a module
    result = import_string('mock_module.MockModule')
    assert result == mock_module_obj
    mock_import_module.assert_called_once_with('mock_module', package=None)

def test_import_string_class(mock_import_module):
    # Mock the import_module to return a new module (mimicking a real module)
    mock_module = ModuleType('mock_module')
    mock_import_module.return_value = mock_module

    # Mock a class object to be returned by getattr
    mock_class = type('MockClass', (object,), {})
    setattr(mock_module, 'MockClass', mock_class)

    # Test importing a class and instantiating it
    result = import_string('mock_module.MockClass')
    assert isinstance(result, mock_class)
    mock_import_module.assert_called_once_with('mock_module', package=None)
