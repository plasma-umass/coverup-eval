# file lib/ansible/module_utils/facts/system/chroot.py:42-47
# lines [42, 43, 44, 46, 47]
# branches []

import pytest
from ansible.module_utils.facts.system.chroot import ChrootFactCollector

# Mock function to simulate is_chroot behavior
def mock_is_chroot(module):
    return True

# Test function to cover ChrootFactCollector.collect
def test_chroot_fact_collector(mocker):
    # Setup the mock for is_chroot
    mocker.patch('ansible.module_utils.facts.system.chroot.is_chroot', side_effect=mock_is_chroot)
    
    # Create an instance of ChrootFactCollector
    chroot_collector = ChrootFactCollector()
    
    # Call the collect method
    facts = chroot_collector.collect()
    
    # Assert that the returned facts include 'is_chroot' key with the expected value
    assert 'is_chroot' in facts
    assert facts['is_chroot'] is True
