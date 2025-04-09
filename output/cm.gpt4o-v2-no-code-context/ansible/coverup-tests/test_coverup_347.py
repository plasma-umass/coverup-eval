# file: lib/ansible/module_utils/facts/hardware/darwin.py:79-90
# asked: {"lines": [79, 80, 81, 82, 83, 85, 86, 87, 88, 90], "branches": [[81, 82], [81, 85]]}
# gained: {"lines": [79, 80, 81, 82, 83, 85, 86, 87, 88, 90], "branches": [[81, 82], [81, 85]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.facts.hardware.darwin import DarwinHardware

class TestDarwinHardware:
    @pytest.fixture
    def darwin_hardware(self):
        with patch('ansible.module_utils.facts.hardware.darwin.DarwinHardware', autospec=True) as mock_darwin_hardware:
            instance = mock_darwin_hardware.return_value
            instance.sysctl = {}
            instance.get_cpu_facts = DarwinHardware.get_cpu_facts.__get__(instance)
            yield instance

    def test_get_cpu_facts_intel(self, darwin_hardware):
        darwin_hardware.sysctl = {
            'machdep.cpu.brand_string': 'Intel(R) Core(TM) i7-8565U CPU @ 1.80GHz',
            'machdep.cpu.core_count': 4,
            'hw.logicalcpu': 8
        }
        cpu_facts = darwin_hardware.get_cpu_facts()
        assert cpu_facts['processor'] == 'Intel(R) Core(TM) i7-8565U CPU @ 1.80GHz'
        assert cpu_facts['processor_cores'] == 4
        assert cpu_facts['processor_vcpus'] == 8

    def test_get_cpu_facts_powerpc(self, darwin_hardware):
        darwin_hardware.sysctl = {
            'hw.physicalcpu': 2,
            'hw.ncpu': 4
        }
        system_profile = {
            'Processor Name': 'PowerPC G4',
            'Processor Speed': '1.25 GHz'
        }
        darwin_hardware.get_system_profile = MagicMock(return_value=system_profile)
        cpu_facts = darwin_hardware.get_cpu_facts()
        assert cpu_facts['processor'] == 'PowerPC G4 @ 1.25 GHz'
        assert cpu_facts['processor_cores'] == 2
        assert cpu_facts['processor_vcpus'] == 4
