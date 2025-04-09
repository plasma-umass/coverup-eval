# file lib/ansible/module_utils/common/json.py:42-82
# lines [42, 43, 47, 48, 49, 50, 53, 54, 56, 57, 59, 60, 62, 63, 65, 66, 68, 71, 72, 74, 79, 80, 82]
# branches ['54->56', '54->60', '56->57', '56->59', '60->62', '60->63', '63->65', '63->66', '66->68', '66->71', '79->80', '79->82']

import json
import pytest
from ansible.module_utils.common.json import AnsibleJSONEncoder
from ansible.module_utils._text import to_text
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

@pytest.fixture
def vault_text():
    vault = AnsibleVaultEncryptedUnicode('vault_value')
    vault._ciphertext = b'encrypted_data'
    return vault

@pytest.fixture
def unsafe_string(mocker):
    unsafe = mocker.Mock()
    unsafe.__UNSAFE__ = True
    unsafe.__str__ = mocker.Mock(return_value='unsafe_string')
    return unsafe

def test_ansible_json_encoder_with_vault_to_text(vault_text):
    encoder = AnsibleJSONEncoder(vault_to_text=True)
    result = encoder.default(vault_text)
    assert result == to_text(vault_text, errors='surrogate_or_strict')

def test_ansible_json_encoder_without_vault_to_text(vault_text):
    encoder = AnsibleJSONEncoder(vault_to_text=False)
    result = encoder.default(vault_text)
    expected = {'__ansible_vault': to_text(vault_text._ciphertext, errors='surrogate_or_strict', nonstring='strict')}
    assert result == expected

def test_ansible_json_encoder_with_unsafe_object(unsafe_string):
    encoder = AnsibleJSONEncoder(preprocess_unsafe=False)
    with pytest.raises(TypeError):
        encoder.default(unsafe_string)
