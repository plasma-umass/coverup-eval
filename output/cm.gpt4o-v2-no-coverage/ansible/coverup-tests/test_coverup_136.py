# file: lib/ansible/config/manager.py:395-419
# asked: {"lines": [395, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 409, 410, 412, 413, 416, 417, 419], "branches": [[400, 401], [400, 419], [407, 400], [407, 409], [409, 410], [409, 412], [416, 400], [416, 417]]}
# gained: {"lines": [395, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 409, 410, 412, 413, 416, 417, 419], "branches": [[400, 401], [400, 419], [407, 409], [409, 410], [409, 412], [416, 400], [416, 417]]}

import pytest
from ansible.config.manager import ConfigManager
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
from ansible.module_utils._text import to_text

class MockContainer(dict):
    def __init__(self, *args, **kwargs):
        super(MockContainer, self).__init__(*args, **kwargs)

@pytest.fixture
def config_manager():
    class TestConfigManager(ConfigManager):
        def __init__(self):
            self.WARNINGS = set()
            self.DEPRECATED = []

    return TestConfigManager()

def test_loop_entries_basic(config_manager):
    container = MockContainer({'valid_entry': 'value1'})
    entry_list = [{'name': 'valid_entry'}]
    value, origin = config_manager._loop_entries(container, entry_list)
    assert value == 'value1'
    assert origin == 'valid_entry'
    assert not config_manager.WARNINGS
    assert not config_manager.DEPRECATED

def test_loop_entries_unicode_error(config_manager, mocker):
    container = MockContainer({'invalid_entry': 'value1'})
    entry_list = [{'name': 'invalid_entry'}]
    mocker.patch.object(container, 'get', side_effect=UnicodeEncodeError('codec', 'a', 0, 1, 'reason'))
    value, origin = config_manager._loop_entries(container, entry_list)
    assert value is None
    assert origin is None
    assert 'value for config entry invalid_entry contains invalid characters, ignoring...' in config_manager.WARNINGS
    assert not config_manager.DEPRECATED

def test_loop_entries_vault_encrypted(config_manager):
    encrypted_value = AnsibleVaultEncryptedUnicode('encrypted_value')
    container = MockContainer({'vault_entry': encrypted_value})
    entry_list = [{'name': 'vault_entry'}]
    value, origin = config_manager._loop_entries(container, entry_list)
    assert value == to_text(encrypted_value, errors='surrogate_or_strict')
    assert origin == 'vault_entry'
    assert not config_manager.WARNINGS
    assert not config_manager.DEPRECATED

def test_loop_entries_deprecated(config_manager):
    container = MockContainer({'deprecated_entry': 'value2'})
    entry_list = [{'name': 'deprecated_entry', 'deprecated': 'deprecated_reason'}]
    value, origin = config_manager._loop_entries(container, entry_list)
    assert value == 'value2'
    assert origin == 'deprecated_entry'
    assert not config_manager.WARNINGS
    assert config_manager.DEPRECATED == [('deprecated_entry', 'deprecated_reason')]
