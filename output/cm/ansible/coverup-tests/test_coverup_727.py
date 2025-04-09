# file lib/ansible/playbook/role/requirement.py:125-128
# lines [125, 126, 128]
# branches []

import pytest
from ansible.playbook.role.requirement import RoleRequirement
from unittest.mock import patch

# Assuming that the scm_archive_resource function is defined elsewhere in the codebase
# and that it performs some kind of operation to archive a role from a source control system.

# Mock the scm_archive_resource function to control its behavior for testing
@pytest.fixture
def mock_scm_archive_resource(mocker):
    return mocker.patch('ansible.playbook.role.requirement.scm_archive_resource')

# Test function to cover the scm_archive_role static method
def test_scm_archive_role(mock_scm_archive_resource):
    # Setup the expected values
    src = "fake_repo_url"
    scm = "git"
    name = "fake_role_name"
    version = "v1.0.0"
    keep_scm_meta = True

    # Call the static method with the test values
    RoleRequirement.scm_archive_role(src, scm, name, version, keep_scm_meta)

    # Assert that the scm_archive_resource function was called with the correct arguments
    mock_scm_archive_resource.assert_called_once_with(src, scm=scm, name=name, version=version, keep_scm_meta=keep_scm_meta)

    # Since scm_archive_resource is mocked, we don't need to clean up any actual resources
