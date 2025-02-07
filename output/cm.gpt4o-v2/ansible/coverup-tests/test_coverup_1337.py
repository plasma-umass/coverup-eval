# file: lib/ansible/cli/doc.py:88-132
# asked: {"lines": [106, 107, 108, 109, 111, 113, 116, 117, 118, 119, 120, 122, 123, 125, 126, 127, 128, 129, 130, 131, 132], "branches": [[106, 107], [106, 108], [108, 109], [108, 111], [116, 117], [116, 122], [118, 116], [118, 119], [122, 123], [122, 125], [128, 129], [128, 130]]}
# gained: {"lines": [106, 107, 108, 109, 111, 113, 116, 117, 118, 119, 120, 122, 123, 125, 126, 127, 128, 130, 131, 132], "branches": [[106, 107], [106, 108], [108, 109], [108, 111], [116, 117], [116, 122], [118, 116], [118, 119], [122, 123], [122, 125], [128, 130]]}

import os
import pytest
from unittest.mock import mock_open, patch
from ansible.errors import AnsibleError, AnsibleParserError
from ansible.module_utils._text import to_native
from ansible.parsing.utils.yaml import from_yaml
from ansible.cli.doc import RoleMixin

class TestRoleMixin(RoleMixin):
    ROLE_ARGSPEC_FILES = ['argument_spec.yml', 'main.yml']

@pytest.fixture
def role_mixin():
    return TestRoleMixin()

def test_load_argspec_no_path(role_mixin):
    with pytest.raises(AnsibleError, match="A path is required to load argument specs for role 'test_role'"):
        role_mixin._load_argspec('test_role')

def test_load_argspec_collection_path(role_mixin, monkeypatch):
    collection_path = '/fake/collection/path'
    role_name = 'test_role'
    meta_path = os.path.join(collection_path, 'roles', role_name, 'meta')
    specfile = 'argument_spec.yml'
    full_path = os.path.join(meta_path, specfile)

    monkeypatch.setattr(os.path, 'exists', lambda x: x == full_path)
    monkeypatch.setattr('builtins.open', mock_open(read_data="argument_specs: {}"))

    result = role_mixin._load_argspec(role_name, collection_path=collection_path)
    assert result == {}

def test_load_argspec_role_path(role_mixin, monkeypatch):
    role_path = '/fake/role/path'
    role_name = 'test_role'
    meta_path = os.path.join(role_path, 'meta')
    specfile = 'argument_spec.yml'
    full_path = os.path.join(meta_path, specfile)

    monkeypatch.setattr(os.path, 'exists', lambda x: x == full_path)
    monkeypatch.setattr('builtins.open', mock_open(read_data="argument_specs: {}"))

    result = role_mixin._load_argspec(role_name, role_path=role_path)
    assert result == {}

def test_load_argspec_no_spec_file(role_mixin, monkeypatch):
    role_path = '/fake/role/path'
    role_name = 'test_role'
    meta_path = os.path.join(role_path, 'meta')

    monkeypatch.setattr(os.path, 'exists', lambda x: False)

    result = role_mixin._load_argspec(role_name, role_path=role_path)
    assert result == {}

def test_load_argspec_file_read_error(role_mixin, monkeypatch):
    role_path = '/fake/role/path'
    role_name = 'test_role'
    meta_path = os.path.join(role_path, 'meta')
    specfile = 'argument_spec.yml'
    full_path = os.path.join(meta_path, specfile)

    monkeypatch.setattr(os.path, 'exists', lambda x: x == full_path)
    monkeypatch.setattr('builtins.open', mock_open(read_data="argument_specs: {}"))
    monkeypatch.setattr('builtins.open', lambda *args, **kwargs: (_ for _ in ()).throw(OSError("File read error")))

    with pytest.raises(AnsibleParserError, match="An error occurred while trying to read the file"):
        role_mixin._load_argspec(role_name, role_path=role_path)
