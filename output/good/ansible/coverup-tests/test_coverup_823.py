# file lib/ansible/module_utils/facts/virtual/freebsd.py:77-79
# lines [77, 78, 79]
# branches []

import pytest
from ansible.module_utils.facts.virtual.freebsd import FreeBSDVirtualCollector

# Assuming the FreeBSDVirtual class is defined somewhere in the module
# If not, we would need to mock it or define a dummy version for testing purposes

# Mocking the FreeBSDVirtual class for the purpose of this test
class MockFreeBSDVirtual:
    pass

@pytest.fixture
def freebsd_virtual_collector(mocker):
    # Patch the FreeBSDVirtualCollector to use the MockFreeBSDVirtual class
    mocker.patch.object(FreeBSDVirtualCollector, '_fact_class', new=MockFreeBSDVirtual)
    return FreeBSDVirtualCollector()

def test_freebsd_virtual_collector_initialization(freebsd_virtual_collector):
    assert isinstance(freebsd_virtual_collector, FreeBSDVirtualCollector)
    assert freebsd_virtual_collector._fact_class is MockFreeBSDVirtual
    assert freebsd_virtual_collector._platform == 'FreeBSD'
