# file: lib/ansible/template/native_helpers.py:46-93
# asked: {"lines": [46, 55, 57, 58, 60, 61, 64, 65, 67, 75, 78, 79, 81, 82, 83, 85, 86, 90, 92, 93], "branches": [[57, 58], [57, 60], [60, 61], [60, 81], [64, 65], [64, 67], [67, 75], [67, 78], [78, 79], [78, 85], [81, 82], [81, 83]]}
# gained: {"lines": [46, 55, 57, 58, 60, 61, 64, 65, 67, 75, 78, 79, 81, 83, 85, 86, 90, 92, 93], "branches": [[57, 58], [57, 60], [60, 61], [60, 81], [64, 65], [64, 67], [67, 75], [67, 78], [78, 79], [78, 85], [81, 83]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.template.native_helpers import ansible_native_concat
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
from ansible.utils.native_jinja import NativeJinjaText

def test_ansible_native_concat_empty():
    assert ansible_native_concat([]) is None

def test_ansible_native_concat_single_vault_encrypted():
    node = AnsibleVaultEncryptedUnicode('vault_data')
    with patch('ansible.template.native_helpers._fail_on_undefined', return_value=node):
        assert ansible_native_concat([node]) == 'vault_data'

def test_ansible_native_concat_single_native_jinja_text():
    node = NativeJinjaText('native_text')
    with patch('ansible.template.native_helpers._fail_on_undefined', return_value=node):
        assert ansible_native_concat([node]) == node

def test_ansible_native_concat_single_non_string():
    node = 123
    with patch('ansible.template.native_helpers._fail_on_undefined', return_value=node):
        assert ansible_native_concat([node]) == node

def test_ansible_native_concat_multiple_nodes():
    nodes = ['1', '2', '3']
    with patch('ansible.template.native_helpers._fail_on_undefined', side_effect=lambda x: x):
        assert ansible_native_concat(nodes) == 123

def test_ansible_native_concat_syntax_error():
    nodes = ['invalid_syntax']
    with patch('ansible.template.native_helpers._fail_on_undefined', side_effect=lambda x: x):
        assert ansible_native_concat(nodes) == 'invalid_syntax'
