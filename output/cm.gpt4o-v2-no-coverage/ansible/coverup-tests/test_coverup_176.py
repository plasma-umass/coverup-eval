# file: lib/ansible/cli/doc.py:304-329
# asked: {"lines": [304, 312, 313, 315, 317, 318, 319, 320, 321, 323, 324, 325, 326, 327, 329], "branches": [[317, 318], [317, 323], [320, 317], [320, 321], [323, 324], [323, 329], [326, 323], [326, 327]]}
# gained: {"lines": [304, 312, 313, 315, 317, 318, 319, 320, 321, 323, 324, 325, 326, 327, 329], "branches": [[317, 318], [317, 323], [320, 321], [323, 324], [323, 329], [326, 327]]}

import pytest
from unittest.mock import patch, mock_open
from ansible.cli.doc import RoleMixin

class TestRoleMixin:

    @patch('os.path.isdir', return_value=True)
    @patch('os.listdir', return_value=['role1', 'role2'])
    @patch('os.path.exists', return_value=True)
    def test_create_role_doc_normal_roles(self, mock_exists, mock_listdir, mock_isdir, monkeypatch):
        class MockRoleMixin(RoleMixin):
            ROLE_ARGSPEC_FILES = ['main.yml', 'argument_spec.yml']

            def _find_all_normal_roles(self, role_paths, name_filters=None):
                return {('role1', '/path/to/role1'), ('role2', '/path/to/role2')}

            def _find_all_collection_roles(self, name_filters=None):
                return set()

            def _load_argspec(self, role, role_path=None, collection_path=None):
                return {'main': {'param1': 'value1'}}

            def _build_doc(self, role, path, collection, argspec, entry_point):
                return (role, {'path': path, 'collection': collection, 'entry_points': argspec})

        mixin = MockRoleMixin()
        result = mixin._create_role_doc(('role1', 'role2'), ('/path/to/roles',))
        assert 'role1' in result
        assert 'role2' in result
        assert result['role1']['path'] == '/path/to/role1'
        assert result['role2']['path'] == '/path/to/role2'

    @patch('os.path.isdir', return_value=True)
    @patch('os.listdir', return_value=['role1', 'role2'])
    @patch('os.path.exists', return_value=True)
    def test_create_role_doc_collection_roles(self, mock_exists, mock_listdir, mock_isdir, monkeypatch):
        class MockRoleMixin(RoleMixin):
            ROLE_ARGSPEC_FILES = ['main.yml', 'argument_spec.yml']

            def _find_all_normal_roles(self, role_paths, name_filters=None):
                return set()

            def _find_all_collection_roles(self, name_filters=None):
                return {('role1', 'collection1', '/path/to/collection1'), ('role2', 'collection2', '/path/to/collection2')}

            def _load_argspec(self, role, role_path=None, collection_path=None):
                return {'main': {'param1': 'value1'}}

            def _build_doc(self, role, path, collection, argspec, entry_point):
                return (f"{collection}.{role}", {'path': path, 'collection': collection, 'entry_points': argspec})

        mixin = MockRoleMixin()
        result = mixin._create_role_doc(('role1', 'role2'), ('/path/to/roles',))
        assert 'collection1.role1' in result
        assert 'collection2.role2' in result
        assert result['collection1.role1']['path'] == '/path/to/collection1'
        assert result['collection2.role2']['path'] == '/path/to/collection2'

    @patch('os.path.isdir', return_value=True)
    @patch('os.listdir', return_value=['role1', 'role2'])
    @patch('os.path.exists', return_value=True)
    def test_create_role_doc_mixed_roles(self, mock_exists, mock_listdir, mock_isdir, monkeypatch):
        class MockRoleMixin(RoleMixin):
            ROLE_ARGSPEC_FILES = ['main.yml', 'argument_spec.yml']

            def _find_all_normal_roles(self, role_paths, name_filters=None):
                return {('role1', '/path/to/role1')}

            def _find_all_collection_roles(self, name_filters=None):
                return {('role2', 'collection2', '/path/to/collection2')}

            def _load_argspec(self, role, role_path=None, collection_path=None):
                return {'main': {'param1': 'value1'}}

            def _build_doc(self, role, path, collection, argspec, entry_point):
                if collection:
                    fqcn = f"{collection}.{role}"
                else:
                    fqcn = role
                return (fqcn, {'path': path, 'collection': collection, 'entry_points': argspec})

        mixin = MockRoleMixin()
        result = mixin._create_role_doc(('role1', 'role2'), ('/path/to/roles',))
        assert 'role1' in result
        assert 'collection2.role2' in result
        assert result['role1']['path'] == '/path/to/role1'
        assert result['collection2.role2']['path'] == '/path/to/collection2'
