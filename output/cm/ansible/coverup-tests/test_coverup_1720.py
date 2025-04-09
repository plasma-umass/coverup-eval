# file lib/ansible/module_utils/facts/hardware/freebsd.py:151-170
# lines []
# branches ['157->170']

import pytest
from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware
from unittest.mock import Mock, patch

# Define a test function to cover the missing branch
def test_get_mount_facts_with_empty_fstab_content(mocker):
    # Mock the get_file_content function to return an empty fstab content
    fstab_content = ""
    mocker.patch(
        'ansible.module_utils.facts.hardware.freebsd.get_file_content',
        return_value=fstab_content
    )

    # Mock the module parameter for FreeBSDHardware
    module_mock = Mock()

    # Create an instance of FreeBSDHardware with the mocked module
    freebsd_hardware = FreeBSDHardware(module=module_mock)

    # Call the get_mount_facts method
    mount_facts = freebsd_hardware.get_mount_facts()

    # Assert that the returned mount_facts contains an empty 'mounts' list
    assert mount_facts['mounts'] == []
