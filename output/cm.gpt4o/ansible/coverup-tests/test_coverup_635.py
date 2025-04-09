# file lib/ansible/module_utils/facts/system/chroot.py:42-47
# lines [42, 43, 44, 46, 47]
# branches []

import pytest
from unittest.mock import Mock, patch
from ansible.module_utils.facts.system.chroot import ChrootFactCollector

def test_chroot_fact_collector_collect(mocker):
    # Mock the is_chroot function
    mock_is_chroot = mocker.patch('ansible.module_utils.facts.system.chroot.is_chroot', return_value=True)
    
    # Create an instance of ChrootFactCollector
    collector = ChrootFactCollector()
    
    # Call the collect method
    result = collector.collect(module=Mock())
    
    # Assert that is_chroot was called once
    mock_is_chroot.assert_called_once()
    
    # Assert the result is as expected
    assert result == {'is_chroot': True}
