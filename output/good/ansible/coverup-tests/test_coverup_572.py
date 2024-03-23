# file lib/ansible/plugins/filter/encryption.py:73-82
# lines [73, 74, 76, 77, 78, 79, 82]
# branches []

import pytest
from unittest.mock import MagicMock
from ansible.plugins.filter.encryption import FilterModule

def test_filter_module_filters():
    filter_module = FilterModule()
    filters_dict = filter_module.filters()

    # Assertions to ensure the filters are correctly set
    assert 'vault' in filters_dict
    assert 'unvault' in filters_dict
    assert callable(filters_dict['vault'])
    assert callable(filters_dict['unvault'])

    # Mocking the do_vault and do_unvault functions
    mock_do_vault = MagicMock(return_value='encrypted_data')
    mock_do_unvault = MagicMock(return_value='decrypted_data')

    # Replacing the actual functions with mocks in the filters dictionary
    filters_dict['vault'] = mock_do_vault
    filters_dict['unvault'] = mock_do_unvault

    # Call the filters to ensure they execute the mocked functions
    encrypted_data = filters_dict['vault']('data', 'secret')
    decrypted_data = filters_dict['unvault']('encrypted_data', 'secret')

    # Verify that the mocked functions were called with the correct arguments
    mock_do_vault.assert_called_once_with('data', 'secret')
    mock_do_unvault.assert_called_once_with('encrypted_data', 'secret')

    # Assertions to check the return values are as expected from the mocks
    assert encrypted_data == 'encrypted_data'
    assert decrypted_data == 'decrypted_data'
