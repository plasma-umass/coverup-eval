# file lib/ansible/plugins/loader.py:1132-1145
# lines [1136, 1137, 1138, 1140, 1143, 1145]
# branches ['1133->1136', '1136->1137', '1136->1140']

import pytest
from ansible.plugins.loader import _does_collection_support_ansible_version
from ansible.utils.display import Display

@pytest.fixture
def mock_display(mocker):
    return mocker.patch.object(Display, 'warning')

def test_does_collection_support_ansible_version_without_packaging(mock_display, mocker):
    # Simulate the absence of SpecifierSet by setting it to None
    mocker.patch('ansible.plugins.loader.SpecifierSet', None)
    assert _does_collection_support_ansible_version(">=2.9", "2.9.10")
    mock_display.assert_called_once_with('packaging Python module unavailable; unable to validate collection Ansible version requirements')
