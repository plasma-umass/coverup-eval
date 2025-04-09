# file: lib/ansible/cli/doc.py:88-132
# asked: {"lines": [109], "branches": [[108, 109]]}
# gained: {"lines": [109], "branches": [[108, 109]]}

import os
import pytest
from unittest.mock import mock_open, patch
from ansible.errors import AnsibleError, AnsibleParserError
from ansible.module_utils._text import to_native
from ansible.parsing.utils.yaml import from_yaml
from ansible.cli.doc import RoleMixin

class TestRoleMixin:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.mixin = RoleMixin()
        self.mixin.ROLE_ARGSPEC_FILES = ['argument_spec.yml', 'main.yml']

    def test_load_argspec_no_path(self):
        with pytest.raises(AnsibleError, match="A path is required to load argument specs for role 'test_role'"):
            self.mixin._load_argspec('test_role')

    def test_load_argspec_collection_path(self, monkeypatch):
        collection_path = '/fake/collection/path'
        role_name = 'test_role'
        meta_path = os.path.join(collection_path, 'roles', role_name, 'meta')
        specfile_path = os.path.join(meta_path, 'argument_spec.yml')

        monkeypatch.setattr(os.path, 'exists', lambda x: x == specfile_path)
        with patch('builtins.open', mock_open(read_data="argument_specs: {'key': 'value'}")):
            result = self.mixin._load_argspec(role_name, collection_path=collection_path)
            assert result == {'key': 'value'}

    def test_load_argspec_role_path(self, monkeypatch):
        role_path = '/fake/role/path'
        role_name = 'test_role'
        meta_path = os.path.join(role_path, 'meta')
        specfile_path = os.path.join(meta_path, 'argument_spec.yml')

        monkeypatch.setattr(os.path, 'exists', lambda x: x == specfile_path)
        with patch('builtins.open', mock_open(read_data="argument_specs: {'key': 'value'}")):
            result = self.mixin._load_argspec(role_name, role_path=role_path)
            assert result == {'key': 'value'}

    def test_load_argspec_no_spec_file(self, monkeypatch):
        collection_path = '/fake/collection/path'
        role_name = 'test_role'

        monkeypatch.setattr(os.path, 'exists', lambda x: False)
        result = self.mixin._load_argspec(role_name, collection_path=collection_path)
        assert result == {}

    def test_load_argspec_io_error(self, monkeypatch):
        collection_path = '/fake/collection/path'
        role_name = 'test_role'
        meta_path = os.path.join(collection_path, 'roles', role_name, 'meta')
        specfile_path = os.path.join(meta_path, 'argument_spec.yml')

        monkeypatch.setattr(os.path, 'exists', lambda x: x == specfile_path)
        with patch('builtins.open', mock_open()) as mocked_open:
            mocked_open.side_effect = IOError("Unable to open file")
            with pytest.raises(AnsibleParserError, match="An error occurred while trying to read the file"):
                self.mixin._load_argspec(role_name, collection_path=collection_path)
