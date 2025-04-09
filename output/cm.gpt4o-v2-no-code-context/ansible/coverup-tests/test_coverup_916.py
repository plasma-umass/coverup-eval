# file: lib/ansible/playbook/base.py:349-402
# asked: {"lines": [350, 351, 353, 354, 356, 357, 358, 359, 360, 365, 366, 371, 372, 375, 376, 378, 379, 382, 383, 385, 386, 387, 392, 393, 394, 395, 397, 398, 400, 402], "branches": [[350, 351], [350, 353], [353, 354], [353, 356], [357, 358], [357, 402], [358, 359], [358, 365], [366, 371], [366, 400], [371, 372], [371, 382], [375, 376], [375, 378], [382, 383], [382, 385], [386, 387], [386, 392], [392, 366], [392, 393], [397, 366], [397, 398]]}
# gained: {"lines": [350, 351, 353, 354, 356, 357, 358, 359, 360, 365, 366, 371, 372, 375, 376, 378, 379, 382, 383, 385, 386, 387, 392, 393, 394, 395, 397, 398, 400, 402], "branches": [[350, 351], [350, 353], [353, 354], [353, 356], [357, 358], [357, 402], [358, 359], [358, 365], [366, 371], [366, 400], [371, 372], [371, 382], [375, 376], [382, 383], [382, 385], [386, 387], [392, 393], [397, 398]]}

import pytest
from ansible.playbook.base import FieldAttributeBase
from ansible.errors import AnsibleParserError

class TestFieldAttributeBase:
    @pytest.fixture
    def field_attribute_base(self, monkeypatch):
        class DummyPlay:
            def __init__(self):
                self._resolved_action_groups_cache = {}

        class DummyFieldAttributeBase(FieldAttributeBase):
            def __init__(self):
                self._play = DummyPlay()

            @property
            def play(self):
                return self._play

            def _resolve_group(self, group_name):
                return group_name, None

            def _resolve_action(self, action_name, mandatory=True):
                if action_name == 'ansible.legacy.ping':
                    return 'ansible.legacy.ping'
                elif action_name == 'ansible.builtin.ping':
                    return 'ansible.builtin.ping'
                return None

        return DummyFieldAttributeBase()

    def test_load_module_defaults_none(self, field_attribute_base):
        result = field_attribute_base._load_module_defaults('module_defaults', None)
        assert result is None

    def test_load_module_defaults_not_list(self, field_attribute_base):
        result = field_attribute_base._load_module_defaults('module_defaults', {'ping': 'pong'})
        assert result == [{'ansible.legacy.ping': 'pong', 'ansible.builtin.ping': 'pong'}]

    def test_load_module_defaults_invalid_dict(self, field_attribute_base):
        with pytest.raises(AnsibleParserError):
            field_attribute_base._load_module_defaults('module_defaults', ['invalid'])

    def test_load_module_defaults_group(self, field_attribute_base):
        result = field_attribute_base._load_module_defaults('module_defaults', [{'group/test_group': 'defaults'}])
        assert result == [{'group/test_group': 'defaults'}]

    def test_load_module_defaults_action(self, field_attribute_base):
        result = field_attribute_base._load_module_defaults('module_defaults', [{'ping': 'pong'}])
        assert result == [{'ansible.legacy.ping': 'pong', 'ansible.builtin.ping': 'pong'}]

    def test_load_module_defaults_action_with_prefix(self, field_attribute_base):
        result = field_attribute_base._load_module_defaults('module_defaults', [{'ansible.legacy.ping': 'pong'}])
        assert result == [{'ansible.legacy.ping': 'pong', 'ansible.builtin.ping': 'pong'}]
