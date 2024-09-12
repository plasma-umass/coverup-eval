# file: pytutils/lazy/lazy_import.py:189-191
# asked: {"lines": [190, 191], "branches": []}
# gained: {"lines": [190, 191], "branches": []}

import pytest
from pytutils.lazy.lazy_import import ScopeReplacer

class TestScopeReplacer:
    def test_scope_replacer_call(self, mocker):
        # Mock the _resolve method to return a callable object
        mock_scope = {}
        mock_factory = mocker.Mock()
        mock_name = 'test_obj'
        mock_callable = mocker.Mock()
        mock_factory.return_value = mock_callable

        replacer = ScopeReplacer(mock_scope, mock_factory, mock_name)
        
        # Use a temporary attribute to mock _resolve
        original_resolve = replacer._resolve
        replacer._resolve = mocker.Mock(return_value=mock_callable)

        # Call the replacer and assert the callable was called with the correct arguments
        args = (1, 2, 3)
        kwargs = {'a': 4, 'b': 5}
        replacer(*args, **kwargs)
        mock_callable.assert_called_once_with(*args, **kwargs)

        # Clean up
        replacer._resolve = original_resolve
        del mock_scope[mock_name]
