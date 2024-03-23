# file lib/ansible/utils/vars.py:185-210
# lines [185, 186, 187, 188, 189, 190, 191, 193, 195, 196, 197, 198, 200, 203, 205, 206, 208, 210]
# branches ['187->188', '187->210', '190->191', '190->193', '193->195', '193->196', '196->197', '196->198', '198->200', '198->203', '205->206', '205->208']

import pytest
from ansible.errors import AnsibleOptionsError
from ansible.utils.vars import load_extra_vars
from ansible.parsing.dataloader import DataLoader
from ansible.utils.vars import combine_vars
from ansible.parsing.yaml.loader import AnsibleLoader
from collections.abc import MutableMapping
from ansible.module_utils._text import to_text
from ansible.module_utils.common.collections import ImmutableDict
from unittest.mock import MagicMock, patch

# Mock the context and the parse_kv function
@pytest.fixture
def mock_context(mocker):
    mocker.patch('ansible.utils.vars.context.CLIARGS', {'extra_vars': []})

# Mock the DataLoader
@pytest.fixture
def mock_loader(mocker):
    mock_loader = MagicMock(spec=DataLoader)
    mock_loader.load_from_file.return_value = {'key': 'value'}
    mock_loader.load.return_value = {'key': 'value'}
    return mock_loader

# Test function to improve coverage
def test_load_extra_vars(mock_context, mock_loader):
    # Test valid YAML file
    with patch('ansible.utils.vars.context.CLIARGS', {'extra_vars': ('@valid_file.yml',)}):
        extra_vars = load_extra_vars(mock_loader)
        assert extra_vars == {'key': 'value'}
        mock_loader.load_from_file.assert_called_once_with('valid_file.yml')

    # Test invalid prefix
    with patch('ansible.utils.vars.context.CLIARGS', {'extra_vars': ('/invalid_prefix',)}):
        with pytest.raises(AnsibleOptionsError) as excinfo:
            load_extra_vars(mock_loader)
        assert "Please prepend extra_vars filename '/invalid_prefix' with '@'" in str(excinfo.value)

    # Test valid inline YAML
    with patch('ansible.utils.vars.context.CLIARGS', {'extra_vars': ('[{"key": "value"}]',)}):
        extra_vars = load_extra_vars(mock_loader)
        assert extra_vars == {'key': 'value'}
        mock_loader.load.assert_called_once_with('[{"key": "value"}]')

    # Test invalid data
    with patch('ansible.utils.vars.context.CLIARGS', {'extra_vars': ('invalid_data',)}):
        with patch('ansible.utils.vars.parse_kv', return_value=None):
            with pytest.raises(AnsibleOptionsError) as excinfo:
                load_extra_vars(mock_loader)
            assert "Invalid extra vars data supplied. 'invalid_data' could not be made into a dictionary" in str(excinfo.value)
