# file: lib/ansible/modules/rpm_key.py:179-186
# asked: {"lines": [180, 181, 182, 183, 184, 186], "branches": [[181, 182], [181, 186], [183, 181], [183, 184]]}
# gained: {"lines": [180, 181, 182, 183, 184, 186], "branches": [[181, 182], [181, 186], [183, 184]]}

import pytest
from unittest.mock import MagicMock

def test_getkeyid_success(monkeypatch):
    rpm_key_instance = MagicMock()
    rpm_key_instance.gpg = 'gpg'
    rpm_key_instance.execute_command = MagicMock(return_value=("pub:u:2048:1:ABCDEF1234567890:...", ""))
    rpm_key_instance.module = MagicMock()

    def mock_init(self, module):
        self.gpg = 'gpg'
        self.module = module
        self.execute_command = rpm_key_instance.execute_command

    monkeypatch.setattr('ansible.modules.rpm_key.RpmKey.__init__', mock_init)

    from ansible.modules.rpm_key import RpmKey
    rpm_key = RpmKey(module=MagicMock())
    key_id = rpm_key.getkeyid('dummy_keyfile')
    assert key_id == 'ABCDEF1234567890'

def test_getkeyid_failure(monkeypatch):
    rpm_key_instance = MagicMock()
    rpm_key_instance.gpg = 'gpg'
    rpm_key_instance.execute_command = MagicMock(return_value=("", ""))
    rpm_key_instance.module = MagicMock()

    def mock_init(self, module):
        self.gpg = 'gpg'
        self.module = module
        self.execute_command = rpm_key_instance.execute_command

    monkeypatch.setattr('ansible.modules.rpm_key.RpmKey.__init__', mock_init)

    from ansible.modules.rpm_key import RpmKey
    rpm_key = RpmKey(module=MagicMock())
    rpm_key.module.fail_json = MagicMock(side_effect=Exception("Unexpected gpg output"))
    with pytest.raises(Exception, match="Unexpected gpg output"):
        rpm_key.getkeyid('dummy_keyfile')
    rpm_key.module.fail_json.assert_called_once_with(msg="Unexpected gpg output")
