# file lib/ansible/utils/collection_loader/_collection_finder.py:324-325
# lines [324, 325]
# branches []

import os
import pytest
from unittest import mock

# Assuming the class is imported from the module
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase

class TestAnsibleCollectionPkgLoaderBase:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        # Setup: Create a mock for the _package_to_load attribute
        self.loader = _AnsibleCollectionPkgLoaderBase.__new__(_AnsibleCollectionPkgLoaderBase)
        self.loader._package_to_load = 'test_package'
        yield
        # Teardown: Clean up if necessary (none needed in this case)

    def test_get_candidate_paths(self):
        # Mock the os.path.join to ensure it is called correctly
        with mock.patch('os.path.join', side_effect=lambda p, pkg: f"{p}/{pkg}") as mock_join:
            path_list = ['/path/one', '/path/two']
            expected_paths = ['/path/one/test_package', '/path/two/test_package']
            candidate_paths = self.loader._get_candidate_paths(path_list)
            
            # Assertions to verify the correct paths are generated
            assert candidate_paths == expected_paths
            assert mock_join.call_count == len(path_list)
            for path in path_list:
                mock_join.assert_any_call(path, 'test_package')
