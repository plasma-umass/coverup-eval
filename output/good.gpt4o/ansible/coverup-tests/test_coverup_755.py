# file lib/ansible/module_utils/facts/virtual/freebsd.py:77-79
# lines [77, 78, 79]
# branches []

import pytest
from unittest.mock import patch
from ansible.module_utils.facts.virtual.freebsd import FreeBSDVirtualCollector, FreeBSDVirtual

def test_freebsd_virtual_collector_initialization():
    collector = FreeBSDVirtualCollector()
    assert isinstance(collector, FreeBSDVirtualCollector)
    assert collector._fact_class == FreeBSDVirtual
    assert collector._platform == 'FreeBSD'

@patch('ansible.module_utils.facts.virtual.freebsd.FreeBSDVirtualCollector._fact_class')
@patch('ansible.module_utils.facts.virtual.freebsd.FreeBSDVirtualCollector._platform', 'FreeBSD')
def test_freebsd_virtual_collector_fact_class_and_platform(mock_fact_class):
    collector = FreeBSDVirtualCollector()
    assert collector._fact_class == mock_fact_class
    assert collector._platform == 'FreeBSD'
