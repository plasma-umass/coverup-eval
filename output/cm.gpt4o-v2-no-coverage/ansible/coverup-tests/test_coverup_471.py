# file: lib/ansible/modules/rpm_key.py:169-177
# asked: {"lines": [169, 171, 172, 173, 174, 175, 177], "branches": [[172, 173], [172, 174], [174, 175], [174, 177]]}
# gained: {"lines": [169, 171, 172, 174, 175, 177], "branches": [[172, 174], [174, 175], [174, 177]]}

import pytest
from ansible.modules.rpm_key import RpmKey

@pytest.fixture
def rpm_key_instance(mocker):
    module_mock = mocker.Mock()
    module_mock.get_bin_path.side_effect = lambda name, required=False: f'/usr/bin/{name}'
    module_mock.params = {
        'state': 'present',
        'key': '0x12345678',
        'fingerprint': None
    }
    module_mock.run_command.return_value = (0, '', '')
    module_mock.exit_json = mocker.Mock()
    module_mock.fail_json = mocker.Mock()
    return RpmKey(module_mock)

def test_normalize_keyid_no_prefix(rpm_key_instance):
    keyid = "12345678"
    normalized = rpm_key_instance.normalize_keyid(keyid)
    assert normalized == "12345678"

def test_normalize_keyid_lowercase_prefix(rpm_key_instance):
    keyid = "0x12345678"
    normalized = rpm_key_instance.normalize_keyid(keyid)
    assert normalized == "12345678"

def test_normalize_keyid_uppercase_prefix(rpm_key_instance):
    keyid = "0X12345678"
    normalized = rpm_key_instance.normalize_keyid(keyid)
    assert normalized == "12345678"

def test_normalize_keyid_with_whitespace(rpm_key_instance):
    keyid = "  0x12345678  "
    normalized = rpm_key_instance.normalize_keyid(keyid)
    assert normalized == "12345678"
