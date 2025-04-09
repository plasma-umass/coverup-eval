# file: lib/ansible/cli/doc.py:168-208
# asked: {"lines": [182, 183, 184, 185, 186, 188, 189, 190, 193, 194, 195, 196, 197, 200, 201, 202, 203, 204, 205, 206, 207, 208], "branches": [[184, 185], [184, 208], [189, 184], [189, 190], [190, 184], [190, 193], [193, 190], [193, 194], [195, 193], [195, 196], [196, 197], [196, 200], [200, 201], [200, 207], [201, 202], [201, 205], [203, 200], [203, 204], [205, 200], [205, 206]]}
# gained: {"lines": [182, 183, 184, 185, 186, 188, 189, 190, 193, 194, 195, 196, 197, 200, 201, 202, 203, 204, 205, 206, 207, 208], "branches": [[184, 185], [184, 208], [189, 190], [190, 184], [190, 193], [193, 194], [195, 196], [196, 197], [196, 200], [200, 201], [200, 207], [201, 202], [201, 205], [203, 200], [203, 204], [205, 200], [205, 206]]}

import os
import pytest
from unittest.mock import patch, MagicMock

# Assuming the RoleMixin class is defined in a module named ansible.cli.doc
from ansible.cli.doc import RoleMixin

class TestRoleMixin:
    @pytest.fixture
    def role_mixin(self):
        return RoleMixin()

    @pytest.fixture
    def mock_list_collection_dirs(self, monkeypatch):
        mock = MagicMock(return_value=['/fake/path/collection1', '/fake/path/collection2'])
        monkeypatch.setattr('ansible.cli.doc.list_collection_dirs', mock)
        return mock

    @pytest.fixture
    def mock_get_collection_name_from_path(self, monkeypatch):
        def side_effect(path):
            return 'namespace.collection1' if 'collection1' in path else 'namespace.collection2'
        mock = MagicMock(side_effect=side_effect)
        monkeypatch.setattr('ansible.cli.doc._get_collection_name_from_path', mock)
        return mock

    @pytest.fixture
    def mock_os_path_exists(self, monkeypatch):
        def side_effect(path):
            if 'roles' in path:
                return True
            if 'meta' in path and 'argspec.yml' in path:
                return True
            return False
        mock = MagicMock(side_effect=side_effect)
        monkeypatch.setattr('os.path.exists', mock)
        return mock

    @pytest.fixture
    def mock_os_listdir(self, monkeypatch):
        mock = MagicMock(return_value=['roleA', 'roleB'])
        monkeypatch.setattr('os.listdir', mock)
        return mock

    def test_find_all_collection_roles_no_filters(self, role_mixin, mock_list_collection_dirs, mock_get_collection_name_from_path, mock_os_path_exists, mock_os_listdir):
        role_mixin.ROLE_ARGSPEC_FILES = ['argspec.yml']
        result = role_mixin._find_all_collection_roles()
        expected = {('roleA', 'namespace.collection1', '/fake/path/collection1'),
                    ('roleB', 'namespace.collection1', '/fake/path/collection1'),
                    ('roleA', 'namespace.collection2', '/fake/path/collection2'),
                    ('roleB', 'namespace.collection2', '/fake/path/collection2')}
        assert result == expected

    def test_find_all_collection_roles_with_name_filters(self, role_mixin, mock_list_collection_dirs, mock_get_collection_name_from_path, mock_os_path_exists, mock_os_listdir):
        role_mixin.ROLE_ARGSPEC_FILES = ['argspec.yml']
        result = role_mixin._find_all_collection_roles(name_filters=('roleA', 'namespace.collection2.roleB'))
        expected = {('roleA', 'namespace.collection1', '/fake/path/collection1'),
                    ('roleA', 'namespace.collection2', '/fake/path/collection2'),
                    ('roleB', 'namespace.collection2', '/fake/path/collection2')}
        assert result == expected

    def test_find_all_collection_roles_with_collection_filter(self, role_mixin, mock_list_collection_dirs, mock_get_collection_name_from_path, mock_os_path_exists, mock_os_listdir):
        role_mixin.ROLE_ARGSPEC_FILES = ['argspec.yml']
        mock_list_collection_dirs.return_value = ['/fake/path/collection1']
        result = role_mixin._find_all_collection_roles(collection_filter='namespace.collection1')
        expected = {('roleA', 'namespace.collection1', '/fake/path/collection1'),
                    ('roleB', 'namespace.collection1', '/fake/path/collection1')}
        assert result == expected
