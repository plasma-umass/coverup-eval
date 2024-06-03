# file lib/ansible/module_utils/facts/virtual/hpux.py:70-72
# lines [70, 71, 72]
# branches []

import pytest
from ansible.module_utils.facts.virtual.hpux import HPUXVirtualCollector

def test_hpux_virtual_collector():
    # Create an instance of HPUXVirtualCollector
    collector = HPUXVirtualCollector()

    # Assert that the _fact_class attribute is set correctly
    assert collector._fact_class.__name__ == 'HPUXVirtual'

    # Assert that the _platform attribute is set correctly
    assert collector._platform == 'HP-UX'
