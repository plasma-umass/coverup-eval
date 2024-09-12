# file: lib/ansible/config/manager.py:395-419
# asked: {"lines": [395, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 409, 410, 412, 413, 416, 417, 419], "branches": [[400, 401], [400, 419], [407, 400], [407, 409], [409, 410], [409, 412], [416, 400], [416, 417]]}
# gained: {"lines": [395, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 409, 410, 412, 413, 416, 417, 419], "branches": [[400, 401], [400, 419], [407, 400], [407, 409], [409, 410], [409, 412], [416, 400], [416, 417]]}

import pytest
from ansible.config.manager import ConfigManager
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
from ansible.module_utils._text import to_text

@pytest.fixture
def config_manager():
    class MockConfigManager(ConfigManager):
        WARNINGS = set()
        DEPRECATED = []

    return MockConfigManager()

def test_loop_entries_with_valid_entries(config_manager):
    container = {
        'valid_entry': 'value1',
        'vault_entry': AnsibleVaultEncryptedUnicode('encrypted_value')
    }
    entry_list = [
        {'name': 'valid_entry'},
        {'name': 'vault_entry'}
    ]

    value, origin = config_manager._loop_entries(container, entry_list)

    assert value == 'encrypted_value'
    assert origin == 'vault_entry'
    assert len(config_manager.WARNINGS) == 0
    assert len(config_manager.DEPRECATED) == 0

def test_loop_entries_with_unicode_error(config_manager, mocker):
    container = mocker.MagicMock()
    container.get.side_effect = UnicodeEncodeError('codec', 'string', 0, 1, 'reason')
    entry_list = [{'name': 'invalid_entry'}]

    value, origin = config_manager._loop_entries(container, entry_list)

    assert value is None
    assert origin is None
    assert len(config_manager.WARNINGS) == 1
    assert 'invalid characters' in next(iter(config_manager.WARNINGS))
    assert len(config_manager.DEPRECATED) == 0

def test_loop_entries_with_deprecated_entry(config_manager):
    container = {'deprecated_entry': 'value2'}
    entry_list = [{'name': 'deprecated_entry', 'deprecated': 'deprecated_reason'}]

    value, origin = config_manager._loop_entries(container, entry_list)

    assert value == 'value2'
    assert origin == 'deprecated_entry'
    assert len(config_manager.WARNINGS) == 0
    assert len(config_manager.DEPRECATED) == 1
    assert config_manager.DEPRECATED[0] == ('deprecated_entry', 'deprecated_reason')
