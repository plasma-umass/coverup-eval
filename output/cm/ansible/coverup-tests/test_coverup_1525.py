# file lib/ansible/cli/doc.py:88-132
# lines [106, 107, 108, 109, 111, 113, 116, 117, 118, 119, 120, 122, 123, 125, 126, 127, 128, 129, 130, 131, 132]
# branches ['106->107', '106->108', '108->109', '108->111', '116->117', '116->122', '118->116', '118->119', '122->123', '122->125', '128->129', '128->130']

import os
import pytest
from ansible.errors import AnsibleError, AnsibleParserError
from ansible.cli.doc import RoleMixin
from ansible.parsing.yaml.loader import AnsibleLoader

# Assuming ROLE_ARGSPEC_FILES is defined somewhere in the RoleMixin
# If not, you would need to define it accordingly for the test to work
RoleMixin.ROLE_ARGSPEC_FILES = ['argument_spec.yml', 'main.yml']

def from_yaml(data, file_name=None):
    loader = AnsibleLoader(data, file_name=file_name)
    try:
        return loader.get_single_data()
    finally:
        loader.dispose()

def test_role_mixin_load_argspec_missing_path(mocker, tmp_path):
    role_mixin = RoleMixin()
    role_name = 'testrole'
    with pytest.raises(AnsibleError):
        role_mixin._load_argspec(role_name)

def test_role_mixin_load_argspec_with_collection_path(mocker, tmp_path):
    role_mixin = RoleMixin()
    role_name = 'testrole'
    collection_path = str(tmp_path / 'collections' / 'ansible_collections' / 'namespace' / 'collection')
    os.makedirs(os.path.join(collection_path, 'roles', role_name, 'meta'))
    mocker.patch('os.path.exists', return_value=False)
    assert role_mixin._load_argspec(role_name, collection_path=collection_path) == {}

def test_role_mixin_load_argspec_with_role_path(mocker, tmp_path):
    role_mixin = RoleMixin()
    role_name = 'testrole'
    role_path = str(tmp_path / 'roles' / role_name)
    os.makedirs(os.path.join(role_path, 'meta'))
    mocker.patch('os.path.exists', return_value=False)
    assert role_mixin._load_argspec(role_name, role_path=role_path) == {}

def test_role_mixin_load_argspec_with_existing_spec(mocker, tmp_path):
    role_mixin = RoleMixin()
    role_name = 'testrole'
    role_path = str(tmp_path / 'roles' / role_name)
    meta_path = os.path.join(role_path, 'meta')
    os.makedirs(meta_path)
    spec_file = os.path.join(meta_path, 'argument_spec.yml')
    with open(spec_file, 'w') as f:
        f.write('argument_specs:\n  key: value\n')
    mocker.patch('os.path.exists', return_value=True)
    assert role_mixin._load_argspec(role_name, role_path=role_path) == {'key': 'value'}

def test_role_mixin_load_argspec_with_ioerror(mocker, tmp_path):
    role_mixin = RoleMixin()
    role_name = 'testrole'
    role_path = str(tmp_path / 'roles' / role_name)
    meta_path = os.path.join(role_path, 'meta')
    os.makedirs(meta_path)
    spec_file = os.path.join(meta_path, 'argument_spec.yml')
    with open(spec_file, 'w') as f:
        f.write('argument_specs:\n  key: value\n')
    mocker.patch('os.path.exists', return_value=True)
    mocker.patch('builtins.open', mocker.mock_open(read_data='argument_specs:\n  key: value\n'))
    mocker.patch('builtins.open', side_effect=IOError("Test IOError"))
    with pytest.raises(AnsibleParserError):
        role_mixin._load_argspec(role_name, role_path=role_path)
