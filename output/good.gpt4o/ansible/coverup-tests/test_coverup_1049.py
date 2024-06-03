# file lib/ansible/cli/doc.py:88-132
# lines [106, 107, 108, 109, 111, 113, 116, 117, 118, 119, 120, 122, 123, 125, 126, 127, 128, 129, 130, 131, 132]
# branches ['106->107', '106->108', '108->109', '108->111', '116->117', '116->122', '118->116', '118->119', '122->123', '122->125', '128->129', '128->130']

import os
import pytest
from unittest import mock
from ansible.errors import AnsibleError, AnsibleParserError
from ansible.cli.doc import RoleMixin

class TestRoleMixin(RoleMixin):
    ROLE_ARGSPEC_FILES = ['argument_spec.yml', 'main.yml']

@pytest.fixture
def role_mixin():
    return TestRoleMixin()

def test_load_argspec_with_collection_path(role_mixin, mocker):
    role_name = 'test_role'
    collection_path = '/fake/collection/path'
    meta_path = os.path.join(collection_path, 'roles', role_name, 'meta')
    specfile_path = os.path.join(meta_path, 'argument_spec.yml')

    mocker.patch('os.path.exists', return_value=True)
    mocker.patch('builtins.open', mock.mock_open(read_data='argument_specs: {}'))
    mocker.patch('ansible.cli.doc.from_yaml', return_value={'argument_specs': {'key': 'value'}})

    result = role_mixin._load_argspec(role_name, collection_path=collection_path)
    assert result == {'key': 'value'}

def test_load_argspec_with_role_path(role_mixin, mocker):
    role_name = 'test_role'
    role_path = '/fake/role/path'
    meta_path = os.path.join(role_path, 'meta')
    specfile_path = os.path.join(meta_path, 'argument_spec.yml')

    mocker.patch('os.path.exists', return_value=True)
    mocker.patch('builtins.open', mock.mock_open(read_data='argument_specs: {}'))
    mocker.patch('ansible.cli.doc.from_yaml', return_value={'argument_specs': {'key': 'value'}})

    result = role_mixin._load_argspec(role_name, role_path=role_path)
    assert result == {'key': 'value'}

def test_load_argspec_no_path(role_mixin):
    role_name = 'test_role'
    with pytest.raises(AnsibleError, match="A path is required to load argument specs for role 'test_role'"):
        role_mixin._load_argspec(role_name)

def test_load_argspec_file_not_found(role_mixin, mocker):
    role_name = 'test_role'
    collection_path = '/fake/collection/path'

    mocker.patch('os.path.exists', return_value=False)

    result = role_mixin._load_argspec(role_name, collection_path=collection_path)
    assert result == {}

def test_load_argspec_file_read_error(role_mixin, mocker):
    role_name = 'test_role'
    collection_path = '/fake/collection/path'
    meta_path = os.path.join(collection_path, 'roles', role_name, 'meta')
    specfile_path = os.path.join(meta_path, 'argument_spec.yml')

    mocker.patch('os.path.exists', return_value=True)
    mocker.patch('builtins.open', side_effect=IOError("File read error"))

    with pytest.raises(AnsibleParserError, match="An error occurred while trying to read the file"):
        role_mixin._load_argspec(role_name, collection_path=collection_path)
