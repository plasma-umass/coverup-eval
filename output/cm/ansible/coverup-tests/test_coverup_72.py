# file lib/ansible/cli/doc.py:134-166
# lines [134, 145, 146, 148, 149, 150, 153, 154, 157, 158, 159, 160, 161, 162, 163, 165, 166]
# branches ['148->149', '148->166', '149->150', '149->153', '153->148', '153->154', '157->153', '157->158', '159->157', '159->160', '160->161', '160->165', '161->162', '161->163']

import os
import pytest
from ansible.cli.doc import RoleMixin

# Define a fixture to create a temporary directory structure for roles
@pytest.fixture
def role_dir(tmp_path):
    roles_path = tmp_path / "roles"
    roles_path.mkdir()
    # Create a role with a meta/main.yml file
    role1 = roles_path / "role1"
    role1.mkdir()
    (role1 / "meta").mkdir()
    (role1 / "meta" / "main.yml").touch()
    # Create a role without a meta/main.yml file
    role2 = roles_path / "role2"
    role2.mkdir()
    (role2 / "meta").mkdir()
    # Create a role with a meta/.galaxy_install_info file
    role3 = roles_path / "role3"
    role3.mkdir()
    (role3 / "meta").mkdir()
    (role3 / "meta" / ".galaxy_install_info").touch()
    return roles_path

# Define the test function
def test_find_all_normal_roles(role_dir, mocker):
    mocker.patch.object(RoleMixin, 'ROLE_ARGSPEC_FILES', new=['main.yml', '.galaxy_install_info'])

    role_mixin = RoleMixin()
    found_roles = role_mixin._find_all_normal_roles((str(role_dir),), name_filters=None)

    # Assert that the correct roles are found
    assert ('role1', str(role_dir / 'role1')) in found_roles
    assert ('role2', str(role_dir / 'role2')) not in found_roles
    assert ('role3', str(role_dir / 'role3')) in found_roles

    # Now test with name filters
    found_roles_filtered = role_mixin._find_all_normal_roles((str(role_dir),), name_filters=('role1',))
    assert ('role1', str(role_dir / 'role1')) in found_roles_filtered
    assert ('role3', str(role_dir / 'role3')) not in found_roles_filtered

    # Cleanup is handled by pytest's tmp_path fixture
