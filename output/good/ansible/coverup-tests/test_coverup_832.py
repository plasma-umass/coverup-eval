# file lib/ansible/modules/apt_repository.py:454-456
# lines [454, 455, 456]
# branches []

import pytest
from ansible.modules.apt_repository import UbuntuSourcesList
from ansible.module_utils.basic import AnsibleModule

# Mock AnsibleModule to avoid side effects
@pytest.fixture
def mock_module(mocker):
    mock = mocker.MagicMock(spec=AnsibleModule)
    mock.run_command = mocker.MagicMock()
    mock.params = {'codename': 'focal'}  # Add a fake codename parameter
    return mock

# Mock apt_pkg to avoid side effects
@pytest.fixture
def mock_apt_pkg(mocker):
    apt_pkg_mock = mocker.patch('ansible.modules.apt_repository.apt_pkg', create=True)
    apt_pkg_mock.config.find_file = mocker.MagicMock(return_value='/etc/apt/sources.list')
    return apt_pkg_mock

# Test function to cover _key_already_exists method
def test_key_already_exists(mock_module, mock_apt_pkg, mocker):
    # Setup the mock for run_command
    mock_module.run_command.return_value = (0, '', 'error message')

    # Instantiate UbuntuSourcesList with the mocked module
    sources_list = UbuntuSourcesList(mock_module)

    # Call the method with a fake key fingerprint
    result = sources_list._key_already_exists('FAKE_KEY_FINGERPRINT')

    # Assert that the method returns False when there is an error message
    assert not result

    # Change the mock to simulate no error message
    mock_module.run_command.return_value = (0, '', '')

    # Call the method again with a fake key fingerprint
    result = sources_list._key_already_exists('FAKE_KEY_FINGERPRINT')

    # Assert that the method returns True when there is no error message
    assert result

    # Verify that run_command was called twice
    assert mock_module.run_command.call_count == 2

    # Verify that run_command was called with the correct arguments
    mock_module.run_command.assert_any_call('apt-key export FAKE_KEY_FINGERPRINT', check_rc=True)
