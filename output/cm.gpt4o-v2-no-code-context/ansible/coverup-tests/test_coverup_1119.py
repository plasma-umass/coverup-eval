# file: lib/ansible/parsing/mod_args.py:222-258
# asked: {"lines": [], "branches": [[241, 258]]}
# gained: {"lines": [], "branches": [[241, 258]]}

import pytest
from ansible.parsing.mod_args import ModuleArgsParser
from ansible.errors import AnsibleParserError
from ansible.module_utils.common.text.converters import to_text

class TestModuleArgsParser:
    
    def setup_method(self):
        self.parser = ModuleArgsParser()

    def test_normalize_old_style_args_with_module_key(self):
        input_data = {'module': 'shell echo hi'}
        action, args = self.parser._normalize_old_style_args(input_data)
        assert action == 'shell'
        assert args == {'_raw_params': 'echo hi'}

    def test_normalize_old_style_args_with_string(self):
        input_data = 'shell echo hi'
        action, args = self.parser._normalize_old_style_args(input_data)
        assert action == 'shell'
        assert args == {'_raw_params': 'echo hi'}

    def test_normalize_old_style_args_with_invalid_type(self):
        input_data = 12345
        with pytest.raises(AnsibleParserError):
            self.parser._normalize_old_style_args(input_data)

    def test_normalize_old_style_args_with_dict_without_module_key(self):
        input_data = {'action': 'copy', 'src': 'a', 'dest': 'b'}
        action, args = self.parser._normalize_old_style_args(input_data)
        assert action is None
        assert args is None
