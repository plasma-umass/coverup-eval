# file lib/ansible/plugins/become/runas.py:64-70
# lines [64, 66, 68, 70]
# branches []

import pytest
from ansible.plugins.become import runas

# Mocking the BecomeBase class to avoid side effects on other tests
@pytest.fixture
def mock_become_base(mocker):
    mocker.patch('ansible.plugins.become.runas.BecomeBase')

def test_build_become_command():
    # Instantiate the BecomeModule class
    become_module = runas.BecomeModule()

    # Define a dummy command and shell
    dummy_cmd = ['echo', 'hello']
    dummy_shell = 'powershell'

    # Call the build_become_command method
    result = become_module.build_become_command(dummy_cmd, dummy_shell)

    # Assert that the result is the same as the dummy command
    assert result == dummy_cmd

# Run the test function
def test_runas_build_become_command(mock_become_base):
    test_build_become_command()
