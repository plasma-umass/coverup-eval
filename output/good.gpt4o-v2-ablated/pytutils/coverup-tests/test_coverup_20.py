# file: pytutils/lazy/lazy_import.py:449-475
# asked: {"lines": [449, 474, 475], "branches": []}
# gained: {"lines": [449, 474, 475], "branches": []}

import pytest
from unittest.mock import MagicMock

# Assuming ImportProcessor is defined in the same module
from pytutils.lazy.lazy_import import lazy_import, ImportProcessor

def test_lazy_import_with_valid_imports(monkeypatch):
    # Mock the ImportProcessor class and its lazy_import method
    mock_import_processor = MagicMock()
    mock_lazy_import = MagicMock()
    mock_import_processor.return_value.lazy_import = mock_lazy_import

    # Patch the ImportProcessor to use the mock
    monkeypatch.setattr('pytutils.lazy.lazy_import.ImportProcessor', mock_import_processor)

    # Define a scope and text for the test
    scope = {}
    text = '''
    from some_module import (
        foo,
        bar,
        baz,
    )
    import some_module.branch
    import some_module.transport
    '''

    # Call the lazy_import function
    lazy_import(scope, text)

    # Assert that ImportProcessor was instantiated correctly
    mock_import_processor.assert_called_once_with(lazy_import_class=None)

    # Assert that lazy_import was called with the correct arguments
    mock_lazy_import.assert_called_once_with(scope, text)

def test_lazy_import_with_custom_class(monkeypatch):
    # Mock the ImportProcessor class and its lazy_import method
    mock_import_processor = MagicMock()
    mock_lazy_import = MagicMock()
    mock_import_processor.return_value.lazy_import = mock_lazy_import

    # Patch the ImportProcessor to use the mock
    monkeypatch.setattr('pytutils.lazy.lazy_import.ImportProcessor', mock_import_processor)

    # Define a scope, text, and custom lazy_import_class for the test
    scope = {}
    text = '''
    from another_module import (
        alpha,
        beta,
        gamma,
    )
    import another_module.branch
    import another_module.transport
    '''
    custom_class = MagicMock()

    # Call the lazy_import function with a custom class
    lazy_import(scope, text, lazy_import_class=custom_class)

    # Assert that ImportProcessor was instantiated with the custom class
    mock_import_processor.assert_called_once_with(lazy_import_class=custom_class)

    # Assert that lazy_import was called with the correct arguments
    mock_lazy_import.assert_called_once_with(scope, text)
