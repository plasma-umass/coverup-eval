# file: lib/ansible/module_utils/facts/hardware/openbsd.py:48-64
# asked: {"lines": [48, 49, 50, 52, 53, 54, 55, 56, 59, 60, 61, 62, 64], "branches": []}
# gained: {"lines": [48, 49, 50, 52, 53, 54, 55, 56, 59, 60, 61, 62, 64], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.facts.hardware.openbsd import OpenBSDHardware
from ansible.module_utils.facts import timeout

@pytest.fixture
def openbsd_hardware():
    module = MagicMock()
    module.run_command = MagicMock(return_value=(0, "0", ""))
    hardware = OpenBSDHardware(module)
    hardware.sysctl = {
        'hw.ncpuonline': '4',
        'hw.model': 'Intel(R) Xeon(R) CPU',
        'hw.usermem': '16777216',
        'hw.disknames': 'sd0,sd1',
        'hw.product': 'TestProduct',
        'hw.version': '1.0',
        'hw.uuid': '1234-5678',
        'hw.serialno': 'SN123456',
        'hw.vendor': 'TestVendor'
    }
    return hardware

def test_populate(openbsd_hardware):
    with patch.object(OpenBSDHardware, 'get_processor_facts', return_value={'processor': ['Intel(R) Xeon(R) CPU'], 'processor_count': 4, 'processor_cores': 4}), \
         patch.object(OpenBSDHardware, 'get_memory_facts', return_value={'memfree_mb': 1024, 'memtotal_mb': 16384, 'swapfree_mb': 2048, 'swaptotal_mb': 4096}), \
         patch.object(OpenBSDHardware, 'get_device_facts', return_value={'devices': ['sd0', 'sd1']}), \
         patch.object(OpenBSDHardware, 'get_dmi_facts', return_value={'product_name': 'TestProduct', 'product_version': '1.0', 'product_uuid': '1234-5678', 'product_serial': 'SN123456', 'system_vendor': 'TestVendor'}), \
         patch.object(OpenBSDHardware, 'get_uptime_facts', return_value={'uptime_seconds': 3600}), \
         patch.object(OpenBSDHardware, 'get_mount_facts', return_value={'mounts': [{'mount': '/', 'device': '/dev/sd0a', 'fstype': 'ffs', 'options': 'rw'}]}):
        
        facts = openbsd_hardware.populate()
        
        assert 'processor' in facts
        assert 'memfree_mb' in facts
        assert 'devices' in facts
        assert 'product_name' in facts
        assert 'uptime_seconds' in facts
        assert 'mounts' in facts

def test_populate_timeout(openbsd_hardware):
    with patch.object(OpenBSDHardware, 'get_processor_facts', return_value={'processor': ['Intel(R) Xeon(R) CPU'], 'processor_count': 4, 'processor_cores': 4}), \
         patch.object(OpenBSDHardware, 'get_memory_facts', return_value={'memfree_mb': 1024, 'memtotal_mb': 16384, 'swapfree_mb': 2048, 'swaptotal_mb': 4096}), \
         patch.object(OpenBSDHardware, 'get_device_facts', return_value={'devices': ['sd0', 'sd1']}), \
         patch.object(OpenBSDHardware, 'get_dmi_facts', return_value={'product_name': 'TestProduct', 'product_version': '1.0', 'product_uuid': '1234-5678', 'product_serial': 'SN123456', 'system_vendor': 'TestVendor'}), \
         patch.object(OpenBSDHardware, 'get_uptime_facts', return_value={'uptime_seconds': 3600}), \
         patch.object(OpenBSDHardware, 'get_mount_facts', side_effect=timeout.TimeoutError):
        
        facts = openbsd_hardware.populate()
        
        assert 'processor' in facts
        assert 'memfree_mb' in facts
        assert 'devices' in facts
        assert 'product_name' in facts
        assert 'uptime_seconds' in facts
        assert 'mounts' not in facts
