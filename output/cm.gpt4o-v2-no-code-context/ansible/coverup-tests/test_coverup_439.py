# file: lib/ansible/plugins/inventory/toml.py:112-121
# asked: {"lines": [112, 113, 114, 116, 117, 118, 119, 120], "branches": []}
# gained: {"lines": [112, 113, 114, 116, 117, 118, 119, 120], "branches": []}

import pytest
import toml
from ansible.plugins.inventory.toml import AnsibleTomlEncoder, AnsibleSequence, AnsibleUnicode, AnsibleUnsafeBytes, AnsibleUnsafeText

def test_ansible_toml_encoder_initialization():
    encoder = AnsibleTomlEncoder()
    assert isinstance(encoder, AnsibleTomlEncoder)
    assert encoder.dump_funcs[AnsibleSequence] == encoder.dump_funcs[list]
    assert encoder.dump_funcs[AnsibleUnicode] == encoder.dump_funcs[str]
    assert encoder.dump_funcs[AnsibleUnsafeBytes] == encoder.dump_funcs[str]
    assert encoder.dump_funcs[AnsibleUnsafeText] == encoder.dump_funcs[str]

@pytest.fixture
def mock_toml_encoder(monkeypatch):
    class MockTomlEncoder:
        def __init__(self, *args, **kwargs):
            self.dump_funcs = {}
        def update(self, new_funcs):
            self.dump_funcs.update(new_funcs)
    monkeypatch.setattr(toml, 'TomlEncoder', MockTomlEncoder)

def test_ansible_toml_encoder_with_mock(mock_toml_encoder):
    encoder = AnsibleTomlEncoder()
    assert isinstance(encoder, AnsibleTomlEncoder)
    assert AnsibleSequence in encoder.dump_funcs
    assert AnsibleUnicode in encoder.dump_funcs
    assert AnsibleUnsafeBytes in encoder.dump_funcs
    assert AnsibleUnsafeText in encoder.dump_funcs
