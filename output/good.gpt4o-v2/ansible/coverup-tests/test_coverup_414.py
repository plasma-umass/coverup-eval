# file: lib/ansible/modules/rpm_key.py:169-177
# asked: {"lines": [169, 171, 172, 173, 174, 175, 177], "branches": [[172, 173], [172, 174], [174, 175], [174, 177]]}
# gained: {"lines": [169, 171, 172, 174, 175, 177], "branches": [[172, 174], [174, 175], [174, 177]]}

import pytest
from ansible.modules.rpm_key import RpmKey

@pytest.fixture
def rpm_key_instance(mocker):
    module_mock = mocker.Mock()
    module_mock.get_bin_path.side_effect = lambda x, required=False: f'/usr/bin/{x}'
    module_mock.params = {
        'state': 'present',
        'key': '0xABC123',
        'fingerprint': None
    }
    rpm_key = RpmKey.__new__(RpmKey)
    rpm_key.module = module_mock
    return rpm_key

def test_normalize_keyid_no_prefix(rpm_key_instance):
    keyid = "ABC123"
    normalized = rpm_key_instance.normalize_keyid(keyid)
    assert normalized == "ABC123"

def test_normalize_keyid_with_0x_prefix(rpm_key_instance):
    keyid = "0xABC123"
    normalized = rpm_key_instance.normalize_keyid(keyid)
    assert normalized == "ABC123"

def test_normalize_keyid_with_0X_prefix(rpm_key_instance):
    keyid = "0XABC123"
    normalized = rpm_key_instance.normalize_keyid(keyid)
    assert normalized == "ABC123"

def test_normalize_keyid_with_whitespace(rpm_key_instance):
    keyid = "  abc123  "
    normalized = rpm_key_instance.normalize_keyid(keyid)
    assert normalized == "ABC123"
