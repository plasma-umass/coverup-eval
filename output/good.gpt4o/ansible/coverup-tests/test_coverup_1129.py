# file lib/ansible/config/manager.py:395-419
# lines [404, 405, 406, 409, 410, 412, 413, 416, 417]
# branches ['407->409', '409->410', '409->412', '416->400', '416->417']

import pytest
from unittest.mock import MagicMock, patch
from ansible.config.manager import ConfigManager
from ansible.module_utils._text import to_text

class AnsibleVaultEncryptedUnicode(str):
    pass

@pytest.fixture
def config_manager():
    return ConfigManager()

def test_loop_entries_unicode_error(config_manager, mocker):
    container = MagicMock()
    entry_list = [{'name': 'test_entry'}]

    # Mock container.get to raise UnicodeEncodeError
    container.get.side_effect = UnicodeEncodeError("codec", "string", 0, 1, "reason")

    # Mock the WARNINGS set
    mocker.patch.object(config_manager, 'WARNINGS', set())

    value, origin = config_manager._loop_entries(container, entry_list)

    assert value is None
    assert origin is None
    assert 'value for config entry test_entry contains invalid characters, ignoring...' in config_manager.WARNINGS

def test_loop_entries_vault_encrypted_unicode(config_manager, mocker):
    container = MagicMock()
    entry_list = [{'name': 'vault_entry'}]

    # Mock container.get to return an AnsibleVaultEncryptedUnicode object
    encrypted_value = AnsibleVaultEncryptedUnicode('encrypted_value')
    container.get.return_value = encrypted_value

    # Mock the DEPRECATED list
    mocker.patch.object(config_manager, 'DEPRECATED', [])

    value, origin = config_manager._loop_entries(container, entry_list)

    assert value == to_text(encrypted_value, errors='surrogate_or_strict')
    assert origin == 'vault_entry'

def test_loop_entries_deprecated(config_manager, mocker):
    container = MagicMock()
    entry_list = [{'name': 'deprecated_entry', 'deprecated': 'deprecated_reason'}]

    # Mock container.get to return a normal value
    container.get.return_value = 'normal_value'

    # Mock the DEPRECATED list
    mocker.patch.object(config_manager, 'DEPRECATED', [])

    value, origin = config_manager._loop_entries(container, entry_list)

    assert value == 'normal_value'
    assert origin == 'deprecated_entry'
    assert ('deprecated_entry', 'deprecated_reason') in config_manager.DEPRECATED
