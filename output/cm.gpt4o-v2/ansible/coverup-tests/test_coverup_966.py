# file: lib/ansible/modules/rpm_key.py:208-210
# asked: {"lines": [208, 210], "branches": []}
# gained: {"lines": [208, 210], "branches": []}

import pytest
import re
from unittest.mock import Mock, patch
from ansible.modules.rpm_key import RpmKey

@pytest.fixture
def rpm_key(mocker):
    module = mocker.Mock()
    module.get_bin_path.return_value = '/usr/bin/rpm'
    module.params = {
        'state': 'present',
        'key': '0x12345678',
        'fingerprint': None
    }
    module.run_command.return_value = (0, '', '')
    return RpmKey(module)

def test_is_keyid_valid_key(rpm_key):
    assert rpm_key.is_keyid('0x12345678') is not None

def test_is_keyid_invalid_key(rpm_key):
    assert rpm_key.is_keyid('invalid_key') is None

def test_is_keyid_valid_key_no_prefix(rpm_key):
    assert rpm_key.is_keyid('12345678') is not None

def test_is_keyid_invalid_key_length(rpm_key):
    assert rpm_key.is_keyid('1234567') is None
