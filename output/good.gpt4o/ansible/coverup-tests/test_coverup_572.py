# file lib/ansible/utils/collection_loader/_collection_finder.py:994-998
# lines [994, 995, 996, 998]
# branches ['995->996', '995->998']

import pytest
from unittest.mock import patch

# Assuming the function _nested_dict_get is defined somewhere in the module
from ansible.utils.collection_loader._collection_finder import _get_import_redirect

def test_get_import_redirect_no_meta():
    result = _get_import_redirect({}, 'some.fullname')
    assert result is None

def test_get_import_redirect_with_meta(mocker):
    mock_nested_dict_get = mocker.patch('ansible.utils.collection_loader._collection_finder._nested_dict_get')
    collection_meta_dict = {
        'import_redirection': {
            'some.fullname': {
                'redirect': 'redirect_value'
            }
        }
    }
    fullname = 'some.fullname'
    
    mock_nested_dict_get.return_value = 'redirect_value'
    
    result = _get_import_redirect(collection_meta_dict, fullname)
    
    mock_nested_dict_get.assert_called_once_with(collection_meta_dict, ['import_redirection', fullname, 'redirect'])
    assert result == 'redirect_value'
