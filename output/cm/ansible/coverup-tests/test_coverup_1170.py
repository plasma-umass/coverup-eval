# file lib/ansible/module_utils/facts/virtual/openbsd.py:27-69
# lines [37, 38, 39, 42, 43, 45, 46, 47, 48, 50, 51, 52, 54, 55, 59, 60, 61, 62, 63, 64, 65, 67, 68, 69]
# branches ['54->55', '54->59', '60->61', '60->67', '62->60', '62->63']

import pytest
from unittest.mock import MagicMock

# Assuming the OpenBSDVirtual class is imported from the appropriate module
from ansible.module_utils.facts.virtual.openbsd import OpenBSDVirtual

@pytest.fixture
def openbsd_virtual(mocker):
    module_mock = MagicMock()
    module_mock.run_command = MagicMock(return_value=(0, 'None', ''))
    return OpenBSDVirtual(module=module_mock)

@pytest.fixture
def mock_get_file_content(mocker):
    return mocker.patch('ansible.module_utils.facts.virtual.openbsd.get_file_content')

def test_get_virtual_facts_with_vmm_in_dmesg_boot(openbsd_virtual, mock_get_file_content):
    # Mock the dmesg.boot content to include a line that matches the regex
    mock_get_file_content.return_value = "vmm0 at mainbus0: VMX/EPT\n"

    # Call the method under test
    virtual_facts = openbsd_virtual.get_virtual_facts()

    # Assertions to ensure the method behaves as expected
    assert virtual_facts['virtualization_type'] == 'vmm'
    assert virtual_facts['virtualization_role'] == 'host'
    assert 'vmm' in virtual_facts['virtualization_tech_host']
    assert virtual_facts['virtualization_tech_guest'] == set()

    # Ensure the mock was called with the expected arguments
    mock_get_file_content.assert_called_once_with(OpenBSDVirtual.DMESG_BOOT)

def test_get_virtual_facts_without_vmm_in_dmesg_boot(openbsd_virtual, mock_get_file_content):
    # Mock the dmesg.boot content to not include a line that matches the regex
    mock_get_file_content.return_value = "random line\n"

    # Call the method under test
    virtual_facts = openbsd_virtual.get_virtual_facts()

    # Assertions to ensure the method behaves as expected
    assert virtual_facts['virtualization_type'] == ''
    assert virtual_facts['virtualization_role'] == ''
    assert 'vmm' not in virtual_facts['virtualization_tech_host']
    assert virtual_facts['virtualization_tech_guest'] == set()

    # Ensure the mock was called with the expected arguments
    mock_get_file_content.assert_called_once_with(OpenBSDVirtual.DMESG_BOOT)
