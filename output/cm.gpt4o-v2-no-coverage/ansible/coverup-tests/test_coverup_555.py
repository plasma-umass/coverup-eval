# file: lib/ansible/plugins/inventory/toml.py:112-121
# asked: {"lines": [112, 113, 114, 116, 117, 118, 119, 120], "branches": []}
# gained: {"lines": [112, 113, 114, 116, 117, 118, 119, 120], "branches": []}

import pytest
import toml
from ansible.parsing.yaml.objects import AnsibleSequence, AnsibleUnicode
from ansible.utils.unsafe_proxy import AnsibleUnsafeBytes, AnsibleUnsafeText
from ansible.plugins.inventory.toml import AnsibleTomlEncoder

def test_ansible_toml_encoder_init():
    encoder = AnsibleTomlEncoder()
    
    assert encoder.dump_funcs[AnsibleSequence] == encoder.dump_funcs[list]
    assert encoder.dump_funcs[AnsibleUnicode] == encoder.dump_funcs[str]
    assert encoder.dump_funcs[AnsibleUnsafeBytes] == encoder.dump_funcs[str]
    assert encoder.dump_funcs[AnsibleUnsafeText] == encoder.dump_funcs[str]
