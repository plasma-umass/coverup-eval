# file lib/ansible/module_utils/facts/virtual/openbsd.py:72-74
# lines [72, 73, 74]
# branches []

import pytest
from ansible.module_utils.facts.virtual.openbsd import OpenBSDVirtualCollector, OpenBSDVirtual
from ansible.module_utils.facts.virtual.base import VirtualCollector

def test_openbsd_virtual_collector():
    collector = OpenBSDVirtualCollector()
    
    # Verify that the collector is an instance of VirtualCollector
    assert isinstance(collector, VirtualCollector)
    
    # Verify that the _fact_class is set correctly
    assert collector._fact_class == OpenBSDVirtual
    
    # Verify that the _platform is set correctly
    assert collector._platform == 'OpenBSD'
