# file: lib/ansible/playbook/base.py:349-402
# asked: {"lines": [350, 351, 353, 354, 356, 357, 358, 359, 360, 365, 366, 371, 372, 375, 376, 378, 379, 382, 383, 385, 386, 387, 392, 393, 394, 395, 397, 398, 400, 402], "branches": [[350, 351], [350, 353], [353, 354], [353, 356], [357, 358], [357, 402], [358, 359], [358, 365], [366, 371], [366, 400], [371, 372], [371, 382], [375, 376], [375, 378], [382, 383], [382, 385], [386, 387], [386, 392], [392, 366], [392, 393], [397, 366], [397, 398]]}
# gained: {"lines": [350, 351, 353, 354, 356, 357, 358, 359, 360, 365, 366, 371, 372, 375, 376, 378, 379, 382, 383, 385, 386, 387, 392, 393, 394, 395, 397, 398, 400, 402], "branches": [[350, 351], [350, 353], [353, 354], [353, 356], [357, 358], [357, 402], [358, 359], [358, 365], [366, 371], [366, 400], [371, 372], [371, 382], [375, 376], [382, 383], [386, 387], [392, 393], [397, 398]]}

import pytest
from ansible.errors import AnsibleParserError
from ansible.playbook.base import FieldAttributeBase

class MockPlay:
    def _resolve_group(self, group_name):
        return (group_name, None)

    def _resolve_action(self, action_name, mandatory=True):
        if action_name == "ansible.legacy.ping":
            return "ansible.legacy.ping"
        if action_name == "ansible.builtin.ping":
            return "ansible.builtin.ping"
        return None

@pytest.fixture
def field_attribute_base(monkeypatch):
    fab = FieldAttributeBase()
    monkeypatch.setattr(fab, '_resolve_group', MockPlay()._resolve_group)
    monkeypatch.setattr(fab, '_resolve_action', MockPlay()._resolve_action)
    monkeypatch.setattr(fab.__class__, 'play', property(lambda self: True))
    return fab

def test_load_module_defaults_none(field_attribute_base):
    result = field_attribute_base._load_module_defaults("test", None)
    assert result is None

def test_load_module_defaults_not_list(field_attribute_base):
    result = field_attribute_base._load_module_defaults("test", {"ping": "pong"})
    assert result == [{"ansible.legacy.ping": "pong", "ansible.builtin.ping": "pong"}]

def test_load_module_defaults_invalid_dict(field_attribute_base):
    with pytest.raises(AnsibleParserError):
        field_attribute_base._load_module_defaults("test", ["invalid"])

def test_load_module_defaults_group(field_attribute_base):
    result = field_attribute_base._load_module_defaults("test", [{"group/testgroup": "defaults"}])
    assert result == [{"group/testgroup": "defaults"}]

def test_load_module_defaults_action(field_attribute_base):
    result = field_attribute_base._load_module_defaults("test", [{"ping": "pong"}])
    assert result == [{"ansible.legacy.ping": "pong", "ansible.builtin.ping": "pong"}]

def test_load_module_defaults_multiple(field_attribute_base):
    result = field_attribute_base._load_module_defaults("test", [{"ping": "pong"}, {"group/testgroup": "defaults"}])
    assert result == [{"ansible.legacy.ping": "pong", "ansible.builtin.ping": "pong"}, {"group/testgroup": "defaults"}]
