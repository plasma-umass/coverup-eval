# file pytutils/lazy/lazy_import.py:449-475
# lines [449, 474, 475]
# branches []

import pytest
from unittest import mock
from pytutils.lazy.lazy_import import lazy_import

def test_lazy_import(mocker):
    # Mock the ImportProcessor class and its lazy_import method
    mock_import_processor = mocker.patch('pytutils.lazy.lazy_import.ImportProcessor')
    mock_lazy_import = mock_import_processor.return_value.lazy_import

    # Define a scope and text for the lazy_import function
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
    result = lazy_import(scope, text)

    # Assertions to verify the behavior
    mock_import_processor.assert_called_once_with(lazy_import_class=None)
    mock_lazy_import.assert_called_once_with(scope, text)
    assert result == mock_lazy_import.return_value

    # Clean up
    del scope
    del text
    del result
