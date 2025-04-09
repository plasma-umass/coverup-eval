# file: lib/ansible/cli/doc.py:88-132
# asked: {"lines": [88, 106, 107, 108, 109, 111, 113, 116, 117, 118, 119, 120, 122, 123, 125, 126, 127, 128, 129, 130, 131, 132], "branches": [[106, 107], [106, 108], [108, 109], [108, 111], [116, 117], [116, 122], [118, 116], [118, 119], [122, 123], [122, 125], [128, 129], [128, 130]]}
# gained: {"lines": [88, 106, 107, 108, 111, 113, 116, 117, 118, 119, 120, 122, 123, 125, 126, 127, 128, 129, 130, 131, 132], "branches": [[106, 107], [106, 108], [108, 111], [116, 117], [116, 122], [118, 116], [118, 119], [122, 123], [122, 125], [128, 129], [128, 130]]}

import os
import pytest
from unittest.mock import mock_open, patch
from ansible.errors import AnsibleError, AnsibleParserError
from ansible.module_utils._text import to_native
from ansible.parsing.utils.yaml import from_yaml
from ansible.cli.doc import RoleMixin

class TestRoleMixin:
    @pytest.fixture
    def role_mixin(self):
        class TestRole(RoleMixin):
            ROLE_ARGSPEC_FILES = ['argument_spec.yml', 'main.yml']
        return TestRole()

    def test_load_argspec_no_path(self, role_mixin):
        with pytest.raises(AnsibleError, match="A path is required to load argument specs for role 'test_role'"):
            role_mixin._load_argspec('test_role')

    def test_load_argspec_no_spec_file(self, role_mixin, monkeypatch):
        monkeypatch.setattr(os.path, 'exists', lambda x: False)
        result = role_mixin._load_argspec('test_role', collection_path='/fake/collection/path')
        assert result == {}

    def test_load_argspec_with_spec_file(self, role_mixin, monkeypatch):
        mock_data = {'argument_specs': {'key': 'value'}}
        monkeypatch.setattr(os.path, 'exists', lambda x: True)
        monkeypatch.setattr('builtins.open', mock_open(read_data='argument_specs:\n  key: value'))
        monkeypatch.setattr('ansible.parsing.utils.yaml.from_yaml', lambda x, file_name: mock_data)
        
        result = role_mixin._load_argspec('test_role', collection_path='/fake/collection/path')
        assert result == {'key': 'value'}

    def test_load_argspec_with_empty_spec_file(self, role_mixin, monkeypatch):
        monkeypatch.setattr(os.path, 'exists', lambda x: True)
        monkeypatch.setattr('builtins.open', mock_open(read_data=''))
        monkeypatch.setattr('ansible.parsing.utils.yaml.from_yaml', lambda x, file_name: None)
        
        result = role_mixin._load_argspec('test_role', collection_path='/fake/collection/path')
        assert result == {}

    def test_load_argspec_io_error(self, role_mixin, monkeypatch):
        monkeypatch.setattr(os.path, 'exists', lambda x: True)
        monkeypatch.setattr('builtins.open', mock_open())
        monkeypatch.setattr('builtins.open', lambda *args, **kwargs: (_ for _ in ()).throw(IOError("File error")))
        
        with pytest.raises(AnsibleParserError, match="An error occurred while trying to read the file"):
            role_mixin._load_argspec('test_role', collection_path='/fake/collection/path')
