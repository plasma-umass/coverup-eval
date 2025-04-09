# file: lib/ansible/template/native_helpers.py:46-93
# asked: {"lines": [46, 55, 57, 58, 60, 61, 64, 65, 67, 75, 78, 79, 81, 82, 83, 85, 86, 90, 92, 93], "branches": [[57, 58], [57, 60], [60, 61], [60, 81], [64, 65], [64, 67], [67, 75], [67, 78], [78, 79], [78, 85], [81, 82], [81, 83]]}
# gained: {"lines": [46, 55, 57, 58, 60, 61, 64, 65, 67, 75, 78, 79, 81, 83, 85, 86, 90, 92, 93], "branches": [[57, 58], [57, 60], [60, 61], [60, 81], [64, 65], [64, 67], [67, 75], [67, 78], [78, 79], [78, 85], [81, 83]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.six import string_types
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
from ansible.utils.native_jinja import NativeJinjaText
from ansible.template.native_helpers import ansible_native_concat

def test_ansible_native_concat_empty():
    assert ansible_native_concat([]) is None

def test_ansible_native_concat_single_node():
    with patch('ansible.template.native_helpers._fail_on_undefined', return_value='test') as mock_fail:
        assert ansible_native_concat(['node']) == 'test'
        mock_fail.assert_called_once_with('node')

def test_ansible_native_concat_single_node_vault():
    vault_data = AnsibleVaultEncryptedUnicode('ciphertext')
    vault_data.data = 'vaulted_data'
    with patch('ansible.template.native_helpers._fail_on_undefined', return_value=vault_data) as mock_fail:
        assert ansible_native_concat(['node']) == 'vaulted_data'
        mock_fail.assert_called_once_with('node')

def test_ansible_native_concat_single_node_native_jinja():
    native_jinja_text = NativeJinjaText('native_text')
    with patch('ansible.template.native_helpers._fail_on_undefined', return_value=native_jinja_text) as mock_fail:
        assert ansible_native_concat(['node']) == native_jinja_text
        mock_fail.assert_called_once_with('node')

def test_ansible_native_concat_single_node_non_string():
    with patch('ansible.template.native_helpers._fail_on_undefined', return_value=123) as mock_fail:
        assert ansible_native_concat(['node']) == 123
        mock_fail.assert_called_once_with('node')

def test_ansible_native_concat_multiple_nodes():
    with patch('ansible.template.native_helpers._fail_on_undefined', side_effect=lambda x: x):
        assert ansible_native_concat(['node1', 'node2']) == 'node1node2'

def test_ansible_native_concat_literal_eval():
    with patch('ansible.template.native_helpers._fail_on_undefined', side_effect=lambda x: x):
        assert ansible_native_concat(['1', '2']) == 12

def test_ansible_native_concat_literal_eval_exception():
    with patch('ansible.template.native_helpers._fail_on_undefined', side_effect=lambda x: x):
        assert ansible_native_concat(['invalid', 'data']) == 'invaliddata'
