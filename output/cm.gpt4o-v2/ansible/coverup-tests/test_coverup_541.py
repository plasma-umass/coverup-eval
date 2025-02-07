# file: lib/ansible/parsing/utils/yaml.py:46-56
# asked: {"lines": [46, 49, 50, 51, 53, 54, 55, 56], "branches": []}
# gained: {"lines": [46, 49, 50, 51, 53, 54, 55, 56], "branches": []}

import pytest
from ansible.parsing.utils.yaml import _safe_load
from ansible.parsing.yaml.loader import AnsibleLoader
from unittest.mock import patch, MagicMock

def test_safe_load_with_dispose():
    stream = "key: value"
    file_name = "test_file.yml"
    vault_secrets = None

    with patch.object(AnsibleLoader, 'dispose', return_value=None) as mock_dispose:
        result = _safe_load(stream, file_name, vault_secrets)
        assert result == {'key': 'value'}
        mock_dispose.assert_called_once()

def test_safe_load_without_dispose():
    stream = "key: value"
    file_name = "test_file.yml"
    vault_secrets = None

    with patch('ansible.parsing.yaml.loader.AnsibleLoader.dispose', side_effect=AttributeError):
        result = _safe_load(stream, file_name, vault_secrets)
        assert result == {'key': 'value'}
