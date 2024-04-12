# file lib/ansible/cli/doc.py:168-208
# lines [182, 183, 184, 185, 186, 188, 189, 190, 193, 194, 195, 196, 197, 200, 201, 202, 203, 204, 205, 206, 207, 208]
# branches ['184->185', '184->208', '189->184', '189->190', '190->184', '190->193', '193->190', '193->194', '195->193', '195->196', '196->197', '196->200', '200->201', '200->207', '201->202', '201->205', '203->200', '203->204', '205->200', '205->206']

import os
import pytest
from ansible.cli.doc import RoleMixin
from unittest.mock import MagicMock
from shutil import rmtree

# Define a test class to encapsulate the tests
class TestRoleMixin:

    # Define a pytest fixture to create a temporary directory structure
    @pytest.fixture
    def role_mixin_setup(self, tmp_path):
        # Create a collection directory structure
        collection_path = tmp_path / 'collections' / 'ansible_collections' / 'namespace' / 'collection'
        roles_dir = collection_path / 'roles' / 'testrole' / 'meta'
        roles_dir.mkdir(parents=True)
        spec_file = roles_dir / 'main.yml'
        spec_file.touch()

        # Mock the functions called by _find_all_collection_roles
        with pytest.MonkeyPatch.context() as m:
            m.setattr(RoleMixin, 'ROLE_ARGSPEC_FILES', ('main.yml',))
            m.setattr('ansible.cli.doc.list_collection_dirs', MagicMock(return_value=[str(collection_path)]))
            m.setattr('ansible.cli.doc._get_collection_name_from_path', MagicMock(return_value='namespace.collection'))
            m.setattr('ansible.cli.doc.to_text', MagicMock(side_effect=lambda x, errors: x))

            yield collection_path, 'namespace.collection.testrole'

        # Cleanup after the test
        if tmp_path.exists():
            rmtree(tmp_path)

    # Define the test function
    def test_find_all_collection_roles(self, role_mixin_setup):
        collection_path, expected_role_fqcn = role_mixin_setup
        role_mixin = RoleMixin()

        # Call the method under test
        found_roles = role_mixin._find_all_collection_roles()

        # Assert that the expected role is found
        assert (expected_role_fqcn.split('.')[-1], 'namespace.collection', str(collection_path)) in found_roles

        # Call the method under test with name_filters
        found_roles_filtered = role_mixin._find_all_collection_roles(name_filters=(expected_role_fqcn,))

        # Assert that the expected role is found with name_filters
        assert (expected_role_fqcn.split('.')[-1], 'namespace.collection', str(collection_path)) in found_roles_filtered

        # Call the method under test with collection_filter
        found_roles_collection_filtered = role_mixin._find_all_collection_roles(collection_filter='namespace.collection')

        # Assert that the expected role is found with collection_filter
        assert (expected_role_fqcn.split('.')[-1], 'namespace.collection', str(collection_path)) in found_roles_collection_filtered
