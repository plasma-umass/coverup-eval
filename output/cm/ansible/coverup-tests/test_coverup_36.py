# file lib/ansible/module_utils/facts/hardware/netbsd.py:67-99
# lines [67, 68, 70, 71, 72, 73, 74, 75, 76, 77, 78, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 96, 97, 99]
# branches ['73->74', '73->75', '76->77', '76->92', '81->82', '81->86', '82->83', '82->84', '86->87', '86->90', '88->76', '88->89', '90->76', '90->91', '92->93', '92->96']

import os
import pytest
from ansible.module_utils.facts.hardware.netbsd import NetBSDHardware
from unittest.mock import MagicMock, patch

# Define a fixture for the mock open function
@pytest.fixture
def mock_file_lines():
    cpuinfo_content = """model name: Intel(R) Xeon(R) CPU
physical id: 0
cpu cores: 4
model name: Intel(R) Xeon(R) CPU
physical id: 0
cpu cores: 4
"""
    return cpuinfo_content.splitlines()

# Define the test function
def test_get_cpu_facts(mock_file_lines):
    with patch('ansible.module_utils.facts.hardware.netbsd.os.access', return_value=True):
        with patch('ansible.module_utils.facts.hardware.netbsd.get_file_lines', return_value=mock_file_lines):
            # Mock the module parameter required by the Hardware class
            mock_module = MagicMock()
            hardware = NetBSDHardware(mock_module)
            cpu_facts = hardware.get_cpu_facts()

            # Assertions to verify postconditions
            assert 'processor' in cpu_facts
            assert cpu_facts['processor'] == ['Intel(R) Xeon(R) CPU', 'Intel(R) Xeon(R) CPU']
            assert cpu_facts['processor_count'] == 1
            assert cpu_facts['processor_cores'] == 4

# Clean up after the test
@pytest.fixture(autouse=True)
def cleanup():
    yield
    # No cleanup needed for this test as we are mocking os.access and get_file_lines
